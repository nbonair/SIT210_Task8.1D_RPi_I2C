import smbus 
import time
bus = smbus.SMBus(1)
DEVICE     = 0x23 # Default device I2C address

POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20
def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number. Optional parameter 'decimals'
  # will round to specified number of decimal places.
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr = DEVICE):
    data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
    lightLevel = convertToNumber(data)
    if lightLevel < 20:
          return "too dark"
    elif (lightLevel < 50):
        return "dark"
    elif (lightLevel < 80):
        return "medium"
    elif (lightLevel < 110):
        return "bright"
    else:
        return "too bright"
try:
    while True:
        lightLevel = readLight()
        print("Current light level: ",lightLevel)
        time.sleep(1)
except KeyboardInterrupt:
    pass
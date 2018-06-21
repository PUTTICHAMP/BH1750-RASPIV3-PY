import smbus
import time

DEVICE     =  0x23
POWER_DOWN =  0x00
POWER_ON   =  0x01
RESET      =  0x07
ONE_TIME_HIGH_RES_MODE = 0x20

bus = smbus.SMBus(1)

def convertToNumber(data):
    return((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
  return convertToNumber(data)

def main():
  while True:
    print"Light Level : " + str(readLight()) + " lux"
    time.sleep(0.5)

if __name__ =="__main__":
    main()

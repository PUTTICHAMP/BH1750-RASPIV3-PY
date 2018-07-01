from firebase import firebase
import socket
import requests
import urllib2
import os
import smbus
import time
import json
import sys


DEVICE     =  0x23
POWER_DOWN =  0x00
POWER_ON   =  0x01
RESET      =  0x07
ONE_TIME_HIGH_RES_MODE = 0x20

firebase = firebase.FirebaseApplication('https://smartfactory-193909.firebaseio.com/',None)

bus = smbus.SMBus(1)

def internet_on ()
    try:
        urllib2.urlopen('https://www.google.com', timeout=1)
        print "Internet Connect"
	return True
    except urllib2.URLError as err:
	print "Internet Disconnect"
	print err.message
        return False
def update_firebase(light):

 # data = {"Light":light}
   firebase.put("/BH1750","/Light",light)
 # firebase.post('HTU21D',data)
 # firebase.put("/HTU21D", "/Humid",Humid)

def convertToNumber(data):
    return((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
  return convertToNumber(data)

def main():
  try :
     while True:
	 internet_on()
         update_firebase(str(readLight()))
         print"Light Level : " + str(readLight()) + " lux"
         time.sleep(0.5)
  except IOError as e:
     print('INTERNET ERROR',e)

if __name__ =="__main__":
     main()















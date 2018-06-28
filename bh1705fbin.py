from firebase import firebase
import subprocess as sp
import os
import smbus
import time
import json
import sys

hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print hostname, 'ready'
else:
  print hostname, 'down!'

DEVICE     =  0x23
POWER_DOWN =  0x00
POWER_ON   =  0x01
RESET      =  0x07
ONE_TIME_HIGH_RES_MODE = 0x20

firebase = firebase.FirebaseApplication('https://smartfactory-193909.firebaseio.com/',None)

bus = smbus.SMBus(1)

def update_firebase(light):
  # data = {"Light":light}
   firebase.put("/BH1750","/Light",light)
 # firebase.post('HTU21D',data)
 # firebase.put("/HTU21D", "/Humid",Humid)

#def ipcheck():
#    ip = "192.168.43.204"
#    status,result = sp.getstatusoutput("ping -c1 -w2"+ ip)
#    if status == 0:
#       print("System " + ip + " is UP !")
#    else:
#       print("System " + ip + " is DOWN !")

def convertToNumber(data):
    return((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
  return convertToNumber(data)

def main():
 try:
  while True:
    update_firebase(str(readLight()))
    print"Light Level : " + str(readLight()) + " lux"
    time.sleep(0.5)

 except IOError as e:
    print('I/0 error:',e)
 

if __name__ =="__main__":
     main()


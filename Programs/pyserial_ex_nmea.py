# Importing libraries
## importing pandas for data manipulation 
from pandas import read_csv, DataFrame, concat, merge 

## importing operating sys library for traversing file paths
import os

## importing regular expressions lib
import re

## importing numpy for data manipulation
import numpy as np

## importing json for transofmring data to json obect
import json


##importing sys
import sys

##importing serial
import serial

## importing io

import io

##importing pynmea2
import pynmea2

## instantite serial connection for NMEA data
ser = serial.Serial('/dev/rfcomm0', 1000000, timeout=5.0)
ser.flushInput()
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
sio.flush()
'''
serv = serial.Serial('/dev/ttyUSB0', 9600, timeout=5.0)
serv.flushInput()
'''
#ser_bytes = ser.readline()
output = {}
x = 0
genos = []

listex = []
outdict = {}

listCA3 = []
outputCA3 = {}

####
# For capturing and piping serial data from the phone for NMEA data
#
####
while True:
    ser_bytes = ser.readline().decode("utf-8").rstrip('\r\n')
    
    #print(repr(pynmea2.parse(ser_bytes)))
    
    #for entry in output:
        #print (output[entry])
    yellow = json.dumps(output)
    #j = json.dump(output, '/home/pi/Desktop/pyserialjs.json')
    #print(j)
    '''
    while (pynmea2.ParseError == False):
        msg = pynmea2.parse(ser_bytes)
        ten = repr(msg)
        output[ten.split('(')[0]] = ten.split(',')[1:]
    
    output[ser_bytes.split(',')[0]] = ser_bytes.split(',')[1:]
    listex.append(output)
    dft = DataFrame.from_records(listex)
    outone = dft.to_json(orient='records', lines=True)
    print(outone)
    '''
    
    try:
        #can work on pynmea part later. as long as base strings can be sent. Then good.
        #if(pynmea2.nmea.ParseError == False or pynmea2.nmea.SentenceTypeError == False):
        msg = repr(pynmea2.parse(ser_bytes))
        #print(msg)
        ten = str(msg).lstrip('<').rstrip('>')
        output[ten.split('(')[0]] = ten.split(',')[1:].strip(')')
        #listex.append(output)
        
    except:
        output[ser_bytes.split(',')[0]] = ser_bytes.split(',')[1:]
    
    listex.append(output)
    
    #listex.append(output)
    dft = DataFrame.from_records(listex)
    outone = dft.to_json(orient='records', lines=True)
    print(outone)
    
    with open('/home/pi/Desktop/pyserialNMEA.json', 'a') as file_1:
            #file.write(repr(msg), '\n')
            print(outone, file=file_1)
    '''
    try:
        dft = DataFrame.from_records(listex)
        outone = dft.to_json(orient='records', lines=True)
        print(outone)
    except:
        jack = "jack"
    '''
    '''
    try:
        #listex.append(msg)
        #print(ser_bytes)
        msg = pynmea2.parse(ser_bytes)
        #print(repr(msg))
        #outdict[repr(msg.split('(')[0])] = repr(msg.split[1:])
        #print("outdict", "\n", outdict)
        #j = json.loads(outdict)
        
        #listex.append(ser_bytes)
        #print(listex)
        #j = json.dump(repr(msg), file_1, indent=2)
        #print("j is printing:", j)
       
        with open('/home/pi/Desktop/pyserialjs.json', 'a') as file_1:
            #file.write(repr(msg), '\n')
            print(repr(msg), file=file_1)
            #print(json.dump(repr(msg), file_1, indent=2), file=file_1)
            
            #sys.stdout.write(file_1)
            #for line in file_1:
                #json.dump(line, file_1, indent=2)
            
    except:
        print("error, not getting nmea data")
    '''
    '''
    try:
        #global msg
        listex.append(msg)
        
        #print("listex", listex)
        
    except:
        print("not getting msg into list")
        continue
    '''
    '''
    try:
        dft = DataFrame.from_records(listex)
            #print(dft.head())

        dft.fillna('N/A')

        dft_json = dft.to_json(orient='records', lines=True)
        #print("dft_json", dft_json)
    except:
        print("not creating df nor json")
        continue
    '''

   
    '''
    with open('/home/pi/Desktop/pyserialjs.json', 'r') as fileo:
            temp = fileo.read().splitlines()
            
            for line in temp:
                
                print(line)
   '''

###
# For capturing and piping CA3 data
####
'''
while True:
    serv_bytes = serv.readline().decode("utf-8").rstrip('\r\n')
    
    #print(repr(pynmea2.parse(ser_bytes)))
    
    #for entry in output:
        #print (output[entry])
    yellow = json.dumps(output)
    #j = json.dump(output, '/home/pi/Desktop/pyserialjs.json')
    #print(j)
    outputCA3[serv_bytes]
    listCA3.append(output_CA3)
    dfb = DataFrame.from_records(list_CA3)
    outtwo = dfb.to_json(orient='records', lines=True)
    #print(outtwo)
    try:
       dfa = read_csv(serv_bytes, sep='\t', header=(0))
       df_CA3 = DataFrame(data=dfa)
       df_CA3.fillna('NaN')
       CA3_json = df_CA3.to_json(orient='index')
            
    except:
        output[ser_bytes.split(',')[0]] = ser_bytes.split(',')[1:]
    
    listCA3.append(output)
    
    #listex.append(output)
    
    with open('/home/pi/Desktop/pyserialCA3.json', 'a') as file_1:
            #file.write(repr(msg), '\n')
            print(outtwo, file=file_1)
'''
'''

#############3
            # Combining the dataframes, conervt to json, and print to stdout
##########33#            

result_0 = dft.join(dfb, how='outer')
## Need to oreitn as a record so you can set lines option to true
lost = result_0.to_json(orient='records', lines=True)
print(lost)
### Direct josn example with json lbry
#with open('/home/pi/Desktop/pyserail.txt', 'r') as file_2:
        #file.write(repr(msg), '\n')
        #print(repr(msg), file=file_1)

#j = json.loads(outdict)
'''
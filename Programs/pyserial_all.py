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

#importing csv
import csv
##importing sys
import sys

##importing serial
import serial


# Importing StringIO
#import StringIO
## importing io

import io

##importing pynmea2
import pynmea2


'''
Part 1: Capturing data from NMEA Serial Stream
'''

#############
# Variables
#############

listex = []
output = {}

## instantiate serial connection for NMEA data
ser = serial.Serial('/dev/rfcomm0', 1000000, timeout=5.0)
ser.flushInput()

################################################################
# While loop to capture, process, and export NMEA data stream  #
################################################################

while True:
    ser_bytes = ser.readline().decode("utf-8").rstrip('\r\n')
   
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
    global dft = DataFrame.from_records(listex)
    outone = dft.to_json(orient='records', lines=True)
    print(outone)
    
    with open('/home/pi/Desktop/pyserialNMEA.json', 'a') as file_1:
            #file.write(repr(msg), '\n')
            print(outone, file=file_1)

'''
Part 2: Capture and process CA3 data
'''
#############
# Variables
############
listCA3 = []

## instantiate serial connection for CA3 data stream

serv = serial.Serial('/dev/ttyUSB0', 9600, timeout=10.0)
serv.flushInput()

################################################################
# While loop to capture, process, and export CA3 data stream   #
################################################################

while True:
    serv_bytes = serv.readline().decode("utf-8").strip('\r\n')
    serv_bytes = serv_bytes.replace('\x00', "")
    serv_bytes = serv_bytes.split('\t')
    
   
    listCA3.append(serv_bytes)
    
    
    try:
        dfe = DataFrame.from_records(listCA3, columns = ['Ah', 'V', 'A', 'S', 'D', 'Deg',
                                                         'RPM', 'HW', 'Nm', 'ThI', 'ThO',
                                                         'AuxA', 'AuxD', 'Flgs'])
      
        outtwo = dfe.to_json(orient='records', lines=True)
        
        print(outtwo)
    
        with open('/home/pi/Desktop/pyserialCA3.json', 'a') as file_1:
                #file.write(repr(msg), '\n')
                print(outtwo, file=file_1)
        
        continue
    
    except:
        #print('did not read file')
        continue
    
####################################################################################
#            Combining the dataframes, conervt to json, and print to stdout
##########33########################################################################  
    try:
        
        comb_df = dft.join(dfe, how='outer')
        ## Need to oreitn as a record so you can set lines option to true
        comb_out = comb_df.to_json(orient='records', lines=True)
        print(comb_out)
    
    except:
        continue

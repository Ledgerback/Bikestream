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

## instantite serial connection for CA3 data

serv = serial.Serial('/dev/ttyUSB0', 9600, timeout=10.0)
serv.flushInput()

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


###
# For capturing and piping CA3 data
####


##hrlpful sources:

# https://stackoverflow.com/questions/38883476/how-to-remove-those-x00-x00
while True:
    serv_bytes = serv.readline().decode("utf-8").strip('\r\n')
    serv_bytes = serv_bytes.replace('\x00', "")
    serv_bytes = serv_bytes.split('\t')
    #serv_bytes = serv_bytes.split('\t')
    #serv_bytes = serv_bytes.strip('\x')
    #print(serv_bytes, 'serv_bytes \n \n')
    #print(repr(pynmea2.parse(ser_bytes)))
    '''
    for x in range(10):
        print(serv_bytes)
        x = x + 1
    '''
    listCA3.append(serv_bytes)
    #print(listCA3)
    '''
    for line in listCA3:
        outputCA3[str(line.split(',')[0])] = outputCA3[str(line.split(',')[1:])]
        listCA3.append(outputCA3)
        '''
        #print(outputCA3, '\n', '\n',  listCA3)
    #outputCA3 = outputCA3[serv_bytes]
    #listCA3[serv_bytes.split('\t')[0]] = listCA3[serv_bytes.split('\t')[1:]]
    #listCA3.append(serv_bytes)
    #print(listCA3)
    #outputCA3[serv_bytes.split('\t')[0]] = outputCA3[serv_bytes.split('\t')[1:]]
    #print(outputCA3)
    #outputCA3 = outputCA3[dict(serv_bytes)]
    #print(listCA3)
    
    #yung = DataFrame.from_records(list(listCA3))
    #print(yung.head())
    
    #print(outputCA3)
    #jone = read_csv(serv_bytes,  sep='\t', index_col=False)
    #print(jone.head())
    #for entry in output:
        #print (output[entry])
    '''
    yellow = json.dumps(listCA3)
    print(yellow, 'yellow')
    '''
    #j = json.dump(output, '/home/pi/Desktop/pyserialjs.json')
    #print(j)
    '''
    outputCA3[serv_bytes]
    listCA3.append(output_CA3)
    dfb = DataFrame.from_records(list_CA3)
    outtwo = dfb.to_json(orient='records', lines=True)
    #print(outtwo)
    '''
    '''
    try:
       dfa = read_csv(serv_bytes, sep='\t', header=(0))
       df_CA3 = DataFrame(data=dfa)
       df_CA3.fillna('NaN')
       CA3_json = df_CA3.to_json(orient='index')
       print(CA3_json)
        
    except:
        #output[serv_bytes.split(',')[0]] = serv_bytes.split(',')[1:]
        print("error")
       ''' 
    #listCA3.append(output)
    #print(listCA3, 'listCA3')
    listCA3.append(serv_bytes)
    
    
    try:
        dfe = DataFrame.from_records(listCA3, columns = ['Ah', 'V',  'A','S', 'D', 'Deg', 'RPM', 'HW', 'Nm', 'ThI', 'ThO', 'AuxA', 'AuxD', 'Flgs'])
    #print(dfe.head(), 'dfe_head')
    
        tony = dfe.to_json(orient='records', lines=True)
        print(tony)
    #listex.append(output)
    
        with open('/home/pi/Desktop/pyserialCA3.json', 'a') as file_1:
                #file.write(repr(msg), '\n')
                print(tony, file=file_1)
        continue
    except:
        #print('did not read file')
        continue

## goign to try the CSV lbry

# refer to https://stackoverflow.com/questions/16251506/building-a-dictionary-from-a-tab-delimited-file-in-a-pythonic-way
'''
data = {}
for entry in csv.DictReader(serv_bytes, delimiter='\t'):
    data[entry['sku']] = [entry['delivered-price-euro']]
    print(data)
'''
#############3
            # Combining the dataframes, conervt to json, and print to stdout
##########33#            

#result_0 = dft.join(dfb, how='outer')
## Need to oreitn as a record so you can set lines option to true
#lost = result_0.to_json(orient='records', lines=True)
#print(lost)
### Direct josn example with json lbry
#with open('/home/pi/Desktop/pyserail.txt', 'r') as file_2:
        #file.write(repr(msg), '\n')
        #print(repr(msg), file=file_1)

#j = json.loads(outdict)


# Summary

############################

# Summary

## Purpose

##########################################################################$
# To convert data in file from csv/tsv
# format to json format
##########################################################################$

## Tools

################################3#########################################$
# Will use pandas lbry to load, convert, and export data                  $ 
# will use re lbry to match expected filename with true filename          $   
# will use os lbry to traverse file directories to find path to filenames $
###########33#############################################################$


#############################

## Going to make this work with pandas library

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
## importing json_normalize to structure semi-sectructured json-like objects
#from pandas.io.json import json_normalize

## Importing pynmea ot parse through NMEA strings
#import pynmea2

# Defining Variables

###########################################################
# @rootdir root directory of the file                     # 
# @reg_exp_0 regex for CA3 filename                       #
# @reg_exp_1 regex for NMEA filename                      #
# @rootreal placeholder for the true path of the filename #
###########################################################
rootdir = "/home/pi/Desktop"

reg_exp_0 = re.compile(r'CA3\d+.txt')
#reg_exp_0 = re.compile(r'CA3\d+.txt')

reg_exp_1 = re.compile(r'NMEA\d+.txt')

rootreal = ""

CA3_filepath = ""

NMEA_filepath = ""

'''
Adding While loop so this will continuously run
'''

while True:

    # Finding the filepath of the CA3 file

    ###########################################################
    # @root root iterator for os.walk                         #
    # @dirs directories iterator for os.walk                  #
    # @files files iterator for os.walk                       #
    # @reg_exp_0 regex for CA3 filename                       #
    # @reg_exp_1 regex for NMEA filename                      #
    # @rootreal placeholder for the true path of the filename #
    ###########################################################

    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if reg_exp_0.match(file):
                #print(file)
                temp_path = reg_exp_0.match(file)
                CA3_filename = temp_path.group()
                CA3_filepath = os.path.join(root, CA3_filename)
                root_copy = root
                #print(CA3_filepath)
                #print(CA3_filename)
                #break
            #else:
                #print("file is not here")


    # Converting CA3 file data from tab-delimited values to JSON with pandas

    ###########################################################
    # @root root iterator for os.walk                         #
    # @dirs directories iterator for os.walk                  #
    # @files files iterator for os.walk                       #
    # @reg_exp_0 regex for CA3 filename                       #
    # @reg_exp_1 regex for NMEA filename                      #
    # @rootreal placeholder for the true path of the filename #
    ###########################################################

    #print(CA3_filepath)
    dfa = read_csv(CA3_filepath, sep='\t', skiprows= (0), header=(1))
    df_CA3 = DataFrame(data=dfa)

    df_CA3.fillna('NaN')

    CA3_json = df_CA3.to_json(orient='index')

    #print(CA3_json)


    with open(rootreal + 'CA3_testfile.txt','w') as input_fil:
        input_fil.write(CA3_json)
        input_fil.close()
    # Part 2. Finding NMEA File and Data Manipulation

    # Finding the filepath of the NMEA file

    ###########################################################
    # @root root iterator for os.walk                         #
    # @dirs directories iterator for os.walk                  #
    # @files files iterator for os.walk                       #
    # @reg_exp_0 regex for CA3 filename                       #
    # @reg_exp_1 regex for NMEA filename                      #
    # @rootreal placeholder for the true path of the filename #
    ###########################################################

    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if reg_exp_1.match(file):
                #print(file)
                temp_path = reg_exp_1.match(file)
                NMEA_filename = temp_path.group()
                NMEA_filepath = os.path.join(root, NMEA_filename)
                #root_copy = root
                #print(NMEA_filepath)
                #print(NMEA_filename)
                break
            #else:
                #print("file is not here")
                #break


    # Converting NMEA file data from comma-separated values to JSON with pandas

    ###########################################################
    # @root root iterator for os.walk                         #
    # @dirs directories iterator for os.walk                  #
    # @files files iterator for os.walk                       #
    # @reg_exp_0 regex for CA3 filename                       #
    # @reg_exp_1 regex for NMEA filename                      #
    # @rootreal placeholder for the true path of the filename #
    ###########################################################

    ###########################################################
    # ## Issues                                               #
    # 1. Cannot read file into dataframe because the number
    # of columns is differnt for each row
    # ## Possible solutions
    # 1. Refer to:
    #     - https://stackoverflow.com/questions/15242746/
    #       handling-variable-number-of-columns-with-pandas
    #       -python
    #     - https://stackoverflow.com/questions/37354745/python-import-text-file-where-each-line-has-different-number-of-columns?noredirect=1&lq=1
    #
    # @dirs directories iterator for os.walk                  #
    # @files files iterator for os.walk                       #
    # @reg_exp_0 regex for CA3 filename                       #
    # @reg_exp_1 regex for NMEA filename                      #
    # @rootreal placeholder for the true path of the filename #
    ###########################################################


    '''
    print(NMEA_filepath)
    dfb = pandas.read_csv(NMEA_filepath, sep=',', skiprows=(0, 1), header=None, escapechar='\\', engine='python', error_bad_lines=False)
    df_NMEA = pandas.DataFrame(data=dfb)

    df_NMEA.fillna('NaN')

    #NMEA_json = df_NMEA.to_json()

    #print(NMEA_json)
    '''

    # Alterantive, read in file as dictionary, then pass onto dataframe
    # source: https://stackoverflow.com/questions/4796764/read-file-from-line-2-or-skip-header-row
    # source: https://stackoverflow.com/questions/13637816/reading-file-adding-words-and-numbers-in-line-of-text-into-dictionary
    # source:https://stackoverflow.com/questions/12330522/how-to-read-a-file-without-newlines
    # source: https://stackoverflow.com/questions/37354745/python-import-text-file-where-each-line-has-different-number-of-columns?noredirect=1&lq=1
    # source: https://stackoverflow.com/questions/15242746/handling-variable-number-of-columns-with-pandas-python
    #alterantive without readlines()
    #time = 0
    output = {}
    x = 0
    genos = []

    with open(NMEA_filepath,'r') as input_file:
        next(input_file)
        #nonlines = input_file.read().replace('\n', '')
        
        #nonlines = input_file.read().splitlines()
        temp_file = input_file.read().splitlines()
        #print(temp_file)
        #input_file.strip('\n')
        while x < len(temp_file):
            for line in temp_file:
                #line.read().replace('\n', '')
                output[line.split(',')[0]] = line.split(',')[1:]
                tell = line.split(',')[0]
                lett = line.split(',')[1:]
                genos.append(output) 
                #genos.append(tell) = lett
                temp_dict = {}
                temp_dict[tell] = line.split(',')[1:]
                gold = {}
                gold[tell] = lett
                
                #print(output[line.split(',')[0]], '\n')
                #print(line)
                #output[line[0]] = line[1:]
                #print(len(output))
                x = x + 1
                #print(output)
                '''
                with open(rootreal + 'output_test.txt', 'a+') as jojo:
                    jojo.write(output[line.split(',')[0]])
                    jojo.close()
                '''
        #print(genos)    
        input_file.close()
    #probably need a temporary variable 
    #print(output)
    #print(len(output))
            
    #alternative with readlines()
    # source: https://stackoverflow.com/questions/13637816/reading-file-adding-words-and-numbers-in-line-of-text-into-dictionary
    '''
    #output_1 = {}
    #with open(NMEA_filepath,'r') as input_file_1:
        next(input_file_1)
        for line in input_file_1.readlines():
            #line.strip('\n')
            
            # So you split the line into a list
            temp = line.split(',')
            # So, temp = ['Peter', '17', '29', '24', '284', '72']

            # You could split 'temp' like so:
            #    temp[0] would resolve to 'Peter'
            #    temp[1] would resolve to ['17', '29', '24', '284', '72']
            name, num = temp[0], temp[1:]

            # From there, you could make temp[0] the key and temp[1:] the value.
            # But: notice that the numbers are still represented as strings.
            # So, we use the built-in function map() to turn them into integers.
            output_1[name] = num
        input_file_1.close()

    print(output_1)
    '''


    # Converting NMEA file data from prgm-created dict to JSON with pandas
    #addt'l source:
    #https://thispointer.com/python-pandas-how-to-create-dataframe-from-dictionary/

    ###########################################################
    # @root root iterator for os.walk                         #
    # @dirs directories iterator for os.walk                  #
    # @files files iterator for os.walk                       #
    # @reg_exp_0 regex for CA3 filename                       #
    # @reg_exp_1 regex for NMEA filename                      #
    # @rootreal placeholder for the true path of the filename #
    ###########################################################

    ###########################################################
    # ## Issues                                               #
    # 1. Cannot read file into dataframe because the number
    # of columns is differnt for each row
    # ## Possible solutions
    # 1. Refer to:
    #     - https://stackoverflow.com/questions/15242746/
    #       handling-variable-number-of-columns-with-pandas
    #       -python
    #     - https://stackoverflow.com/questions/37354745/python-import-text-file-where-each-line-has-different-number-of-columns?noredirect=1&lq=1
    #
    # @dirs directories iterator for os.walk                  #
    # @files files iterator for os.walk                       #
    # @reg_exp_0 regex for CA3 filename                       #
    # @reg_exp_1 regex for NMEA filename                      #
    # @rootreal placeholder for the true path of the filename #
    ###########################################################



    ##
    # Trying to import genos file into Pandas
    ##

    dft = DataFrame.from_records(genos)
    #print(dft.head())

    dft.fillna('N/A')

    dft_json = dft.to_json(orient='index')

    with open(rootreal + 'NMEA_testfile.txt','w') as input_fil:
        input_fil.write(dft_json)
        input_fil.close()
    #print(NMEA_filepath)
    #Source:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html
    # Source:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.from_dict.html
    dfc = DataFrame.from_dict(output, orient='index')

    NMEA_json = dfc.to_json(orient='index')

    #print('NMEA_json', '\n', NMEA_json)

    #alternatively, normalizing the data before turning into a dataframe
    # source:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.json_normalize.html
    #normal_json = json_normalize(output)
    #print(normal_json)

    ##alternatively, passing it in as a Series

    ## source:https://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe
    ## #Source:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html
    '''
    dfd = pandas.Series(output)

    dfd.index.name = 'NMEA_string'

    dfd.reset_index()

    dfd.to_json(orient='index')
    #print('dfd', '\n', dfd)

    dfe = pandas.DataFrame([output])
    #print(dfe)
    dfe_json = dfe.to_json()
    #print('dfe_json', '\n', dfe_json)

    #alternative, direct dataframe approach
    # does not work T_T
    #dfg = pandas.DataFrame(output)
    #print('dfg', '\n', dfg)

    dfObj = pandas.DataFrame(list(output.items()))
    #print(dfObj)
    '''
    #addt'l source:
    #https://thispointer.com/python-pandas-how-to-create-dataframe-from-dictionary/

    # Converting NMEA file data from prgm-created dict to JSON with JSON lbry

    ###########################################################
    # @root root iterator for os.walk                         #
    # @dirs directories iterator for os.walk                  #
    # @files files iterator for os.walk                       #
    # @reg_exp_0 regex for CA3 filename                       #
    # @reg_exp_1 regex for NMEA filename                      #
    # @rootreal placeholder for the true path of the filename #
    ###########################################################

    ###########################################################
    # ## Issues                                               #
    # 1. Cannot read file into dataframe because the number
    # of columns is differnt for each row
    # ## Possible solutions
    # 1. Refer to:
    #     - https://stackoverflow.com/questions/15242746/
    #       handling-variable-number-of-columns-with-pandas
    #       -python
    #     - https://stackoverflow.com/questions/37354745/python-import-text-file-where-each-line-has-different-number-of-columns?noredirect=1&lq=1
    #
    # @dirs directories iterator for os.walk                  #
    # @files files iterator for os.walk                       #
    # @reg_exp_0 regex for CA3 filename                       #
    # @reg_exp_1 regex for NMEA filename                      #
    # @rootreal placeholder for the true path of the filename #
    ###########################################################
    #
    #tale = json.dumps(genos, indent=4)
    #print(len(tale), '\n')


    # Parsing NMEA strings with Pynmea2 lbry

    ###########################################################
    # @root root iterator for os.walk                         #
    # @dirs directories iterator for os.walk                  #
    # @files files iterator for os.walk                       #
    # @reg_exp_0 regex for CA3 filename                       #
    # @reg_exp_1 regex for NMEA filename                      #
    # @rootreal placeholder for the true path of the filename #
    ###########################################################

    '''
    with open(NMEA_filepath,'r') as input_file_2:
        next(input_file_2)
        for line in input_file_2.readlines():
            try:
                msg = pynmea2.parse(line)
                print(repr(msg))
            except pynmea2.ParseError as e:
                print('Parse error: {}'.format(e))
                continue
        input_file_2.close()    
    '''

    ## Combining dataframes with concat, merge, or other simila rfunctions

    comb_frame = [dft, df_CA3]

    frames = concat(comb_frame, ignore_index=True, sort=False)

    frame_2 = df_CA3.append(dft, ignore_index=True, sort=False)

    # Seems like using .join() method is the best option;
    #Alternatively, can use .merge() method 
    result_0 = dft.join(df_CA3, how='outer')
    ## Need to oreitn as a record so you can set lines option to true
    lost = result_0.to_json(orient='records', lines=True)
    result_1 = merge(dft, df_CA3, left_index=True, right_index=True, how = 'outer')

    with open(rootreal + 'comb_testfile.txt','w') as input_fil:
        input_fil.write(lost)
        input_fil.close()

    print(lost)
    #tale = json.dumps(result_0, indent=4, sort_keys=True)
    #print(tale)
    #sys.stdout.write(tale)
    #os.write(1, bytes(lost))

import re
import math
from collections import deque

#inputs
input_string = 'happydaysarehereagain'
num_rows = 4

#do some sizing, total number of zig-zags  
num_zz_floor = math.floor(len(input_string)/(2*num_rows-2))
#find total number of columns, 2 -> 1 (1+2-2), 3 -> 2 (1+3-2), 4 -> 3 (1+4-2), 5 -> 4 (1+5-2)
num_zz_width = (1+num_rows-2)
num_cols_total = num_zz_width*num_zz_floor
remainder_cols = math.floor(len(input_string)/(1+num_rows-2))
if (remainder_cols <= num_rows and remainder_cols > 0):
    num_cols_total+=1
elif (remainder_cols >= num_rows):
    num_cols_total+=remainder_cols-num_rows
else:
    num_cols_total+=0

print('num_zz_floor = ',num_zz_floor,' num_cols_total = ',num_cols_total,' num_zz_width = ',num_zz_width)

#allocate num_rows of strings
rows_of_strings = ['']*num_rows

char_index = 0
#for k in range(0,num_zz_floor):
while char_index < len(input_string):
    #populate downward with padding
    print('XXXXXXXXXX ITER XXXXXXXXXXXX')
    if (num_rows >= 3):
        pad = ' '*(num_rows-2)
        for kk in range(0,num_rows):
            rows_of_strings[kk]+=input_string[char_index]+pad
            print('kk = ',kk,' char = ', input_string[char_index])
            print(f'rows_of_strings[%d]=%s'%(kk,rows_of_strings[kk]))
            char_index+=1
            pad = pad[:-1] #remove 1 whitespace
            if (char_index == len(input_string)):
                break
        #add in pad for last row
        rows_of_strings[kk]+=' '*(num_rows-2)
    if ( num_rows >= 3):
        #ws = ''
        pad = ' '*(num_rows-3)
        for kk in range(num_rows-2,0,-1):
            if (char_index == len(input_string)):
                break
            #rows_of_strings[kk]+=ws+input_string[char_index]+pad
            rows_of_strings[kk]+=input_string[char_index]+pad
            print('kk = ',kk,' char = ', input_string[char_index])
            print(f'rows_of_strings[%d]=%s'%(kk,rows_of_strings[kk]))
            #ws += ' '
            pad = pad[:-1]
            char_index+=1
    
for item in rows_of_strings:
    print(item)
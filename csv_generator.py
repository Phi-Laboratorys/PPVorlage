Autor: Manuel Lippert

import pandas as pd
import csv

print('Hello, this program helps by the creation of csv-files.')
print('------------SETUP------------')

name = input('Name of File  | ')
if '.csv' in name:
    filename = name
else:
    filename = name + '.csv'

col_count = int(input('Number of Col | '))
i = 0 
col_names = []
while i < col_count:
    col_name = input('Name of Col '+str(i+1)+' | ')
    col_names.append(col_name)
    i += 1

print('------------DATA-------------')

with open(filename, 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    filewriter.writerow(col_names) #header

    write_data = True
    row_count = 0

    while write_data:

        i = 0
        data = []

        while i < col_count:
            data_elem = input('Row '+str(row_count)+' ; Col '+ str(i)+' | ')
            if 'stop' in data_elem:
                write_data = False
                data.clear()
                break
            else:
                data.append(data_elem)
            i += 1
        
        filewriter.writerow(data)
        row_count += 1
        print('-----------------------------')

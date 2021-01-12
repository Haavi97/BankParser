import sys
import csv
import os
import copy as cp
import datetime as dt

# Personal libraries/scripts
import user_data as ud

fd = os.path.sep  # folder delimiter


def reader(file_name, verbose=True):
    result = []
    current_path = os.getcwd() + fd + ud.data_path + fd + current_month + fd + file_name
    try: 
        with open(current_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=";")
            line_count = 0
            if verbose:
                print('Column names are:')
                for e in ud.fields_list:
                    print('{0:<25s}'.format(e[:24]), end='')
                print('')
            
            buff_str = ''

            for row in csv_reader:
                buffer = {}
                for e in ud.fields_list:
                    value = cp.deepcopy(row[e])
                    try:
                        if value.isnumeric():
                            buffer[e] = int(value)
                        elif e == 'Summa':
                            buffer['Summa'] = float(value.replace(',', '.'))
                        elif value == '':
                            buffer[e] = '--'
                        else:
                            buffer[e] = value
                        if verbose:
                            buff_str += '{0:<25s}'.format(str(buffer[e])[:24])
                        
                    except ValueError:
                        print('\n\n***********\n\n', file=sys.stderr)
                        print("Value Error", file=sys.stderr)
                        print(row, file=sys.stderr)
                        print('\n\n***********\n\n', file=sys.stderr)
                    
                buff_str += '\n'
                
                result.append(buffer)
                line_count += 1
            print('\n\n' + buff_str)

            if verbose:
                print(f'\nProcessed {line_count} lines\n\n')
    except FileNotFoundError:
        print('\n\n***********\n\n', file=sys.stderr)
        print('File Not Found Error.', file=sys.stderr)
        print('Please, provide a correct file name')
        print('Files in this directory:')
        for f in os.listdir(current_path):
            print(f)
        print('Files in this directory:', file=sys.stderr)
        print('\n\n***********\n\n', file=sys.stderr)
    return result



if __name__ == "__main__":
    if len(sys.argv) == 1: 
        max_r = 1000000
        for e in range(max_r):
            print(str((e*100)//max_r) + ' %', end='\r')
        current_month = '{:02d}'.format( int( input("Please enter month:")))
        csv_name = input("Please enter csv file name:")
        result = reader(csv_name)
        print('List of lenght: ' + str(len(result)))
    elif sys.argv[1] == "hello":
        print("hello world!")
    else:
        print(sys.argv)
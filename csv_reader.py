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
    with open(os.getcwd() + fd + ud.data_path + fd + current_month + fd + file_name) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        line_count = 0
        if verbose:
            print(f'Column names are:')
            for e in ud.fields:
                print(f'{e}', end='\t')
            print('')
        
        buff_str = ''

        for row in csv_reader:
            buffer = {}
            for e in ud.fields.keys():
                value = cp.deepcopy(row[e])
                try:
                    if value.isnumeric():
                        buffer[e] = int(value)
                    elif e == 'Summa':
                        buffer['Summa'] = float(value.replace(',', '.'))
                    elif value == '':
                        value = '\t'
                    else:
                        buffer[e] = value
                    if verbose:
                        buff_str += f'{buffer[e]}' + '\t'
                    
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
    return result



if __name__ == "__main__":
    if len(sys.argv) == 1: 
        current_month = '{:02d}'.format( int( input("Please enter month:")))
        csv_name = input("Please enter csv file name:")
        ret = reader(csv_name)
        print(ret)
    else:
        print(sys.argv)
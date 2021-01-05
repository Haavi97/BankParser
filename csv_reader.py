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
            if line_count == 0:
                print(row, end='\n******\n\n')
                line_count += 1
            else:
                buffer = {}
                for e in ud.fields.keys():
                    buffer[e] = cp.deepcopy(row[e])
                    if verbose:
                        buff_str += f'{row[e]}' + '\t'
                buff_str += '\n'

                try:
                    buffer['Summa'] = float(buffer['Summa'].replace(',', '.'))
                except ValueError:
                    print('\n\n***********\n\n', file=sys.stderr)
                    print("Value Error", file=sys.stderr)
                    print(row, file=sys.stderr)
                    print('\n\n***********\n\n', file=sys.stderr)
                
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
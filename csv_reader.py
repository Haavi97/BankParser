import sys
import csv
import os
import copy as cp
import datetime as dt

# Personal libraries/scripts
import user_data as ud

fd = os.path.sep  # folder delimiter


def reader(file_name, current_month=dt.datetime.now().month,
           verbose=True, path=None, fl=ud.fields_list):
    result = []
    current_path = os.getcwd() + fd + ud.data_path + fd + str(current_month) + fd
    if path != None:
        current_path = path
    try:
        with open(current_path + file_name) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=";")

            if verbose:
                print('Column names are:')
                for e in fl:
                    print('{0:<25s}'.format(e[:24]), end='')
                print('')

            buff_str = ''

            line_count = 0
            for row in csv_reader:
                line_count += 1
                print('Columns read: {}'.format(line_count), end='\r')
                buffer = {}
                for e in fl:
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
            print('{0:20}'.format(''), end='\r')
            print('\n\n' + buff_str)

            if verbose:
                print('\nProcessed {} lines\n\n'.format(line_count))
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


def main_csv():
    current_month = '{:02d}'.format(int(input("Please enter month:")))
    csv_name = input("Please enter csv file name:")
    result = reader(csv_name, current_month=current_month)
    return result


if __name__ == "__main__":
    if len(sys.argv) == 1:
        result = main_csv()
        print('List of lenght: ' + str(len(result)))
    elif sys.argv[1] == "hello":
        print("hello world!")
    else:
        print(sys.argv)

import csv
import os
import datetime as dt

# Personal libraries/scripts
import user_data as ud

current_month = dt.date.today().month
csv_name = input("Please enter csv file name:")
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
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                buffer = {}
                for e in ud.fields.keys():
                    buffer[e] = row[e]
                    if verbose:
                        print(f'{row[e]}', end='\t')
                print('')
                sign = '-' if buffer["Deebet/Kreedit (D/C)"] == 'D' else '+'
                buffer['käive'] = float(sign + buffer['Summa'])
                result.append(buffer)
                line_count += 1
        if verbose:
            print(f'\nProcessed {line_count} lines')
    return result
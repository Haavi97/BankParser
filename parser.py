import sys
import os
import logging

import csv_reader
import xl_reader
import xl_writer
import user_data as ud

logging.basicConfig(filename='app.log',
                    filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')

output = sys.stdout


def print_wl(s: str) -> str:
    """
    A wrapper function that prints to the predefined output file
    and at the same time logs an info message 

    Paramete: 
    s: str
    """

    print(s, file=output)
    logging.info(s)


def display_menu():
    print_wl('*********')
    print_wl('MAIN MENU')
    print_wl('*********')
    print_wl('01. Read csv file')
    print_wl('02. Read xls/xlsx file')
    print_wl('03. Display menu')
    print_wl('04. Write read data into xlsx file')
    print_wl('05. Read and write all month files')
    print_wl('**. q, exit, 0\n\n')


def is_csv(fn):
    return fn[-3:] == 'csv'


if __name__ == "__main__":
    running = True
    while running:
        display_menu()
        inp = input()
        if inp in ['q', 'exit', '0']:
            break
        elif inp == '1':
            result = csv_reader.main_csv()
        elif inp == '2':
            xl_reader.main_xl()
        elif inp == '3':
            pass
        elif inp == '4':
            try:
                xl_writer.xl_writer("8", result)
            except:
                print("Nothing read yet")
        elif inp == '5':
            current_month = '{:02d}'.format(int(input("Please enter month:")))
            for fn in ud.file_names:
                if is_csv(fn):
                    read = csv_reader.reader(fn, current_month=current_month)
                    xl_writer.xl_writer(current_month, read)
                else:
                    file_name = ud.cwd + ud.fd + ud.data_path + \
                        ud.fd + current_month + ud.fd + fn
                    read = xl_reader.xlsx_reader(6, 8, 2, xl_reader.check_file(file_name))
                    xl_writer.xl_writer(current_month, read)
        else:
            print("Please, choose a valid number")

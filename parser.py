import sys
import os
import logging
import copy as cp

from csv_reader import reader, main_csv
from xl_reader import xlsx_reader, main_xl
from xl_writer import xl_writer, f_append
from xl_helpers import check_file, xl_map
import user_data as ud

FORMAT = '%(asctime)-15s %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='app.log',
                    filemode='a',
                    format=FORMAT)

output = sys.stdout


def print_wl(s: str) -> str:
    """
    A wrapper function that prints to the predefined output file
    and at the same time logs an info message 

    Parameters: 
    s: str
    """

    print(s, file=output)
    logging.info(s)


def print_wl_error(s: str) -> str:
    """
    A wrapper function that prints to the std.err
    and at the same time logs an error message 

    Parameters: 
    s: str
    """

    print(s, file=sys.stderr)
    logging.error(s)


def display_menu():
    print_wl('*********')
    print_wl('MAIN MENU')
    print_wl('*********')
    print_wl('01. Read csv file')
    print_wl('02. Read xls/xlsx file')
    print_wl('03. Display menu')
    print_wl('04. Write read data into xlsx file')
    print_wl('05. Read and write all month files')
    print_wl('06. Read defaults')
    print_wl('07. Read and write all month files with defaults')
    print_wl('08. Set/unset verbosity')
    print_wl('**. q, exit, 0\n\n')


def is_csv(fn):
    return fn[-3:] == 'csv'


def assign_defaults(data, defaults, ft='csv'):
    name = ud.csv_name if ft == 'csv' else ud.xls_name
    suma = ud.csv_suma if ft == 'csv' else ud.xls_suma
    data_new = cp.deepcopy(data)
    try:
        assigned = 0
        for e in data_new:
            found = False
            for d in defaults:
                if not found:
                    try:
                        suma_i = int(e[suma]*100)
                        if suma_i == 0:
                            print("suma_i = 0")
                            raise ValueError('Suma_i = 0 ')
                        dc = abs(suma_i)/suma_i
                        if d[ud.def_description] == '-':
                            if (e[name] == d[ud.def_name]) & (dc == int(d[ud.def_dc])):
                                for label in ud.def_labs:
                                    e[label] = cp.deepcopy(d[label])
                                found = True
                                assigned += 1
                        else:
                            p1 = (e[name] == d[ud.def_name])
                            p2 = (dc == int(d[ud.def_dc]))
                            p3 = (d[ud.def_description].lower() in e[ud.def_description].lower())
                            if p1 & p2 & p3:
                                for label in ud.def_labs:
                                    e[label] = cp.deepcopy(d[label])
                                found = True
                                assigned += 1 
                    except KeyError:
                        print_wl_error("Probably some entry with missing values")
                        break
        print("Assigned: {} defaults".format(assigned))
    except:
        e = sys.exc_info()[0]
        print_wl_error("An error ocurred assigning defaults.")
        print_wl_error("Exception message: {}".format(e))
    return data_new


if __name__ == "__main__":
    running = True
    verbosity = True
    while running:
        display_menu()
        inp = input()
        try:
            if inp in ['q', 'exit', '0']:
                break
            elif inp == '1':
                result = main_csv()
            elif inp == '2':
                main_xl()
            elif inp == '3':
                pass
            elif inp == '4':
                try:
                    xl_writer("8", result)
                except:
                    print_wl_error("Nothing read yet")
            elif inp == '5':
                current_month = '{:02d}'.format(
                    int(input("Please enter month:")))
                for fn in ud.file_names:
                    if is_csv(fn):
                        read = reader(
                            fn, current_month=current_month, verbose=verbosity)
                        xl_writer(current_month, read)
                    else:
                        file_name = ud.cwd + ud.fd + ud.data_path + \
                            ud.fd + current_month + ud.fd + fn
                        read = xlsx_reader(ud.xl_header_row,
                                           ud.xl_data_row,
                                           ud.xl_data_row - ud.xl_header_row,
                                           check_file(file_name), 
                                           verbose=verbosity)
                        xl_writer(current_month, read, fmap='xl')
            elif inp == '6':
                result = reader(ud.defaults_file,
                                path=ud.defaults_path,
                                fl=ud.defaults_fields_list, 
                                verbose=verbosity)
            elif inp == '7':
                current_month = '{:02d}'.format(
                    int(input("Please enter month:")))
                for fn in ud.file_names:
                    if is_csv(fn):
                        read = reader(
                            fn, current_month=current_month, verbose=verbosity)
                        defaults_read = reader(ud.defaults_file,
                                               path=ud.defaults_path,
                                               fl=ud.defaults_fields_list, 
                                               verbose=verbosity)
                        defualts_assigned = assign_defaults(
                            read, defaults_read)
                        xl_writer(current_month, defualts_assigned,
                                  fmap='csv_def')
                    else:
                        file_name = ud.cwd + ud.fd + ud.data_path + \
                            ud.fd + current_month + ud.fd + fn
                        read = xlsx_reader(ud.xl_header_row,
                                           ud.xl_data_row,
                                           ud.xl_data_row - ud.xl_header_row,
                                           check_file(file_name), 
                                           verbose=verbosity)
                        defaults_read = reader(ud.defaults_file,
                                               path=ud.defaults_path,
                                               fl=ud.defaults_fields_list, 
                                               verbose=verbosity)
                        defualts_assigned = assign_defaults(
                            read, defaults_read, ft='xls')
                        xl_writer(
                            current_month, defualts_assigned, fmap='xl_def')
            elif inp == '8':
                verbosity = not verbosity
                print("Verbosity: {}\n\n".format(verbosity))
            else:
                print_wl("Please, choose a valid number")
        except:
            e = sys.exc_info()[0]
            print_wl_error("An error ocurred.")
            print_wl_error("Exception message: {}".format(e))

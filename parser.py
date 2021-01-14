import sys
import os
import logging

import csv_reader
import xl_reader
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
    print_wl('**. q, exit, 0\n\n')

if __name__ == "__main__":
    running = True
    while running:
        display_menu()
        inp = input()
        if inp in ['q', 'exit', '0']:
            break
        elif inp == '3':
            display_menu() 

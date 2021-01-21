import sys
from openpyxl import load_workbook
from xls2xlsx import XLS2XLSX


import user_data as ud
from xl_helpers import check_file


def xl_writer(current_month, data,  fn=ud.fn):
    current_month = str(current_month)
    workbook = load_workbook(filename=fn, data_only=True)
    try:
        sheet = workbook[current_month]
    except KeyError:
        print("Creating worksheet: \"" + current_month + "\"")
        workbook.create_sheet(current_month)
        sheet = workbook[current_month]
    for element in data:
        f_append(sheet, element)
    workbook.save(fn)


def f_append(sheet, element):
    row = []
    for e in ud.xl_month_fileds:
        try:
            current = element[ud.xl_csv_map[e]]
        except:
            current = ""
        row.append(current)
    sheet.append(row)

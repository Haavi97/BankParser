import sys
from openpyxl import load_workbook
from xls2xlsx import XLS2XLSX


import user_data as ud
from xl_helpers import check_file


def xl_writer(current_month, data,  fn=ud.fn):
    workbook = load_workbook(filename=fn, data_only=True)
    sheet = workbook[str(current_month)]
    for element in data:
        f_append(sheet, element)
    workbook.save(fn)


def f_append(sheet, element):
    row = []
    for e in ud.xl_month_fileds:
        try:
            current = element[e]
        except:
            current = ""
        row.append(current)
    sheet.append(row)
    
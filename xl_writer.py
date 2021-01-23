import sys
from openpyxl import load_workbook
from xls2xlsx import XLS2XLSX


import user_data as ud
from xl_helpers import check_file


def xl_writer(current_month, data,  fn=ud.fn, fmap='csv'):
    current_month = str(current_month)
    workbook = load_workbook(filename=fn, data_only=True)
    try:
        sheet = workbook[current_month]
    except KeyError:
        print("Creating worksheet: \"" + current_month + "\"")
        workbook.create_sheet(current_month)
        sheet = workbook[current_month]
        sheet.append(ud.xl_month_fileds)
    for element in data:
        f_append(sheet, element, ff)
    workbook.save(fn)


def f_append(sheet, element, fmap):
    row = []
    if ff == 'csv':
        fmaps = ud.xl_csv_map
    else:
        fmaps = ud.xl_xl_map
    for e in ud.xl_month_fields:
        try:
            current = element[fmaps[e]]
        except:
            current = ""
        row.append(current)
    sheet.append(row)


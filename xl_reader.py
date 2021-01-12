from openpyxl import load_workbook
import user_data as ud
import win32com.client as win32
import sys


def check_file(fname):
    if fname[-1] != 'x':
        fname = ud.cwd + ud.fd + ud.data_path + ud.fd + current_month + ud.fd + xl_name
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        wb = excel.Workbooks.Open(fname)

        wb.SaveAs(fname + "x", FileFormat=51)  # FileFormat = 51 is for .xlsx extension
        wb.Close()  # FileFormat = 56 is for .xls extension
        excel.Application.Quit()

        return fname + 'x'
    else:
        return fname


def xlsx_reader(header_row, fn):
    workbook = load_workbook(filename=fn, data_only=True)
    sheet = workbook.active
    header = list(list(sheet.iter_rows(min_row=header_row, max_row=header_row, min_col=2))[0])
    print(header)
    result = []
    for row in sheet.iter_rows(min_row=header_row + 1, min_col=2):
        buffer = {}
        for current_cell in row:
            print('{}, {}'.format(current_cell.column, (current_cell.column-1)))
            buffer[header[current_cell.column-2].value] = current_cell.value
        print(buffer)
        result.append(buffer)
    return result


if __name__ == "__main__":
    if len(sys.argv) == 1: 
        current_month = '{:02d}'.format( int( input("Please enter month:")))
        xl_name = input("Please enter xl file name:")
        file_name = ud.cwd + ud.fd + ud.data_path + ud.fd + current_month + ud.fd + xl_name
        result = xlsx_reader(6, check_file(file_name))
        print('List of lenght: ' + str(len(result)))
    elif sys.argv[1] == "hello":
        print("hello world!")
    else:
        print(sys.argv)
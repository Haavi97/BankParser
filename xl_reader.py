import sys
from openpyxl import load_workbook
from xls2xlsx import XLS2XLSX


import user_data as ud



def check_file(fname):
    if fname[-1] != 'x':
        fname_x = fname + 'x'
        x2x = XLS2XLSX(fname)
        x2x.to_xlsx(fname_x)
        return fname_x
    else:
        return fname


def xlsx_reader(header_row, data_row, data_col, fn):
    workbook = load_workbook(filename=fn, data_only=True)
    sheet = workbook.active
    header = list(list(sheet.iter_rows(min_row=header_row, max_row=header_row, min_col=2))[0])

    result = []
    buff_str = ''
    line_count = 0
    for row in sheet.iter_rows(min_row=data_row, min_col=data_col):
        line_count += 1
        buffer = {}
        for current_cell in row:
            e = header[current_cell.column-2].value
            buffer[e] = current_cell.value
            buff_str += '{0:<25s}'.format(str(buffer[e])[:24])
        buff_str += '\n'
        result.append(buffer)
    
    print('\n\n' + buff_str)
    print('\nProcessed {} lines\n\n'.format(line_count))
    
    return result


if __name__ == "__main__":
    if len(sys.argv) == 1: 
        current_month = '{:02d}'.format( int( input("Please enter month:")))
        xl_name = input("Please enter xl file name:")
        file_name = ud.cwd + ud.fd + ud.data_path + ud.fd + current_month + ud.fd + xl_name
        result = xlsx_reader(6, 8, 2, check_file(file_name))
        print('List of lenght: ' + str(len(result)))
    elif sys.argv[1] == "hello":
        print("hello world!")
    else:
        print(sys.argv)
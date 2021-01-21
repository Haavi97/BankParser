from xls2xlsx import XLS2XLSX


def check_file(fname):
    if fname[-1] != 'x':
        fname_x = fname + 'x'
        x2x = XLS2XLSX(fname)
        x2x.to_xlsx(fname_x)
        return fname_x
    else:
        return fname

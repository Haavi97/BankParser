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


def xl_map(data, fmaps=ud.xl_csv_map):
    new_data = []
    for e in data:
        current = {}
        for k in ud.xl_month_fields:
            try:
                current[k] = e[fmaps[k]]
            except:
                current [k] = ''
        new_data.append(current)
    return new_data
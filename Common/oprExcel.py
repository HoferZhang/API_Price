import xlrd
import xlwt
import os
from xlutils.copy import copy


def creat_excel(header, data, filename, sheetname):
    if not os.path.exists(filename):
        if isinstance(header, list):
            if isinstance(data, list):
                if len(header) == len(data):
                    excel = xlwt.Workbook()
                    sheet = excel.add_sheet(sheetname)
                    for index in range(len(header)):
                        sheet.write(0, index, header[index])
                    excel.save(filename)
                    modify_excel(data, filename, sheetname)
                else:
                    return print("header与data长度不一致")
            else:
                return print("data非数组类型")
        else:
            return print("header非数组类型")
    else:
        modify_excel(data, filename, sheetname)


def modify_excel(data, filename, sheetname):
    if os.path.exists(filename):
        excel = xlrd.open_workbook(filename)
        new_book = copy(excel)
        sheet = new_book.get_sheet(0)
        # col = read_excel(filename, sheetname)["cols"]
        # print(col)
        col = 0
        row = read_excel(filename, sheetname)["rows"]
        print(row)

        for index in range(len(data)):
            sheet.write(col + 2, row - 1, data[index])
            row += 1
            new_book.save(filename)


def read_excel(filename, sheetname):
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_name(sheetname)
    return dict(cols=sheet.ncols, rows=sheet.nrows)


a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
b = [1, 2, 3, 4, 5, 6, 7, ]

# creat_excel(a, b, 'good.xls', 'sheet2')
modify_excel(b, 'good.xls', 'sheet2')

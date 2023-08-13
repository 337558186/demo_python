# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/8 11:42
@Auth ： magician
@Desc ： Excel操作
安装pip install xlrd==1.2.0
xlrd 新版本只支持 xls 格式,指定安装 1.2.0 老版本,可以支持xlsx格式
"""

import xlrd, xlwt
from datetime import date, datetime


def read_excel():
    wb = xlrd.open_workbook('r.xlsx')
    # 通过sheet_by_name()方法获取sheet
    # sheet = wb.sheet_by_name('Sheet1')
    # 通过sheet索引值的方式获取sheet，0表示第一个sheet
    sheet = wb.sheet_by_index(0)
    print('sheet的名称：', sheet.name)
    print('sheet的总行数：', sheet.nrows)
    print('sheet的总列数：', sheet.ncols)
    print('第2行第1列的值为：', sheet.row_values(1)[0])
    print('第3行的值为：', sheet.row_values(2))
    print('第2列的值为：', sheet.col_values(1))
    print('第3行第2列的值为：', sheet.cell_value(2, 1))
    print(sheet.cell(2, 1).value)

    # 循环获取每行的数据
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            value = sheet.cell_value(row, col)
            print('第{}行{}列的数据为：{}'.format(row, col, value))


if __name__ == '__main__':
    read_excel()

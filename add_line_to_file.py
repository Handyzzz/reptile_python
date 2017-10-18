#!/Users/handyzzz/.venv/p352/bin python
import xlwt
import xlrd
import xlutils
from xlutils.copy import copy
def add_line(list):
    old_wb = xlrd.open_workbook('data.xls' ,formatting_info=True)
    new_wb = copy(old_wb)
    table = new_wb.get_sheet(0)
    table.row().write(list[0], list[1], list[2])
    new_wb.save('data.xls')

#!/Users/handyzzz/.venv/p352/bin python
# coding=utf-8
import xlwt
import xlrd
from xlutils.copy import copy

# 应该需要爬一行写一行 现在是全部爬完才写的
from xlwt import Workbook

def write_file(data_dic):
    file = Workbook(encoding='utf-8')
    # 指定file以utf-8的格式打开
    table = file.add_sheet('sheet1')
    # 指定打开的文件名
    ldata = []
    print(data_dic)
    num = [a for a in data_dic]
    # for循环指定取出key值存入num中
    num.sort()
    # 字典数据取出后无需，需要先排序

    for x in num:
        # for循环将data字典中的键和值分批的保存在ldata中
        t = [int(x)]
        for a in data_dic[x]:
            t.append(a)
        ldata.append(t)

    for i, p in enumerate(ldata):
        # 将数据写入文件,i是enumerate()函数返回的序号数
        for j, q in enumerate(p):
            table.write(i, j, q)

    file.save('data.xls')
    print('write to file done')

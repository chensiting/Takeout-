#-*- coding: utf-8 -*- 
#@File : getExcelData.py 
#@Time : 2021-02-23 2:25 
#@Author : chensiting
#@Email : 475707078@qq.com 
#@Software: PyCharm

#获取excel数据获取到代码里

#xlrd openpyxl

import xlrd
from xlutils.copy import copy
#xlrd 新建一个表

#1-打开excel表

def get_excelData(sheetName,startRow,endRow):
    resList = []  #存放空列表
    #1- excel表路径
    excelDir ='../data/外卖系统接口测试用例-V1.2.xls'

    #2- 打开excel对象 --formatting_info=True 保持样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    # workSheet =workBook.sheet_names()  #获取所有的表名
    # print(workSheet)
    #3- 获取某一个指定的表
    workSheet =workBook.sheet_by_name(sheetName)
    #4-读取单元格--返回是字符串--cell（行号，列号） 从0开始   列不变，行在变，，行可以for循环
    for one in range(startRow-1,endRow):    #读取用例在代码角度是0开始（1,7），在测试人员角度是从1开始，既然用例是适合测试人员的就从1开始，用例是（2,7),减1就是代码层
        reqBodyData = workSheet.cell(one,9).value  #请求body
        respData =workSheet.cell(one,11).value   #响应数据
        resList.append((reqBodyData,respData))  #为什么有2个小括号：封装一个列表里嵌套元组
    return resList


def set_excelData():
    #1- excel表路径
    excelDir ='../data/外卖系统接口测试用例-V1.2.xls'

    #2- 打开excel对象 --formatting_info=True 保持样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    workBookNew = copy(workBook)
    workSheetNew = workBookNew.get_sheet(0)   #copy出来不能用index和name去取，固定写法get_sheet
    return workBookNew,workSheetNew



if __name__ == '__main__': #ctrl+j 可以打出main
    #print(get_excelData('登录模块'))
    # for one in get_excelData('登录模块'):
    #     print(one)
    set_excelData()
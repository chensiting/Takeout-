#-*- coding: utf-8 -*- 
#@File : getExcelData.py 
#@Time : 2021-02-23 2:25 
#@Author : chensiting
#@Email : 475707078@qq.com 
#@Software: PyCharm

#获取excel数据获取到代码里

#xlrd openpyxl

import xlrd
#1-打开excel表

def get_excelData(sheetName):
    #1- excel表路径
    excelDir ='../data/外卖系统接口测试用例-V1.2.xls'

    #2- 打开excel对象 --formatting_info=True 保持样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    # workSheet =workBook.sheet_names()  #获取所有的表名
    # print(workSheet)
    #3- 获取某一个指定的表
    workSheet =workBook.sheet_by_name(sheetName)

if __name__ == '__main__': #ctrl+j 可以打出main
    get_excelData('登录模块')
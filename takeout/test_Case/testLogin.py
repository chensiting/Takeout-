#-*- coding: utf-8 -*- 
#@File : testLogin.py 
#@Time : 2021-02-25 1:52 
#@Author : chensiting
#@Email : 475707078@qq.com 
#@Software: PyCharm


import json
#1- 读取数据
from takeout.tool.getExcelData import get_excelData,set_excelData    #导入excel表数据
workBookNew,workSheetNew = set_excelData() #元组


#2- 关联请求
dataList = get_excelData("登录模块",2,7) #[(请求body,响应数据),(),()] 元组形式组装外面是列表

from takeout.lib.apiLib.login import Login

# for one in range(0,len(get_excelData("登录模块",2,7))):
#     Login().login(get_excelData("登录模块",2,7))

for one in range(0,len(dataList)):
    print(one)
    res = Login().login(dataList[one][0], False)  #列表的下标再取0

    if res['msg'] == json.loads(dataList[one][1])['msg']:  #响应结果的msg==表格的预期响应值
        #one是下标不是值
        print('---pass---')

        workSheetNew.write(one +1,12,'pass') #(行号，列号，字符串内容)   #

    else:
        print('---fail---')
        workSheetNew.write(one +1, 12, 'fail')



#用index下标会有一个bug，当出现相同值，只会取第一个下标，后来更换成len
# for one in dataList:  #one----元组--(请求body,响应数据)  for遍历
#     #print('表格的预期结果',one)  #取的表格预期的结果
#     res=Login().login(one[0],False)  #要实际的响应结果  #login返回是有2个参数，要返回json要false
#     #print('响应结果',res)
#     #print(one[1])
#     #预期与实际的响应数据进行比较
#     if res['msg'] == json.loads(one[1])['msg']:  #响应结果的msg==表格的预期响应值
#         print('---pass---')
#         #列表.index(元素)---求出该元素的下标
#         workSheetNew.write(dataList.index(one)+1,12,'pass') #(行号，列号，字符串内容)   #
#         # 对象.元素 对象是dataList 元组的index你要把元素放进去求，元素是one index里面需要加元素  行号有问题因为行号是取one，值要用index下标取下标，one是值要填下标，index()+1 one元素是从0开始的，用例0行是不需要的，所以+1取值
#     else:
#         print('---fail---')
#         workSheetNew.write(dataList.index(one) + 1, 12, 'fail')

#3- 写结果
workBookNew.save('../data/res.xls')
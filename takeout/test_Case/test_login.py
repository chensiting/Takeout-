#-*- coding: utf-8 -*- 
#@File : test_login.py 
#@Time : 2021-02-26 2:27 
#@Author : chensiting
#@Email : 475707078@qq.com 
#@Software: PyCharm
import pytest
from takeout.lib.apiLib.login import Login
from takeout.tool.getExcelData import get_excelData2
import json
import allure,os
#1- 封装测试类
class TestLogin:
    # 数据驱动
    #[({},{}),({},{})]
    @pytest.mark.parametrize('inData,respData',get_excelData2('登录模块','Login'))  # parametrize('变量'，值)   #接口里面的数据都是字典
    def test_login(self,inData,respData):
        #1-调用以前封装的模块---Lib

        res = Login().login(json.dumps(inData),getToken=False)    #login参数是要输入json格式,所以要转成json，inData里面也转了下 把login方法的indata变成字符串
        #2-断言 实际结果与预期的结果进行比较
        assert res['msg'] == respData['msg']


if __name__ == '__main__':
    #-s:输出打印信息； -q  简化输出
    #--alluredir =../report/tmp-----生成allure报告需要的源数据
    pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
    #allure generate-----生成报告
    #方案二：allure serve----启服务----自动打开浏览器----一般设置默认浏览器
    os.system('allure serve ../report/tmp')
    #生成报告

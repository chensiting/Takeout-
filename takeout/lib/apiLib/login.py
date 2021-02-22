#-*- coding: utf-8 -*-
#@File : login.py
#@Time : 2021-02-23 1:59
#@Author : chensiting
#@Email : 475707078@qq.com
#@Software: PyCharm


import requests,hashlib,json
from takeout.configs.config import HOST

#需求：输入一个字符串的密码，输出的一个md5加密

def get_md5(password):
    md5 = hashlib.md5()  #实例化对象
    md5.update(password.encode('utf-8'))  #加密操作
    #print(md5.hexdigest())
    return md5.hexdigest()

#print('md5--->',get_md5('80051'))

class Login:
    def login(self,inData,getToken=True): #实例方法
        '''
        :param inData:账号+密码---字典
        :param getToken 为True 获取token; 为False 返回接口响应数据
        :return:
        '''
        url = f'{HOST}/account/sLogin'
        inData = json.loads(inData) #字符串---转化---字典
        inData['password']=get_md5(inData['password'])  #这样写是当成字典处理的
        payload = inData
        resp = requests.post(url,data=payload)
        if getToken:
            return resp.json()['data']['token']
        else:
            return resp.json()
        #print(resp.text)  #返回str
        #print(resp.json()) #返回字典

    #login({'username':'dp0403','password':'80051'})

if __name__ == '__main__':
    print(Login().login('''{"username":"dp0403","password":"80051"}'''))  #这样是传字典的，excel里面都是字符串，所以要将传入的indata转换

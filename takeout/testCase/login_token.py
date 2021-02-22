import requests,hashlib

#需求：输入一个字符串的密码，输出的一个md5加密
HOST = 'http://121.41.14.39:8082'

def get_md5(password):
    md5 = hashlib.md5()  #实例化对象
    md5.update(password.encode('utf-8'))  #加密操作
    #print(md5.hexdigest())
    return md5.hexdigest()

print('md5--->',get_md5('80051'))


def login(inData):
    '''
    :param inData:账号+密码---字典
    :param getToken 为True 获取token; 为False 返回接口响应数据
    :return:
    '''
    url = f'{HOST}/account/sLogin'
    inData['password']=get_md5(inData['password'])
    payload = inData
    res = requests.post(url,data=payload)
    print(res.text)  #返回str
    print(res.json()) #返回字典

login({'username':'dp0403','password':'80051'})
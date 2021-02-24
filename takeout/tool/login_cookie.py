#time:2021-02-22
#我自己写的

#1- 登录接口
import requests
def login(inData):
    url = 'http://120.55.190.222:7080/api/mgr/loginReq'#路径
    payload = inData
    resp = requests.post(url,data=payload)
    #print(resp.text)
    #方案一：原生态cookie----如果后续的接口直接使用这个cookie,不增加其他参数--直接使用
    print(resp.cookies)
    # 方案二：如果后续的接口使用这个cookie,再增加其他参数认证，重新封装cookies
    print(resp.cookies['sessionid'])
    # print(resp.headers)#响应头
    return resp.cookies,resp.cookies['sessionid']

login({'username':'auto','password':'sdfsdfsdf'})


#方案一：
#原生态cookie
#cookie1 = login({'username':'auto','password':'sdfsdfsdf'})[0]
#其他接口请求
#resp = requests.post(url,cookies = cookie1)#

# 方案二：
# session= login({'username':'auto','password':'sdfsdfsdf'})[1]#sessionid值
# user_cookie = {'sessionid':session,'token':'123456'}
# #其他接口请求
# resp = requests.post('路径',cookies = user_cookie)#

#方案一
def addcourse1():
    url ='http://120.55.190.222:7080/api/mgr/sq_mgr/'
    payload={
        'action':'add_course',
        'data':'''{
            "name":"xiaoxue",
            "desc":"kecheng",
            "display_idx":"4"
        }'''
    }
    cookie1 = login({'username':'auto','password':'sdfsdfsdf'})[0]
    res =requests.post(url,data=payload,cookies=cookie1)
    #print(res.json())
    return res.json()

addcourse1()

#方案二
def addcourse2():
    url ='http://120.55.190.222:7080/api/mgr/sq_mgr/'
    payload={
        'action':'add_course',
        'data':'''{
            "name":"xiaoxue1",
            "desc":"kecheng1",
            "display_idx":"4"
        }'''
    }
    session = login({'username':'auto','password':'sdfsdfsdf'})[1]
    user_cookie = {'sessionid': session}
    res =requests.post(url,data=payload,cookies=user_cookie)
    #print(res.json())
    return res.json()
addcourse2()
'''
data--表单数据   name=tom&age=20---  content-type就是 表单
json--json格式   直接传入字典---     content-type就是 json格式
params---参数到url里的
'''

 #https协议
# requests.packages.urllib3.disable_warnings()#忽略警告
# import requests
# def login(inData):
#     url = 'https://120.55.190.222/api/mgr/loginReq'#路径
#     payload = inData
#     resp = requests.post(url,data=payload,verify = False)#
#     print(resp.text)
#
# login({'username':'auto','password':'sdfsdfsdf'})


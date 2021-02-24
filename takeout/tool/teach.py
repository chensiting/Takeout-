import requests
# requests.packages.urllib3.disable_warnings()
import json
#复制老师的代码---不是自己写的

class Login:
    def login(self,inData,flag=False):#登录方法
        url = 'http://120.55.190.222:7080/api/mgr/loginReq'
        #url = 'https://120.55.190.222/api/mgr/loginReq'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        #payload = json.loads(inData)#字符串---变成----字典
        payload = inData  # 字符串---变成----字典
        # reps = requests.post(url, data=payload)#
        reps = requests.post(url, data=payload,verify=False)  #
        if flag == False:#这个登录的接口会作为后续接口的前置条件
            return reps.cookies['sessionid']
        else:#本身这个登录接口需要调用
            return reps.json()

#1- 课程-新增
def lesson_add(inBody,cookie):
    url = 'http://120.55.190.222:7080/api/mgr/sq_mgr/'
    payload = {
                'action':'add_course',
                'data':inBody
    }
    reps = requests.post(url,data=payload,cookies = cookie)
    reps.encoding = 'unicode_escape'#响应编码
    return reps.json()#json格式


if __name__ == '__main__':#   ctrl+j
    #1-获取登录的seesionid
    user_session = Login().login({'username':'auto','password':'sdfsdfsdf'},False)#获取sessionid
    user_cookie = {'sessionid':user_session }#封装cookie
    data= {#data数据接口要求是json格式
        "name": "初中化学",
        "desc": "初中化学课程",
        "display_idx": "4"
    }
    print(lesson_add(json.dumps(data),cookie=user_cookie))#新增课程接口



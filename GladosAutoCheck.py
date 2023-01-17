# -*- coding: UTF-8 -*-

import requests
import config

#签到操作

def headers_handle(KOA_SESS, KOA_SESS_SIG):
    KOA_SESS = "koa:sess=" + KOA_SESS + ";"
    KOA_SESS_SIG = "koa:sess.sig=" + KOA_SESS_SIG
    both = KOA_SESS + KOA_SESS_SIG
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.62",'Cookie': both,
        'Referer': 'https://glados.rocks/login'}
    return headers




url='https://glados.rocks/api/user/checkin'



data = {
    'token':'glados.network',
}
if __name__ == '__main__':
    headers = headers_handle(config.KOA_SESS,config.KOA_SESS_SIG)
    respond = requests.post(url,data=data,headers=headers)
    unicodeResult = respond.content.decode()
    #print(type(unicodeResult))
    translate = unicodeResult.encode('utf-8').decode('utf-8')
    dict = eval(translate)


    #输出状态与剩余天数
    #将字典的每个值转化为列表形式
    list1 = list(dict.values())


    #取下标为1的列表值（签到状态）
    #print(list1[1])
#     if list1[1] == "Checkin! Get 1 Day":
#         message_status = "签到成功，会员天数+1"
#         print(message_status)
#     elif list1[1] == "Please Try Tomorrow":
#         message_status = "今日已签到"
#         print(message_status)
#     else:
#         print(list1[1])
    

    #列表下标为2的值可以当作字典来处理
    str = str(list1[2])
    #先把方括号去掉
    str = str.replace('[','')
    str = str.replace(']','')
    #print(str)

    #截取第一个花括号在中间的字符串，得到一个json
    cut = str[:str.index('}')+1]
    #print(cut)
    print('-'*10)

    #print(type(cut))

    #将json字符串转换为字典
    dict2 = eval(cut)
    #print(type(list2))

    #将字典的每个值转化为列表形式
    list2 = list(dict2.values())
    #取下标为6的值（会员天数）
    message_days = "会员天数还剩"+list2[6]
    print(message_days)
    
    # plusplus推送
    requests.get('http://www.pushplus.plus/send?token=' + config.SCKEY + '&title='+list1[1]+'&content=剩余'+int(list2[6])+'天')





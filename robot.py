'''
微信自动回复机器人，使用图灵机器人接口。
'''
from itchat.content import *
import requests
import json
import itchat
import re
import  numpy
itchat.auto_login(hotReload = True,enableCmdQR=True)

def tuling(info):
    apikey = "4c5fd36a056a4f38865caf2b4240a3ae"
    api = "http://www.tuling123.com/openapi/api"
    data={
        'key':apikey,
        'info':info,
        'userid':'wechat'
    }
    try:
        req = requests.post(api,data=data).json()
        answer = req['text']
        return answer
    except:
        return

def group_id(name):
    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']


default_reply='您好！信息已收到！--机器人自动回复。'
xiaohao=itchat.search_friends(nickName='robot')
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
    if msg['FromUserName']==xiaohao[0]['UserName'] and msg['Text']=='quit':
        itchat.logout()
        return
    if '(ノ°ο°)ノ' in msg['Text']:
        reply=tuling(msg['Text'])or default_reply
        itchat.send('%s--机器人自动回复。' % reply,msg['FromUserName'])
# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg['Text'](msg['FileName'])
#     return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


black_list=['乳','奶','van','肚','傻']
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING], isGroupChat=True)
def group_text_reply(msg):

    # with open('msg.txt','ab')as f:
    #     f.write(str(msg).encode('utf-8'))
    vg = group_id('VG')
    houyuanhui=group_id('红姐全球后援会')
    xiangqinxiangaiyijiaren=group_id('相亲相爱一家人')
    yijiaren=group_id('一家人')
    xiaoerban=group_id('小2班')
    if (msg['FromUserName'] == vg): #and msg['IsAt']==True) :

        sender_actualname=msg['ActualUserName']
        users=str(msg['User'])
        pattern1=re.compile("'UserName': \'%s\', 'NickName': '(.*?)',"%sender_actualname)
        pattern2=re.compile("'UserName': \'%s\', 'NickName': '(.*?)',"%msg['FromUserName'])
        reply=tuling(msg['Text'])or default_reply
        sender_nickname=pattern1.findall(users)
        reciver_nickname=pattern2.findall(users)

        # if sender_nickname=='姚舜禹':
        #     h=[]
        #     for b in black_list:
        #         r=str(msg['Text']).find(b)
        #         if r!=-1:
        #             h.append(True)
        #     if numpy.any(h):
        #         itchat.send(u'就是姚大傻啊。姚大傻爱吃屎。' , msg['FromUserName'])
        #     else:
        #         itchat.send(u'%s。' % reply, msg['FromUserName'])
        # else:
        #     h=[]
        for b in black_list:
            r=str(msg['Text']).find(b)
            if r!=-1:
                h.append(True)
            if numpy.any(h):
                itchat.send(u'就是姚大傻啊。姚大傻爱吃屎。' , msg['FromUserName'])
            else:
                if(msg['IsAt']==True):
                    itchat.send(u'%s' % reply, msg['FromUserName'])
    elif msg['FromUserName'] == houyuanhui and msg['IsAt']==True:
        reply=tuling(msg['Text'])or default_reply
        itchat.send(u'%s--图灵机器人' % reply, msg['FromUserName'])
    elif msg['FromUserName'] ==xiangqinxiangaiyijiaren or msg['FromUserName'] ==yijiaren:
        reply=tuling(msg['Text'])or default_reply
        itchat.send(u'%s--图灵机器人自动回复' % reply, msg['FromUserName'])
    elif msg['FromUserName'] == xiaoerban and msg['IsAt']==True:
        reply=tuling(msg['Text'])or default_reply
        itchat.send(u'%s--图灵机器人' % reply, msg['FromUserName'])

itchat.run()

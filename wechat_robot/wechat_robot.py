import itchat
from itchat.content import *
import requests
import json
import os
from PIL import Image, ImageDraw
import face_recognition
import os
from translate import translator_zh_to_en
from translate import translator_en_to_zh
import langid



key = "5a82c4c4d895415ea2f31ae8d8d26a86"



def judge_pure_english(str):  
    return str.encode('UTF-8').isalpha()


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key' : key,
        'info' : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl,data).json()
        return r       

    except:
        #return "sorry, I don't understand clear, I beg your pardon."
        return None    


@itchat.msg_register(TEXT)
def send_content(msg):
    zh_content = translator_en_to_zh(msg['Text']) 
    zh_reply = get_response(zh_content)
    eg_reply = translator_zh_to_en(zh_reply['text'])
    itchat.send(eg_reply,msg['FromUserName'])

    """
    reply = get_response(msg['Text'])
    
    if reply["code"] == 100000:
        #itchat.send(reply["text"],msg['FromUserName'])
        pass
    
    elif reply["code"] == 200000:
        print(reply["text"])
        itchat.send(reply["text"],msg['FromUserName'])
        print(reply["url"])
        itchat.send(reply["url"],msg['FromUserName'])

    elif reply["code"] == 302000:
        itchat.send_msg('Here is the news：\n',msg['FromUserName'])
        result = ""
        for item_dict in reply["list"]:
            for key_value, information in item_dict.items():
                print(item_dict[key_value])
                itchat.send(item_dict[key_value],msg['FromUserName'])
    
    elif reply["code"] == 308000:
        itchat.send_msg('here is the cookbooks: \n',msg['FromUserName'])
        for item_dict in reply["list"]:
            for key_value, information in item_dict.items():
                print(item_dict[key_value])
                itchat.send(item_dict[key_value],msg['FromUserName'])
    else:
        print(default_message)
        itchat.send(default_message,msg['FromUserName'])
    """             
                    
@itchat.msg_register(PICTURE)
def reply_image_content(msg):
    msg['Text'](msg['FileName'])
    os.system("python3 mark_up.py {}".format(msg['FileName']))
    itchat.send_image("output.png",msg['FromUserName'])


@itchat.msg_register([RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    os.system("python2 pdf2text.py {}".format(msg['FileName']))
    itchat.send_file("output.txt",msg['FromUserName'])



# 收到好友邀请自动添加好友
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

itchat.auto_login(hotReload=True)
itchat.run()   
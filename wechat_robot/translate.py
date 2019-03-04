#/usr/bin/env python
#coding=utf8
import http.client
import hashlib
import urllib
import random
import json
import urllib.request as urllib2



def translator_zh_to_en(content):
    appid = "20181203000242619"
    secretKey = "Vl3hRQQ1iUyMsdqx9XAN"
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=zh'  + '&to=en' +'&salt=' + str(
        salt) + '&sign=' + sign
 
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")
        js = json.loads(jsonResponse) 
        dst = str(js["trans_result"][0]["dst"])
        return dst
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()


def translator_en_to_zh(q):
    appid = '20181203000242619' #你的appid
    secretKey = 'Vl3hRQQ1iUyMsdqx9XAN' #你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey

    #m1.update(sign)
    m1 = hashlib.md5(bytes(sign,"ascii"))
    
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
     
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
     
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        res = json.load(response)
        return res['trans_result'][0]['dst']

    except Exception as e:
        return e
    finally:
        if httpClient:
            httpClient.close()


if __name__ == '__main__':
    #q = "Game of Thrones is roughly based on the storylines of A Song of Ice and Fire"
    res = translator_zh_to_en( "你好吗")
    

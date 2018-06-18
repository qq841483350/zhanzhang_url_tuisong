#coding:utf8
#百度url主动实时推送百度索引，urls里一行一个URL
import requests,time
def tuisong():
        url = "http://data.zz.baidu.com/urls?site=domain&token=token"%(domain,token)  #接口调用地址 在站长平台获取

        filecontents = {'file': open('urls.txt', 'r')}  #urls.txt为需要推送的URL文件，每行一个
        r=requests.post(url, files=filecontents)
        baiduresult =u"推送成功，结果为:%s \n" %(r.text)
        print baiduresult

if __name__=="__main__":
    domain="www.xiaoshiseo.com"
    token="kdjdld"
    tuisong()


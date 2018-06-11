#coding:utf8
#python编写的熊掌号资源批量提交工具
import requests,time
def xiongzhang():
    url="http://data.zz.baidu.com/urls?appid=%s&token=%s&type=%s"%(appid,token,type)  #接口调用地址 熊掌号-资讯提交页面获取
    filecontents={'file':open('urls.txt','r')}  #urls.txt里是需要推送的URL文件，每行一个
    r=requests.post(url,files=filecontents)
    result=u'\n推送成功,结果为:%s\n'%r.text.decode('utf8')
    print result

if __name__=="__main__":
    appid="xxx"  #在站长平台后台获取appid 	是 	stringo类型 	您的熊掌号唯一识别ID
    token="xxx"  #在搜索资源平台申请的推送用的准入密钥
    type="realtime" #对提交内容的数据类型说明，新增内容参数：realtime
    xiongzhang()
    # raw_input()

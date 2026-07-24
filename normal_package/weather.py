# -*- code=utf-8 -*-

import urllib.request
import requests

URL = r"https://qq.ip138.com/weather/search.asp"

header = {
    'User-Agent':r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    'Referer':r"https://qq.ip138.com/weather/search.asp",
    'Connection':'keep-alive'
}

#提交的数据编码
data = urllib.parse.urlencode({
    'k':'清远',
    'Submit':"提交"
}).encode('utf-8')

#生成请求头对象
request = urllib.request.Request(URL, headers=header, data=data)
response = urllib.request.urlopen(request)
#print(response.read().decode('utf-8'))


#### 使用request 进行处理

response_two = requests.request("post",URL,headers=header,data=data)
print(response_two.status_code)
print(response_two.text) #网页源码
print(response_two.content) #网页源码
print(response_two.cookies) #cookies
print(response_two.headers) #请求头

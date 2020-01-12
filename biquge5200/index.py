import requests
import re

response = requests.get("https://mp.weixin.qq.com/s/8zuPeQnyAHOGHkkBVulezA");
# response.encoding = 'gbk'

# print(response.status_code)
# print(type(response.text))
# print(response.text)

# print(type(response.content))
# print(response.content)
# print(response.content.decode('utf-8'))

result = response.text

title = re.findall(r'<title>(.*?)</title>',result)
text = re.findall(r'<div id="content">([\s\S]*?])</div>',result)
print(title)
# print(text)

data = {"name":"Toby","password":"123456"}
response = requests.post("http://httpbin.org/post",data=data)

# print(response.text)


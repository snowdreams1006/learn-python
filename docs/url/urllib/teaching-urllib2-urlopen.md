# urllib2 的 urlopen 网页下载器

urllib2 下载网页方法

## 最简洁方法

> urllib2.urlopen(url)

```python
import urllib2

# 直接请求
response = urllib2.urlopen('http://www.baidu.com')
# 获取状态码,如果是 200 表示获取成功
print response.getcode()
# 获取内容
print response.read()
```

## 高级用法

> urllib2.Request

```python
import urllib2

# 创建 Request 对象
request = urllib2.Request(url)
# 添加请求数据
request.add_data('param1','param1')
# 添加请求头
request.add_header('User-Agent','Mozilla/5.0')

# 直接请求
response = urllib2.urlopen(request)
# 获取状态码,如果是 200 表示获取成功
print response.getcode()
# 获取内容
print response.read()
```

## 特殊情景处理器

> HTTPCookieProcessor ProxyHandler HTTPSHandler HTTPRedurectHandler
> opener = urllib2.build_opener(handler)
> urllib2.install_opener(opener)
> urllib2.urlopen(url) urllib2.urlopen(request)

```python
import urllib2,cookielib

# 创建 cookie 容器
cj = cookielib.CookieJar()
# 创建支持 cookie 的 opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# 给 urllib2 安装 opener
urllib2.install_opener(opener)

# 使用带有 cookie 的 urllib2 访问网页
response = urllib2.urlopen('http://www.baidu.com')
```

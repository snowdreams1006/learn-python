# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import json

def get_simple_urlopen_with_urllib2():
    '''
    最简单 GET 请求
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Status Code:')
    print(response.getcode())
    print('>>>Response Body:')
    print(response.read())

def get_params_urlopen_with_urllib2():
    '''
    带参数 GET 请求
    '''
    params = urllib.urlencode({
        'param1': 'hello', 
        'param2': 'world',
        'author':'snowdreams1006',
        'website':'http://blog.snowdreams1006.cn',
        'url':'https://snowdreams1006.github.io/learn-python/url/urllib/teaching.html',
        'wechat':'snowdreams1006',
        'email':'snowdreams1006@163.com',
        'github':'https://github.com/snowdreams1006/'
    })
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get?%s' % params)
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Status Code:')
    print(response.getcode())
    print('>>>Response Body:')
    print(response.read())

def post_params_urlopen_with_urllib2():
    '''
    带参数 POST 请求访问
    '''
    data = urllib.urlencode({
        'param1': 'hello', 
        'param2': 'world',
        'author':'snowdreams1006',
        'website':'http://blog.snowdreams1006.cn',
        'url':'https://snowdreams1006.github.io/learn-python/url/urllib/teaching.html',
        'wechat':'snowdreams1006',
        'email':'snowdreams1006@163.com',
        'github':'https://github.com/snowdreams1006/'
    })
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/post',data)
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Status Code:')
    print(response.getcode())
    print('>>>Response Body:')
    print(response.read())

def get_proxy():
    '''
    获取随机代理
    '''
    response = urllib2.urlopen('http://proxyip.snowdreams1006.cn/get/')
    result = response.read()
    return json.loads(result)

def get_proxy_urlopen_with_urllib():
    '''
    设置代理 GET 请求
    '''
    ip = get_proxy().get('proxy')
    print('>>>Get Proxy:')
    print(ip)
    proxies = {
        'http': 'http://{}'.format(ip),
        'https': 'https://{}'.format(ip)
    }
    response = urllib.urlopen('http://httpbin.snowdreams1006.cn/ip',proxies=proxies)
    result = response.read()
    result = json.loads(result)
    response_ip = result.get('origin')
    proxy_ip = ip.split(':')[0]
    if proxy_ip == response_ip:
        print 'Proxy Success'
    else:
        print 'Proxy Fail'

def post_proxy_urlopen_with_urllib():
    '''
    设置代理 POST 请求
    '''
    ip = get_proxy().get('proxy')
    print('>>>Get Proxy:')
    print(ip)
    proxies = {
        'http': 'http://{}'.format(ip),
        'https': 'https://{}'.format(ip)
    }
    data = urllib.urlencode({
        'param1': 'hello', 
        'param2': 'world',
        'author':'snowdreams1006',
        'website':'http://blog.snowdreams1006.cn',
        'url':'https://snowdreams1006.github.io/learn-python/url/urllib/teaching.html',
        'wechat':'snowdreams1006',
        'email':'snowdreams1006@163.com',
        'github':'https://github.com/snowdreams1006/'
    })
    response = urllib.urlopen('http://httpbin.snowdreams1006.cn/ip',data=data,proxies=proxies)
    result = response.read()
    result = json.loads(result)
    response_ip = result.get('origin')
    proxy_ip = ip.split(':')[0]
    if proxy_ip == response_ip:
        print 'Proxy Success'
    else:
        print 'Proxy Fail'

def send_request_header_with_urllib2():
    '''
    自定义请求头
    '''
    request = urllib2.Request('http://httpbin.snowdreams1006.cn/headers')
    request.add_header('user-agent','Mozilla/5.0')
    response = urllib2.urlopen(request)
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Status Code:')
    print(response.getcode())
    print('>>>Response Body:')
    print(response.read())

def send_request_cookie_with_urllib2():
    '''
    自定义请求头
    '''
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://www.baidu.com')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Status Code:')
    print(response.getcode())
    print('>>>Response Body:')
    print(response.read())
    print(cj)


if __name__ == '__main__':
    send_request_cookie_with_urllib2()

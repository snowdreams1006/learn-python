# -*- coding: utf-8 -*-
import urllib
import urllib2

def urlencode_and_unquote_demo():
    encode_params = urllib.urlencode({
        'param1': 'hello', 
        'param2': 'world',
        'author':'snowdreams1006',
        'website':'http://blog.snowdreams1006.cn',
        'url':'https://snowdreams1006.github.io/learn-python/url/urllib/teaching.html',
        'wechat':'snowdreams1006',
        'email':'snowdreams1006@163.com',
        'github':'https://github.com/snowdreams1006/'
    })
    print '>>>urllib.urlencode<<<'
    print encode_params
    unquote_param =  urllib.unquote(encode_params)
    print '>>>urllib.unquote<<<'
    print unquote_param

def urlopen_without_params_demo():
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print '>>>response.info<<<'
    print response.info()
    print '>>>response.info<<<'
    print response.getcode()
    print '>>>response.read<<<'
    print response.read()

def urlopen_with_params_demo():
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
    print '>>>response.info<<<'
    print response.info()
    print '>>>response.info<<<'
    print response.getcode()
    print '>>>response.read<<<'
    print response.read()


def main():
    urlopen_without_params_demo()

if __name__ == '__main__':
    main()
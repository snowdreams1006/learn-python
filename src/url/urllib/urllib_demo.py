# -*- coding: utf-8 -*-
import urllib
import urllib2

def use_simple_urllib2():
    '''
    获取响应头和响应体信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read())

def use_params_urllib2():
    '''
    获取请求方信息
    '''
    params = urllib.urlencode({'param1': 'hello', 'param2': 'world'})
    response = urllib2.urlopen('?'.join(['http://httpbin.snowdreams1006.cn/get', '%s']) % params)
    print('>>>Response Headers:')
    print(response.info())
    print('>>>>Response Status Code:')
    print(response.getcode())
    print('>>>Response body:')
    print(''.join([line for line in response.readlines()]))

if __name__ == '__main__':
    print '>>>Use simple urllib2<<<'
    use_simple_urllib2()

    print '>>>Use params urllib2<<<'
    # use_params_urllib2()

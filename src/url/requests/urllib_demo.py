# -*- coding: utf-8 -*-
import urllib
import urllib2

def use_simple_urllib2_get_ip():
    '''
    获取请求方 ip
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/ip')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(''.join([line for line in response.readlines()]))

def use_simple_urllib2_get_user_agent():
    '''
    获取请求方 user-agent
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/user-agent')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(''.join([line for line in response.readlines()]))

def use_simple_urllib2_get_headers():
    '''
    获取请求方 headers
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/headers')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(''.join([line for line in response.readlines()]))


if __name__ == '__main__':
    # print '>>>Use simple urllib2:'
    # use_simple_urllib2()
    # print '>>>Use simple urllib2 to get ip:'
    # use_simple_urllib2_get_ip()
    # print('>>>Use simple1 urllib2 to get user-agent:')
    # use_simple_urllib2_get_user_agent()
    # print '>>>Use simple urllib2 to get headers:'
    # use_simple_urllib2_get_headers()

    print ''
    print '>>>Use params urllib2:'
    # use_params_urllib2()
    print '>>>Use params urllib2 to get response headers:'
    use_params_urllib2_response_headers()

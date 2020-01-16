# -*- coding: utf-8 -*-
import urllib
import urllib2

def use_simple_urllib2():
    '''
    获取请求方信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    # print type(response)
    # print dir(response)
    # print response.headers.dict
    # print response.info()
    # print response.readline()


    # print type(response.next)
    # print response.next
    # print response.next()
    # while response.next():
    #     print response.readline()
    # print response.readline()
    # print response.readline()
    # print response.readline()

    # for line in response: 
    #     print line.readline()

    # result = response.read()
    # print result

    # response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    # result = ''
    # line = response.readline()
    # result = result + str(line)
    # while line:
    #     line = response.readline()
    #     result = result + str(line)
    # print result

    # result = ''
    # for line in response.readlines():
    #     result = result + str(line)
    # print result

    result = ''.join([line for line in response.readlines()])
    print result


    # print(''.join([line for line in response.readlines()]))

    # for line in response.readlines():
    #     print line



    # # print response.read()
    # print type(response.getcode)
    # print response.msg

    # response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/status/200')
    # print response.code
    # print response.msg

    # response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/status/500')
    # print response.code
    # print response.msg



    # print('>>>Response Headers:')
    # print(response.info())
    # print('>>>Response Body:')
    # print(''.join([line for line in response.readlines()]))

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
    print '>>>Use simple urllib2:'
    use_simple_urllib2()

    print '>>>Use params urllib2:'
    # use_params_urllib2()

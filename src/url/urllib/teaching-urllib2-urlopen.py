# -*- coding: utf-8 -*-
import urllib
import urllib2
import json

def use_simple_urlopen_with_urllib2():
    '''
    最简单 GET 请求访问
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Status Code:')
    print(response.getcode())
    print('>>>Response Body:')
    print(response.read())

def use_params_urlopen_with_urllib2():
    '''
    带参数 POST 请求访问
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
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/post',params)
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

def get_proxy_urllib():
    '''
    通过代理发送请求
    '''
    # 随机代理 ip
    ip = get_proxy().get('proxy')
    print('>>>Get Proxy:')
    print(ip)
    proxy = {
        'http': 'http://{}'.format(ip),
        'https': 'https://{}'.format(ip)
    }
    opener = urllib.FancyURLopener(proxy)
    response = opener.open("http://httpbin.snowdreams1006.cn/ip")
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    result = response.read()
    print(result)
    result = json.loads(result)
    response_ip = result.get('origin')
    proxy_ip = ip.split(':')[0]
    if proxy_ip == response_ip:
        print 'Set proxy success'
    else:
        print 'Set proxy fail'

def clear_proxy_urllib():
    '''
    清除代理后发送请求
    '''
    # 随机代理 ip
    ip = get_proxy().get('proxy')
    print('>>>Get Proxy:')
    print(ip)
    proxy = {
        'http': 'http://{}'.format(ip),
        'https': 'https://{}'.format(ip)
    }
    opener = urllib.FancyURLopener(proxy)
    response = opener.open("http://httpbin.snowdreams1006.cn/ip")
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    result = response.read()
    print(result)
    result = json.loads(result)
    response_ip = result.get('origin')
    proxy_ip = ip.split(':')[0]
    if proxy_ip == response_ip:
        print 'Set proxy success'
    else:
        print 'Set proxy fail'

    opener = urllib.FancyURLopener({})
    response = opener.open("http://httpbin.snowdreams1006.cn/ip")
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    result = response.read()
    print(result)
    result = json.loads(result)
    response_ip = result.get('origin')
    proxy_ip = ip.split(':')[0]
    if proxy_ip == response_ip:
        print 'Clear proxy fail'
    else:
        print 'Clear proxy success'

def send_proxy_urllib():
    '''
    通过代理获取响应头和响应体信息
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

if __name__ == '__main__':
    # print '>>>Get simple urllib2<<<'
    # use_simple_urlopen_with_urllib2()

    print '>>>Post params urllib2<<<'
    use_params_urlopen_with_urllib2()

    # print '>>>Post params urllib2<<<'
    # post_params_urllib2()

    # print '>>>Get proxy urllib<<<'
    # get_proxy_urllib()

    # print '>>>Clear proxy urllib<<<'
    # clear_proxy_urllib()

    # print '>>>Send proxy urllib<<<'
    # send_proxy_urllib()

    # print '>>>Lists all the emojis available to use on GitHub.<<<'
    # get_github_emojis_urllib2()

    # print '>>>List public events<<<'
    # list_github_public_events_urllib2()

    # print '>>List repository events<<<'
    # list_github_repository_events_urllib2()

    # print '>>>List issue events for a repositorys<<<'
    # list_github_repository_issue_events_urllib2()

    # print '>>>List public events for a network of repositories<<<'
    # list_github_repository_networks_events_urllib2()

    # print '>>>List public events for an organization<<<'
    # list_github_organization_events_urllib2()

    # print '>>>List events that a user has received<<<'
    # list_github_received_events_urllib2()

    # print '>>>List public events that a user has received<<<'
    # list_github_public_received_events_urllib2()
    
    # print '>>>List events performed by a user<<<'
    # list_github_performed_events_urllib2()

    # print '>>>List public events performed by a user<<<'
    # list_github_public_performed_events_urllib2()

    # print '>>>List events for an organization<<<'
    # list_github_user_organization_events_urllib2()

    # print '>>>List feeds<<<'
    # list_github_feeds_urllib2()

    # print '>>>List a user gists<<<'
    # list_github_user_gists_urllib2()

    # print '>>>List a user gists<<<'
    # list_github_gists_urllib2()

    # print '>>>List all public gists<<<'
    # list_github_public_gists_urllib2()

    # print '>>>List starred gists<<<'
    # list_github_starred_gists_urllib2()

    # print '>>>Get a single gist<<<'
    # get_github_single_gists_urllib2()

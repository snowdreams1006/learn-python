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

def urlretrieve_without_filename_demo():
    response = urllib.urlretrieve('http://httpbin.snowdreams1006.cn/image/jpeg')
    temp_filename = response[0]
    with open(temp_filename,'rb') as rbf:
        with open('./images/urlretrieve_without_filename_demo.jpeg','wb') as wbf:
            wbf.write(rbf.read())

def urlretrieve_with_filename_demo():
    urllib.urlretrieve('http://httpbin.snowdreams1006.cn/image/png',filename='./images/urlretrieve_with_filename_demo.png')

def urlretrieve_with_reporthook_demo():
    def reporthook(blocknum, blocksize, totalsize):  
        '''回调函数 
        @blocknum: 已经下载的数据块数目
        @blocksize: 每个数据块的大小(单位:字节byte)
        @totalsize: 远程文件总大小(单位:字节byte)
        '''
        percent = 100.0 * blocknum * blocksize / totalsize
        if percent > 100:
            percent = 100
        print "正在下载 %.2f%%"% percent

    urllib.urlretrieve('http://httpbin.snowdreams1006.cn/image/svg',filename='./images/urlretrieve_with_reporthook_demo.svg',reporthook=reporthook)

def urlcleanup_after_urlretrieve_demo():
    for i in range(3):
        urllib.urlretrieve('http://httpbin.snowdreams1006.cn/image/png',filename='./images/urlcleanup_after_urlretrieve_demo(%d).png' % i)
        urllib.urlcleanup()

def quote_and_unquote_demo():
    url = 'http://httpbin.snowdreams1006.cn/get'
    print '>>>urllib.quote<<<'
    quote_url = urllib.quote(url)
    print quote_url
    unquote_url =  urllib.unquote(quote_url)
    print '>>>urllib.unquote<<<'
    print unquote_url

def quote_plus_and_unquote_plus_demo():
    url = 'http://httpbin.snowdreams1006.cn/get'
    print '>>>urllib.quote_plus<<<'
    quote_plus_url = urllib.quote_plus(url)
    print quote_plus_url
    unquote_plus_url =  urllib.unquote_plus(quote_plus_url)
    print '>>>urllib.unquote_plus<<<'
    print quote_plus_url

def pathname2url_and_url2pathname_demo():
    url = '/Users/snowdreams1006/Documents/workspace/snowdreams1006.github.io/python/src/url/urllib'
    print '>>>urllib.pathname2url<<<'
    pathname2url_url = urllib.pathname2url(url)
    print pathname2url_url
    url2pathname_url =  urllib.url2pathname(pathname2url_url)
    print '>>>urllib.url2pathname<<<'
    print url2pathname_url

def main():
    pathname2url_and_url2pathname_demo()

if __name__ == '__main__':
    main()
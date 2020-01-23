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

def main():
    urlretrieve_with_reporthook_demo()

if __name__ == '__main__':
    main()
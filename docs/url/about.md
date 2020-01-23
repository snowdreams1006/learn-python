# 网络请求

## urllib.urlencode() 和 urllib.unquote()

```python
# -*- coding: utf-8 -*-
import urllib

def urlencode_and_unquote_demo():
    encode_params = urllib.urlencode({
        'param1': 'hello', 
        'param2': 'world',
        'author':'snowdreams1006',
        'website':'http://blog.snowdreams1006.cn',
        'url':'https://snowdreams1006.github.io/learn-python/url/urllib/about.html',
        'wechat':'snowdreams1006',
        'email':'snowdreams1006@163.com',
        'github':'https://github.com/snowdreams1006/'
    })
    print '>>>urllib.urlencode<<<'
    print encode_params
    unquote_param =  urllib.unquote(encode_params)
    print '>>>urllib.unquote<<<'
    print unquote_param

def main():
    urlencode_and_unquote_demo()

if __name__ == '__main__':
    main()
```

## urllib2.urlopen(url[,data[,proxies]])

```python
# -*- coding: utf-8 -*-
import urllib
import urllib2

def urlopen_without_params_demo():
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
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
```

## urllib.urlretrieve(url[,filename[,reporthook[,data]]])

```python
# -*- coding: utf-8 -*-
import urllib

def urlretrieve_with_filename_demo():
    urllib.urlretrieve('http://httpbin.snowdreams1006.cn/image/png',filename='./images/urlretrieve_with_filename_demo.png')

def main():
    urlretrieve_with_filename_demo()

if __name__ == '__main__':
    main()
```

## urllib.urlcleanup()

```python
# -*- coding: utf-8 -*-
import urllib

def urlcleanup_after_urlretrieve_demo():
    for i in range(3):
        urllib.urlretrieve('http://httpbin.snowdreams1006.cn/image/png',filename='./images/urlcleanup_after_urlretrieve_demo(%d).png' % i)
        urllib.urlcleanup()

def main():
    urlcleanup_after_urlretrieve_demo()

if __name__ == '__main__':
    main()
```

## urllib.quote(string[, safe]) 和 urllib.unquote(string)

```python
# -*- coding: utf-8 -*-
import urllib

def quote_and_unquote_demo():
    url = 'http://httpbin.snowdreams1006.cn/get'
    print '>>>urllib.quote<<<'
    quote_url = urllib.quote(url)
    print quote_url
    unquote_url =  urllib.unquote(quote_url)
    print '>>>urllib.unquote<<<'
    print unquote_url

def main():
    urlcleanup_after_urlretrieve_demo()

if __name__ == '__main__':
    main()
```

## urllib.quote_plus(string[, safe]) 和 urllib.unquote_plus(string)

```python
# -*- coding: utf-8 -*-
import urllib

def quote_plus_and_unquote_plus_demo():
    url = 'http://httpbin.snowdreams1006.cn/get'
    print '>>>urllib.quote_plus<<<'
    quote_plus_url = urllib.quote_plus(url)
    print quote_plus_url
    unquote_plus_url =  urllib.unquote_plus(quote_plus_url)
    print '>>>urllib.unquote_plus<<<'
    print quote_plus_url

def main():
    quote_plus_and_unquote_plus_demo()

if __name__ == '__main__':
    main()
```

## urllib.pathname2url(path) 和 urllib.url2pathname(path)

```python
# -*- coding: utf-8 -*-
import urllib

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
```

## 参考文档

- [python之文件下载 （urllib模块urlretrieve方法）](https://www.cnblogs.com/wanghuixi/p/12116005.html)

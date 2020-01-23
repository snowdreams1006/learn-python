# 网络请求

## urllib.urlencode() VS urllib.unquote()

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

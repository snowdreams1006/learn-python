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


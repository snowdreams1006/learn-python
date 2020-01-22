# 实例练习之一键爬取 github 全部表情

> 接口地址: [https://api.github.com/emojis](https://api.github.com/emojis),文档地址: [https://developer.github.com/v3/emojis/](https://developer.github.com/v3/emojis/)

## python

```python
# -*- coding: utf-8 -*-
import urllib2

def get_github_emojis_urllib2():
    '''
    Lists all the emojis available to use on GitHub.
    '''
    response = urllib2.urlopen('https://api.github.com/emojis')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read())

if __name__ == '__main__':
    print '>>>Lists all the emojis available to use on GitHub.<<<'
    get_github_emojis_urllib2()
```

## reference

- [Python核心模块——urllib模块](https://www.cnblogs.com/sysu-blackbear/p/3629420.html)
- [Python 如何将字符串转为字典](https://www.cnblogs.com/OnlyDreams/p/7850920.html)
- [python实现图片拼接](https://blog.csdn.net/tellsummer/article/details/80815411)
- [使用python将多张图片拼接成大图](https://blog.csdn.net/beyond9305/article/details/83413009)
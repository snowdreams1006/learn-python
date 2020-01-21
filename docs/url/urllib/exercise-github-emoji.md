# 实例练习之一键爬取 github 全部表情

> 接口地址: [https://api.github.com/emojis](https://api.github.com/emojis),文档地址: [https://developer.github.com/v3/emojis/](https://developer.github.com/v3/emojis/)


https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8



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

- [Python 如何将字符串转为字典](https://www.cnblogs.com/OnlyDreams/p/7850920.html)
- [https://github.com/tenntenn/gopher-stickers](https://github.com/tenntenn/gopher-stickers)
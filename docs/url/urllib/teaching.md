# 范例教学

## 环境准备

演示环境版本信息如下:

```bash
(.env)$ python --version
Python 2.7.16
(.env) $ pip --version
pip 19.3.1 from ~/python/src/url/urllib/.env/lib/python2.7/site-packages/pip (python 2.7)
```

> 以下代码在该环境运行正常,不保证其他环境与演示结果一致,一切以实际运行结果为准.

- 步骤1. [可选] 安装虚拟环境 `virtualenv` 

```bash
sudo pip install virtualenv
```

> 安装虚拟环境方便隔离不同 python 环境,也可以使用系统默认环境,所以这一步是可选的.


- 步骤2. [可选] 准备虚拟环境目录 `.env`

```bash
virtualenv .env
```

> 如果已安装虚拟环境 `virtualenv`,需要运行该命令,否则请忽略.

- 步骤3. [可选] 激活虚拟环境 `.env`

```bash
source .env/bin/activate
```

> 如果已安装虚拟环境 `virtualenv`,需要运行该命令,否则请忽略.

- 步骤4. [可选] 查看当前正在使用的 `python` 与 `pip` 版本

```bash
(.env) $ which python
~/python/src/url/urllib/.env/bin/python
(.env) snowdreams1006s-MacBook-Pro:urllib snowdreams1006$ which pip
~/python/src/url/urllib/.env/bin/pip
```

> 演示环境已开启虚拟环境,因此 `python` 和 `pip` 文件位置正是当前目录 `.env` 而不是系统默认环境,如果未开启虚拟环境则显示的是系统目录.

## 认识原生请求 urllib

如果读者亲测运行时发现网络无法正常请求,可以将[http://httpbin.snowdreams1006.cn/](http://httpbin.snowdreams1006.cn/)替换成[http://httpbin.org/](http://httpbin.org/)或者自行搭建本地测试环境.

下面提供两种搭建本地测试环境的安装方式,当然也可以访问[http://httpbin.snowdreams1006.cn/](http://httpbin.snowdreams1006.cn/)或者[http://httpbin.org/](http://httpbin.org/)在线环境.

- `docker` 安装方式

```bash
docker run -p 8000:80 kennethreitz/httpbin
```

> 首次运行会先将镜像下载到本地再启动容器,非首次运行会直接启动容器,访问地址: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

- `python` 安装方式

```bash
pip install gunicorn httpbin && gunicorn httpbin:app
```

> 默认监听端口是 `8000`,如果遇到端口冲突提示已被占用,可运行 `gunicorn httpbin:app -b :9898` 指定端口.

### 怎么发送最简单的网络请求

> `urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')`

新建 `python` 文件名为 `urllib_demo.py`,代码主要是先导入 `urllib2` 包后,然后使用 `urllib2.urlopen()` 即可发送最简单的 `GET` 请求,最后利用 `response.read()` 可一次性读取响应体内容.

详情代码如下:

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取请求方信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print response.read()

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

> 假如该文件名为 `urllib_demo.py` ,则在终端命令行内运行 `python urllib_demo.py` 即可查看输出结果.

### 怎么知道响应对象有哪些属性和方法

> `print type(response)` : 获取对象类型,配合基本类型可大致猜测出有哪些方法和属性可供外部调用.
> `print dir(response)` : 获取对象方法和属性枚举值,无文档猜测方法和属性.

无论是 `GET` 请求还是 `POST` 请求,获取请求后的响应体无疑是非常重要的,但实际开发中同样不可忽略的是其他方法和属性.

因此,除了掌握 `response.read()` 一次性全部读取响应体内容之外,还需要知道 `response` 有哪些属性和方法.

通过 `type(response)` 获取对象类型再配合 `dir(response)` 获取属性枚举值即可无文档大致猜测对象有哪些可供调用的属性和方法.

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取请求方信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print type(response)
    print dir(response)

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

> 假如该文件名为 `urllib_demo.py` ,则在终端命令行内运行 `python urllib_demo.py` 即可查看输出结果.

- 响应对象的状态码(属性)

> `response.code` : 获取响应对象的状态码,正常情况下是 `200` 表示请求成功,而 `500` 是典型的系统错误.

通过 `dir(response)` 获取属性枚举值,结合 `type(response)` 不难发现 `response.code` 是用来获取响应状态码的,具体调用方式是 `response.code` 还是 `response.code()` 可运行 `print type(response.code)` 大致推断.

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取请求方信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print type(response.read)
    print type(response.code)

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

> 这里不妨结合 `print type(response.read)` 是方法来验证输出结果到底是属性还是方法,可以看出 `response.read` 是 `<type 'instancemethod'>` 方法类型,而 `response.code` 是 `<type 'int'>` 基本类型,因此 `response.code` 是属性调用方式.

`type(response.code)` 的输出结果是 `<type 'int'>` 并不是 `<type 'instancemethod'>`,因此获取状态码的方式是属性调用.

详细代码如下:

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取请求方信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print response.code

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

- 响应对象的状态码(方法)

> `response.getcode()` : 获取响应对象的状态码,正常情况下是 `200` 表示请求成功,而 `500` 是典型的系统错误.

同样地,从 `print dir(response)` 可知 `getcode` 字段可供调用,但不知道是属性调用还是方法调用?再次使用 `
print type(response.getcode)` 得到 `<type 'instancemethod'>` 因而判定为方法调用形式.

详情代码如下:

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取请求方信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print response.getcode()

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

- 响应对象的状态码信息(属性)

> `response.msg` : 获取响应对象的状态描述信息,例如状态码 `200` 对于 `OK`,而 `500` 对于 `INTERNAL SERVER ERROR`.

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取响应状态码
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/status/200')
    print response.code
    print response.msg

    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/status/500')
    print response.code
    print response.msg

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

> 正常请求状态是 `200 OK`,而请求发生异常很可能是 `500 INTERNAL SERVER ERROR` ,一旦出现异常如若异常处理则会报错,程序终止运行.

- 响应对象的访问链接(属性)

> `response.url` : 获取请求链接.

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取请求方信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print response.url

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

- 响应对象的访问链接(方法)

> `response.geturl()` : 获取请求链接.

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取请求方信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print response.geturl()

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

- 响应对象的访问链接(属性)

> `response.headers.dict` : 获取请求头信息并以字典形式显示.

在某些情况下发送请求时必须携带特定的请求头方可成功,因此需要清楚默认不设置请求头时服务端接收到的请求头是什么样子的,同样地,可使用 `print type(response.headers)` 结合 `print dir(response.headers)` 自行探索可供调用的属性和方法.

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取请求方信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print response.headers.dict

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

- 响应对象的请求头信息(方法)

> `response.info()` : 获取请求头信息并以逐行显示

和上一个 `response.headers.dict` 获取请求头信息类似,只不过 `response.info()` 适合肉眼显示而非程序使用.

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取请求方信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print response.info()

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

- 响应对象的响应体(方法)

> `response.read()` : 一次性读取响应体,适合响应体数据量比较小的情况,一次性全部读取到内存方便操作.

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取响应体信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print response.read()

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

`response.read()` 返回的是字符串,因此可以很方便用变量接收作后续处理,例如 `result = response.read()` :

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取响应体信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    result = response.read()
    print result

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

- 响应对象的响应体(方法)

> `response.readline()` : 逐行读取响应体,适用于数据体比较大的情况,循环读取直到最终无数据可读取为止.

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取响应体信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    line = response.readline()
    while line:
        print line
        line = response.readline()

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

`response.readline()` 只能逐行读取,因此想要获取完成的响应体需要进行手动拼接,例如:

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取响应体信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    result = ''
    line = response.readline()
    result = result + str(line)
    while line:
        line = response.readline()
        result = result + str(line)
    print result

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

> `str(line)` 是为了保证响应体字符串一定是字符串类型,其实应该不必如此,`response.readline()` 本身已经是字符串类型了.

- 响应对象的响应体(方法)

> `response.readlines()` : 遍历读取响应体,循环读取且保存到列表对象中,适合需要逐行处理情况.

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取响应体信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    for line in response.readlines():
        print line

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

同样地,如果需要针对 `response.readlines()` 方式获取完整响应体结果,可以如下进行拼接,示例如下:

```python
# -*- coding: utf-8 -*-
import urllib2

def use_simple_urllib2():
    '''
    获取响应体信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    result = ''
    for line in response.readlines():
        result = result + str(line)
    print result

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

> 上述多行代码还可以进一步转换成一行代码: `result = ''.join([line for line in response.readlines()])`

## POST 请求


## 参考文档

- [Python中read()、readline()和readlines()三者间的区别和用法](https://www.cnblogs.com/yun1108/p/8967334.html)
- [Python核心模块——urllib模块](https://www.cnblogs.com/sysu-blackbear/p/3629420.html )


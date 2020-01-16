# 第三方请求

## 实验环境

- `python` 版本

```bash
python --version
```

> 简化写法: `python -V`,笔者实验环境: `Python 2.7.16`

- `pip` 版本

```bash
pip --version
```

> 简化写法: `pip -V`,笔者实验环境: `pip 19.3.1`

- `python` vs `python3`

```bash
python3 -V

python -V
```

> `python3 -V` : `Python 3.7.5`
> `python -V` : `Python 2.7.16`

- `pip` vs `pip3`

```bash
pip3 -V

pip -V
```

> `pip3 -V` : `pip 19.3.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)`
> `pip -V` : `pip 19.3.1 from /Library/Python/2.7/site-packages/pip (python 2.7)`

## pip 基础命令

- 格式化显示已安装包列表

```bash
pip freeze
```

- 默认显示已安装包列表

```bash
pip list
```

## 虚拟环境 `virtualenv`

### 安装

如果本地环境没有安装过 `virtualenv`,则直接在终端命令行中运行 `virtualenv` 会报错,命令无法找到,如下图所示:

```bash
$ virtualenv
-bash: virtualenv: command not found
```

我们可以使用 `pip` 包管理工具安装第三方虚拟环境工具 `virtualenv` ,方便隔离不同环境,避免不同环境直接相互影响.

```bash
sudo pip install virtualenv
```

> 普通用户请运行 `pip install virtualenv --user` 本地化安装,超级用户请运行 `sudo pip install virtualenv` 全局安装.

如果没有报错信息,则表示安装成功,再次运行 `virtualenv` 会显示一大堆相关命令说明文档,如果失败依然会提示 `virtualenv: command not found` .

现在再次查看已安装包列表就会发现多了 `virtualenv` 包的版本信息,如果本地安装第三方包过多的话,可以使用 `| grep virtualenv` 管道符过滤出关键词 `virtualenv`.

```bash
pip freeze | grep virtualenv
```

### 使用
 
`virtualenv` 命令是独立的终端命令,可以终端命令行中直接输入 `virtualenv --help` 查看 `virtualenv` 的帮助信息,如下图所示:

```bash
$ virtualenv --help
Usage: virtualenv [OPTIONS] DEST_DIR

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --verbose         Increase verbosity.
  -q, --quiet           Decrease verbosity.
  -p PYTHON_EXE, --python=PYTHON_EXE
                        The Python interpreter to use, e.g.,
                        --python=python3.5 will use the python3.5 interpreter
                        to create the new environment.  The default is the
                        interpreter that virtualenv was installed with (/Syste
                        m/Library/Frameworks/Python.framework/Versions/2.7/Res
                        ources/Python.app/Contents/MacOS/Python)
  --clear               Clear out the non-root install and start from scratch.
  --no-site-packages    DEPRECATED. Retained only for backward compatibility.
                        Not having access to global site-packages is now the
                        default behavior.
  --system-site-packages
                        Give the virtual environment access to the global
                        site-packages.
  --always-copy         Always copy files rather than symlinking.
  --relocatable         Make an EXISTING virtualenv environment relocatable.
                        This fixes up scripts and makes all .pth files
                        relative.
  --no-setuptools       Do not install setuptools in the new virtualenv.
  --no-pip              Do not install pip in the new virtualenv.
  --no-wheel            Do not install wheel in the new virtualenv.
  --extra-search-dir=DIR
                        Directory to look for setuptools/pip distributions in.
                        This option can be used multiple times.
  --download            Download pre-installed packages from PyPI.
  --no-download, --never-download
                        Do not download pre-installed packages from PyPI.
  --prompt=PROMPT       Provides an alternative prompt prefix for this
                        environment.
  --setuptools          DEPRECATED. Retained only for backward compatibility.
                        This option has no effect.
  --distribute          DEPRECATED. Retained only for backward compatibility.
                        This option has no effect.
  --unzip-setuptools    DEPRECATED.  Retained only for backward compatibility.
                        This option has no effect.
```

根据帮助文档提示, `virtualenv` 的用法是 `virtualenv [OPTIONS] DEST_DIR`,其中选项(`OPTIONS`) 是可选的,目标目录(`DEST_DIR`)是必选的.

因此,假如将当前目录作为目标目录,因此虚拟环境的使用方法则是这样的:

```bash
virtualenv .env
```

> 由于目标目录主要是存储虚拟环境的相关配置,平时并不太关心具体内容而是交由 `virtualenv` 自动管理,我们只需要学习使用 `virtualenv` 相关命令即可,因此将目标目录(`DEST_DIR`) 设置成隐藏目录.


假如目标目录(`DEST_DIR`)是隐藏目录,想要查看目录内容可以运行 `ls -al` 进行查看,如果是可见目录,直接使用 `ls` 即可查看刚刚创建的目标目录.

```bash
$ ls -al
total 0
drwxr-xr-x   3 snowdreams1006  staff   96  1 12 20:51 .
drwxr-xr-x  17 snowdreams1006  staff  544  1 12 13:57 ..
drwxr-xr-x   6 snowdreams1006  staff  192  1 12 20:51 .env
```

现在已经知道目标目录(`DEST_DIR`)的确已经创建成功,既然作为虚拟环境的存储目录,肯定不能是空目录,使用 `tree .env -L 2` 限制二层显示目录结果并以树状展示.

> 如果提示 `command not found` 则说明当前环境并未安装,可以使用 `brew install tree` 进行安装也可以放弃终端使用可视化文件查看器浏览文件目录结构或者自行百度安装 `tree` 命令.

```bash
$ tree .env -L 2
.env
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── activate.ps1
│   ├── activate_this.py
│   ├── easy_install
│   ├── easy_install-2.7
│   ├── pip
│   ├── pip2
│   ├── pip2.7
│   ├── python
│   ├── python-config
│   ├── python2 -> python
│   ├── python2.7 -> python
│   └── wheel
├── include
│   └── python2.7 -> /System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7
└── lib
    └── python2.7

5 directories, 15 files
```

虽然现在已经创建了虚拟环境相关目录,但还没有激活该环境,比如现在运行 `pip freeze` 依然调用的是系统默认环境.

```bash
$ pip freeze
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
altgraph==0.10.2
asn1crypto==0.24.0
```

所以想要开启虚拟环境还差一步,这就是运行 `source .env/bin/activate` 进行激活该虚拟环境.

```bash
source .env/bin/activate
```

> 激活命令无任何输出提示并不表示无反应而是无话可说,没有消息就是好消息,有消息的情况大概率是出错信息或帮助信息.

```bash
(.env) $ python --version
Python 2.7.16

(.env) $ pip --version
pip 19.3.1 from .env/lib/python2.7/site-packages/pip (python 2.7)

(.env) $ pip freeze
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
```

> 再次运行 `python --version` 命令可以查看当前 `python` 版本信息,如果还不确定是否已经进入虚拟环境,不妨运行 `pip freeze` 对比分析和未运行 `source .env/bin/activate` 的输出结果是否一致.

一旦进入到虚拟环境后,这将是一个全新的环境,不会受到宿主机环境的影响,可以方便我们做学习测试之用,下面我们将开始正式学习 `requests` 类库!

## requests 类库

### 安装

```bash
pip install requests
```

> 上述命令默认安装的是最新版本,安装成功后可以运行 `pip freeze | grep requests` 查看已安装版本.

### 验证

```bash
(.env) $ pip freeze | grep requests
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
requests==2.22.0
```

> 具体版本号可能并不一致,过去的最新版很大可能不是现在的最新版,因为 `pip install requests` 默认安装的是当时的最新版而不是指定版本.

现在我们继续在终端命令行进行操作,输入 `python` 进入 `python` 解释器交互环境中,不用任何 IDE 而是纯粹的终端命令行足以教学演示 `requests` 类库的基本用法,加深学习印象.

```bash
(.env) $ python

WARNING: Python 2.7 is not recommended. 
This version is included in macOS for compatibility with legacy software. 
Future versions of macOS will not include Python 2.7. 
Instead, it is recommended that you transition to using 'python3' from within Terminal.

Python 2.7.16 (default, Nov  9 2019, 05:55:08) 
[GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.32.4) (-macos10.15-objc-s on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

> 请注意刚才我们在终端命令行直接输入 `python` 命令并回车确认后就已经进入到 `python` 解释器交互环境,最左侧的命令提示符也由`$`(也有可能你的提示符是`#`)变成了 `>>>` ,这就是已经进入 `python` 解释器交互环境的重要标志,一定要仔细区分命令行提示符的差异,知道自己身处何处才能做到游刃有余.

现在已经进入 `python` 解释器交互环境中而不是普通的终端命令行 `shell` 环境,因此我们可以使用刚才下载安装的 `requests` 类库.

在 `python` 中使用第三方类型是需要先 `import <module>` 进行引入后才能使用的,所以使用的第一步就是先导入 `import` .

```python
>>> import requests
```

同样地,导入 `requests` 类库没有任何提示信息,还记得之前激活虚拟环境使用的 `source .en/bin/activate` 命令吗?

没有消息就是好消息!

如果你不信的话,故意导入 import 一个不存在的第三方包,看一下是否依然没有消息吧,比如: import snowdreams1006

```python
>>> import snowdreams1006
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named snowdreams1006
```

上述命令出现 `ImportError: No module named snowdreams1006` 导入错误,现在总该相信"没有消息就是好消息"这句至理名言了吧!

导入成功后,当然是查看关于命令的帮助信息了,师傅领进门修行在个人,学习还是要多看官方文档,少看乱七八糟的博客教程!

```python
>>> help("requests")
```

继续输入 `help("requests")` 命令可以查看关于第三方包的帮助文档,同时也离开了 `python` 解释器交互环境,最明显的差别在于命令提示符 `>>>` 不见了!

 
```bash
Help on package requests:

NAME
    requests

FILE
    /Users/snowdreams1006/Documents/workspace/snowdreams1006.github.io/python/requests/.env/lib/python2.7/site-packages/requests/__init__.py

MODULE DOCS
    https://docs.python.org/library/requests

DESCRIPTION
    Requests HTTP Library
    ~~~~~~~~~~~~~~~~~~~~~
    
    Requests is an HTTP library, written in Python, for human beings. Basic GET
    usage:
    
       >>> import requests
       >>> r = requests.get('https://www.python.org')
       >>> r.status_code
       200
```

不断点击回车键可以一直查看帮助文档直到尽头,想要退出帮助文档返回到上一层环境,只需要敲入 `q`(英文单词 `quit` 的首字母,表示"退出"的意思.)即可返回到熟悉的 `>>>` 环境.

如果想要返回到普通的终端命令行 `shell` 环境应该继续往上返回,那么是不是继续敲入 `q` 就可以了呢?

```bash
>>> q
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'q' is not defined
>>> quit
Use quit() or Ctrl-D (i.e. EOF) to exit
>>> quit()
(.env) $ 
```

虽然不能直接返回到普通终端命令行 `shell` 环境,但是根据一步一步的提示,确实可以返回,只不过没有做缩写的映射罢了!

## httpbin

现在我们已经安装了 `requests` 类库,还需要服务端供我们学习测试接收 `http` 请求,这里推荐 `httpbin` 类库.

### 安装

```bash
pip install gunicorn httpbin
```

> 一次性安装多个第三方类库,包括 `gunicorn` 和 `httpbin`

### 使用

```bash
gunicorn htpbin:app
```

> 启动本地服务器后,默认端口是 `8000`,可以在浏览器地址栏输入并访问: `http://127.0.0.1:8000`

## http

> HyperText Transfer Protocal : 超文本传输协议

[http://httpbin.snowdreams1006.cn/](http://httpbin.snowdreams1006.cn/)

```bash
curl -v http://httpbin.snowdreams1006.cn/
```

## urllib

问题来啦! `urllib`,`urllib2`,`urllib3` 是进化关系吗?

- urllib 和 urllib2 是相互独立的模块
- requests 库使用了 urllib3(多次请求重复使用同一个 socket)

### 激活环境

```bash
source .env/bin/activate
```

### 核心代码

- `GET` 请求无参数直接发送: 获取发送方 `ip`

> [http://httpbin.snowdreams1006.cn/ip](http://httpbin.snowdreams1006.cn/ip)

```bash
curl -X GET "http://httpbin.snowdreams1006.cn/ip" -H "accept: application/json"
```

> `curl`

```python
# -*- coding: utf-8 -*-
import urllib2

get_ip_url = 'http://httpbin.snowdreams1006.cn/ip'

def use_simple_urllib2_get_ip():
  response = urllib2.urlopen(get_ip_url)
  print '>>>>Response Headers:'
  print response.info()
  print '>>>>Response body:'
  print ''.join([line for line in response.readlines()])

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
```

> `python`

- `GET` 请求无参数直接发送: 获取发送方 `user-agent`

> [http://httpbin.snowdreams1006.cn/user-agent](http://httpbin.snowdreams1006.cn/user-agent)

```bash
curl -X GET "http://httpbin.snowdreams1006.cn/user-agent" -H "accept: application/json"
```

```python
## -*- coding: utf-8 -*-
import urllib2

get_user_agent_url = 'http://httpbin.snowdreams1006.cn/user-agent'

def use_simple_urllib2_get_user_agent():
  response = urllib2.urlopen(get_user_agent_url)
  print('>>>Response Headers:')
  print(response.info())
  print('>>>Resonse Body:')
  print(''.join([line for line in response.readlines()]))

if __name__ == '__main__':
  print('>>>Use simple1 urllib2 to get user-agent:')
  use_simple_urllib2_get_user_agent()
```

```python
# -*- coding: utf-8 -*-
import urllib
import urllib2

URL_IP = 'http://httpbin.snowdreams1006.cn/ip'
URL_GET = 'http://httpbin.snowdreams1006.cn/get'

def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    print '>>>>Response Headers:'
    print response.info()
    print '>>>>Response body:'
    print ''.join([line for line in response.readlines()])

def use_params_urllib2():
    params = urllib.urlencode({'param1': 'hello', 'param2': 'world'})
    response = urllib2.urlopen('?'.join([URL_GET, '%s']) % params)
    print '>>>>Response Headers:'
    print response.info()
    print '>>>>Status Code:'
    print response.getcode()
    print '>>>>Request body:'
    print ''.join([line for line in response.readlines()])

if __name__ == '__main__':
    print '>>>Use simple urllib2:'
    use_simple_urllib2()
    print ''
    print '>>>Use params urllib2:'
    use_params_urllib2()
```

> `urllib_demo.py`

### 使用

```bash
python urllib_demo.py
```

## get

## post

```python
import urllib
import urllib2

url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
```

### 参考文档

- [什么是HTTP协议?](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
- [RFC7230](https://tools.ietf.org/html/rfc7230#page-19)
- [urllib和urllib2区别](http://ver007.com/2015/09/22/276.html)


## 参考文档

- [mac 下 python2 、python3和pip、pip3](https://www.jianshu.com/p/2e4851df72fb)
- [python3.7如何与python2.7共存？快速切换python版本方案](https://newsn.net/say/python-switch/)
- [https://github.com/jian-en/imooc-requests](https://github.com/jian-en/imooc-requests)
- [https://pypi.org/project/requests/](https://pypi.org/project/requests/)
- [https://requests.readthedocs.io/en/master/](https://requests.readthedocs.io/en/master/)
- [https://github.com/psf/requests](https://github.com/psf/requests)
- [https://www.kennethreitz.org/](https://www.kennethreitz.org/)

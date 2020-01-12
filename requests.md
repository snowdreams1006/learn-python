# requests类库

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



## 参考文档

- [mac 下 python2 、python3和pip、pip3](https://www.jianshu.com/p/2e4851df72fb)
- [python3.7如何与python2.7共存？快速切换python版本方案](https://newsn.net/say/python-switch/)
- [https://pypi.org/project/requests/](https://pypi.org/project/requests/)
- [https://requests.readthedocs.io/en/master/](https://requests.readthedocs.io/en/master/)
- [https://github.com/psf/requests](https://github.com/psf/requests)
- [https://www.kennethreitz.org/](https://www.kennethreitz.org/)

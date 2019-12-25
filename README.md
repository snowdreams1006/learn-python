# learn-python

## 认识基本数据类型

### 前提条件

`python` 基本环境已经**安装并配置**成功,可以在**任意目录**中运行 `python` 脚本命令.

```python
$ python

WARNING: Python 2.7 is not recommended. 
This version is included in macOS for compatibility with legacy software. 
Future versions of macOS will not include Python 2.7. 
Instead, it is recommended that you transition to using 'python3' from within Terminal.

Python 2.7.16 (default, Nov  9 2019, 05:55:08) 
[GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.32.4) (-macos10.15-objc-s on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

> `macOS` 系统**默认自带** `python` 环境,然而版本较低,一般都是 `python2` ,目前主流软件一般使用 `python3`,所以需要**自行安装** `python3` .


根据命令行输出内容提示 `python` 命令默认使用的是 `python2.7` 版本,推荐使用 `python3` 命令,这里默认读者已经安装并配置好 `python3` 的相关环境.

不论输入 `python` 还是 `python3` 命令,只要出现 `>>> ` 提示符即表示已经进入 `python` 环境,下面可以直接运行 `python` 脚本.

```bash
Python 2.7.16 (default, Nov  9 2019, 05:55:08) 
[GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.32.4) (-macos10.15-objc-s on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

- 帮助命令

在 `python` 命令行环境中,根据上一步的提示可以输入 `Type "help", "copyright", "credits" or "license" for more information.` 获取更多信息,按照提示输入 `help` 命令得到下面的输出内容:

```python
>>> help
Type help() for interactive help, or help(object) for help about object.
```

根据提示应该输入 `help()` 获取交互性帮助或者输入 `help(object)` 获取关于对象的帮助信息.

如你提示,让我们继续尝试,看一下会输出什么样的帮助信息:

```python
>>> help()

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> 
```

由此可见,确实输出了一大堆帮助信息,这是在线帮助工具,如果是新手,推荐阅读[在线教程](http://docs.python.org/2.7/tutorial/)

在使用中遇到不懂的地方可以获取帮助文档,如需退出帮助文档可以输入 `quit` 命令.

比如想要获取可用模块,关键字,主题等,可以输入 `modules` ,`keywords` ,`topics` ,同时还会继续给出详细帮助信息,比如现在可以输入 `modules spam` 查看关于 `spam` 模块的帮助信息.

> 注意: 从最初的 `python` 交互式命令行中输入 `help()` 已经进入了帮助文档的交互式命令环境,最左边的命令行提示符也由 `>>>` 变成了现在的 `help> `,表明两者不是一个环境!

```python
help> modules spam

Here is a list of matching modules.  Enter any module name to get more help.
```

> 在帮助文档交互环境中输入 `modules spam` 命令可以获取相关的帮助信息,具体的帮助信息因命令不同而不同,不再深究.

现在如果想要

## 阅读更多

- [字符串、整数、浮点数](https://mp.weixin.qq.com/s/shTf5mQAwqJHuiNCwRJ0-g)

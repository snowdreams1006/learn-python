# 基础数据类型

## 前提条件

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

现在如果想要退回**帮助文档交互式环境**返回到 `python` 命令交互式环境的话,只需要按照输入 `help()` 命令给出的提示信息输入 `quit` 即可返回继续输入其余的 "help", "copyright", "credits" or "license" 等命令.

```python
help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
```

命令提示符已经从 `help>` 变回了 `>>> ` ,表明现在已经离开了帮助环境并进入 `python` 环境.

- 版权命令

尝试过 `help()` 命令后,继续一次尝试其余的几个命令: Type "help", "copyright", "credits" or "license" for more information.

```python
>>> copyright
Copyright (c) 2001-2019 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
>>> 
```

> `copyright` 命令直接输出了版权信息,最左边的命令行提示符并没有发生改变,表明现在依然是处于 `python` 交互式环境.

- 致谢人员

依然处于 `python` 交互式环境中输入 `credits` 命令可以查看 `python` 的幕后工作人员,也可以访问[www.python.org](www.python.org) 查看更多信息.

```python
>>> credits
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
>>> 
```

> `Python` 的发展壮大离不开贡献者的辛苦付出,感谢大佬们的智慧.

- 版权命令

现在只剩下最后一个 `license` 命令,已经迫不及待想要快点结束了!

```python
>>> license
Type license() to see the full license text
```

看样子和 `help` 命令一样,不是直接输入 `license` 而是需要输入 `license()` 命令才可以查看版权信息,难不成还会离开 `>>> ` 提示符的 `python` 环境吗?

```bash
>>> license()
A. HISTORY OF THE SOFTWARE
==========================

Python was created in the early 1990s by Guido van Rossum at Stichting
Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
as a successor of a language called ABC.  Guido remains Python's
principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for
National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
in Reston, Virginia where he released several versions of the
software.

In May 2000, Guido and the Python core development team moved to
BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
year, the PythonLabs team moved to Digital Creations, which became
Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
https://www.python.org/psf/) was formed, a non-profit organization
created specifically to own Python-related Intellectual Property.
Zope Corporation was a sponsoring member of the PSF.

All Python releases are Open Source (see http://www.opensource.org for
the Open Source Definition).  Historically, most, but not all, Python
Hit Return for more, or q (and Return) to quit: 
```

命令行提示符好像没有发生变化,最后一句话说想要查看更多信息可以敲入 `回车` 键或者输入 `q` (然后 `回车`) 退出.

```python
releases have also been GPL-compatible; the table below summarizes
the various releases.

    Release         Derived     Year        Owner       GPL-
                    from                                compatible? (1)

    0.9.0 thru 1.2              1991-1995   CWI         yes
    1.3 thru 1.5.2  1.2         1995-1999   CNRI        yes
    1.6             1.5.2       2000        CNRI        no
    2.0             1.6         2000        BeOpen.com  no
    1.6.1           1.6         2001        CNRI        yes (2)
    2.1             2.0+1.6.1   2001        PSF         no
    2.0.1           2.0+1.6.1   2001        PSF         yes
    2.1.1           2.1+2.0.1   2001        PSF         yes
    2.1.2           2.1.1       2002        PSF         yes
    2.1.3           2.1.2       2002        PSF         yes
    2.2 and above   2.1.1       2001-now    PSF         yes

Footnotes:

(1) GPL-compatible doesn't mean that we're distributing Python under
    the GPL.  All Python licenses, unlike the GPL, let you distribute
    a modified version without making your changes open source.  The
Hit Return for more, or q (and Return) to quit: 
```

显示了更多的信息,最后一句话依然是 "Hit Return for more, or q (and Return) to quit: " ,这一次当然是 `q` 并回车了啊!

```python
Hit Return for more, or q (and Return) to quit: q
>>>
```

再一次出现 `>>>` 提示符,现在可以继续愉快地玩耍 `python` 脚本了呢!

## 你好,python

如果还没有进入 `python` 环境,可以输入 `python` 或者 `python3` 进入交互式环境.

```bash
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

> 如果是 `python2` 环境可以输入 `python` 进入交互式环境.


```bash
$ python3
Python 3.7.5 (default, Nov  1 2019, 02:16:23) 
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

> 如果是 `python3` 环境可以输入 `python3` 进入交互式环境.

如果你正在处于 `python` 交互式环境,可以输入 `print('hello python!')` 来表明正式入门开始学习 `python` .

```python
>>> print('hello python!')
hello python!
```
 
如果你想退出 `python` 环境可以输入 `exit()` 命令或者 `Ctrl-D` 来退出.

```python
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
$ 
```

> 按照已有的开发经验推断,退出命令行可以输入 `quit` 或 `exit` 或者 `Ctrl-D` ,试错学习后知道了想要退出 `python` 环境支持 `exit() or Ctrl-D ` 两种方式.

## 扫盲基本类型

### 整数

和其他编程语言一样,整数和数学意义上的概念一样,在 `python` 交互式命令行环境中支持四则运算,请不要问 `5/2` 为什么等于 `2` 而不是 `2.5` 这样的基础问题.

```python
>>> 1
1
>>> 1+1
2
```

### 小数

不同于整数之处在于浮点数保留小数,整数运算的 `5/2=2` 而浮点数运算的 `5.0/2` 或者 `5/2.0` 均等于 `2.5` 而不是 `2` .

```python
>>> 3.1415926*2
6.2831852
>>> 5/2.0
2.5
>>> 5.0/2
2.5
>>> 
```

当数据非常大或者非常小的时候,浮点数可以用来表示科学计算法,比如先定一个小目标,一年挣他一个亿?

```python
>>> 1.0e8
100000000.0
>>> 1e8
100000000.0
>>> 1e-2
0.01
```

> 不论是 `1.0e8` 还是 `1e8` 计算结果均是浮点数,不信你自己试试看!
 
### 字符串

不论是现实生活中还是计算机的编程世界里,字符串才是使用最频繁的一种数据类型,`python` 中的字符串和数字类型在一起会发生什么样的关系呢?

- 左右单引号和双引号均可,但不支持混用

> 左边包裹的是双引号 `"` ,则右边也必须是双引号 `"`,如果左边是单引号 `'` 则右边也需要是单引号 `'`.

```python
>>> print("hello python!")
hello python!
>>> print('hello python!')
hello python!
```

> 正确示例: `print("hello python!")` 或 `print('hello python!')`

```python
>>> print("hello python!')
  File "<stdin>", line 1
    print("hello python!')
                         ^
SyntaxError: EOL while scanning string literal
>>> print('hello python!")
  File "<stdin>", line 1
    print('hello python!")
                         ^
SyntaxError: EOL while scanning string literal
```

> 错误示例: `print("hello python!')` 或 `print('hello python!")`

- 内部单引号和双引号可配合,特殊字符要转义

> 如果用单引号包裹字符串而该字符串本身也有单引号,则需要使用 `\'` 进行转义(`'welcome to \'snowdreams1006.cn\''`),如果该字符串是双引号,那么可以直接使用(`'welcome to "snowdreams1006.cn"'`).
> 如果用双引号包裹的字符串也是类似情况,分别是 `"welcome to \"snowdreams1006.cn\""` 和 `"welcome to 'snowdreams1006.cn'"` .

```python
>>> print("welcome to snowdreams1006.cn")
>>> print('welcome to snowdreams1006.cn')
>>> print("welcome to 'snowdreams1006.cn'")
welcome to 'snowdreams1006.cn'
>>> print('welcome to "snowdreams1006.cn"')
welcome to "snowdreams1006.cn"
>>> print('welcome to \'snowdreams1006.cn\'')
welcome to 'snowdreams1006.cn'
>>> print("welcome to \"snowdreams1006.cn\"")
welcome to "snowdreams1006.cn"
```

> 正确示例: `print("welcome to 'snowdreams1006.cn'")` 或 `print('welcome to "snowdreams1006.cn"')` 或 `print('welcome to \'snowdreams1006.cn\'')` 或 `print("welcome to \"snowdreams1006.cn\"")`

```python
>>> print("welcome to "snowdreams1006.cn"")
  File "<stdin>", line 1
    print("welcome to "snowdreams1006.cn"")
                                    ^
SyntaxError: invalid syntax
>>> print('welcome to 'snowdreams1006.cn'')
  File "<stdin>", line 1
    print('welcome to 'snowdreams1006.cn'')
                                    ^
SyntaxError: invalid syntax
```

> 错误示例: `print("welcome to "snowdreams1006.cn"")` 或 `print('welcome to 'snowdreams1006.cn'')`







### 相互转换

## 阅读更多

- [字符串、整数、浮点数](https://mp.weixin.qq.com/s/shTf5mQAwqJHuiNCwRJ0-g)

# 范例教学

## GET 请求

### 环境准备

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


## POST 请求


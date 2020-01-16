# 范例教学

## GET 请求

### 环境准备

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
(.env) snowdreams1006s-MacBook-Pro:urllib snowdreams1006$ which python
/Users/snowdreams1006/Documents/workspace/snowdreams1006.github.io/python/src/url/urllib/.env/bin/python
(.env) snowdreams1006s-MacBook-Pro:urllib snowdreams1006$ which pip
/Users/snowdreams1006/Documents/workspace/snowdreams1006.github.io/python/src/url/urllib/.env/bin/pip
(.env) snowdreams1006s-MacBook-Pro:urllib snowdreams1006$ 
```

> 演示环境已开启虚拟环境,因此 `python` 和 `pip` 文件位置正是当前目录 `.env` 而不是系统默认环境,如果未开启虚拟环境则显示的是系统目录.

## POST 请求


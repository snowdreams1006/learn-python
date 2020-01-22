# 快速上手

> [https://www.crummy.com/software/BeautifulSoup/](https://www.crummy.com/software/BeautifulSoup/)

Python 第三方库,从 html 或 xml 提取数据

## 安装并测试 beautifulsoup4

- 安装: `pip install beautifulsoup4`
- 测试: `import bs4`

## 使用bs4

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf8')

# 搜索节点
soup.find_all(name,attrs,string)

# 查看所有标签为 a 的节点
soup.find_all('a')

# 查找所有标签为a,链接符合/view/123.html 形式的节点
soup.find_all('a',href='/view/123.html')
soup.find_all('a',href=re.compile(r'/view/\d+\.html'))

# 查找所有标签为div,class 为 abc,文字为 python 的节点
soup.find_all('div',class_='abc',string='python')

# 访问节点信息: <a href='1.html'>python</a> 

# 获取查找到a节点的标签名称
node.name
# 获取查找到的a节点的 href 属性
node['href']
# 获取查找到a节点的链接文字
node.get_text()
```
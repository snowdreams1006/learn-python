# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

def test_bs4_demo():
    html_doc = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>

        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>

        <p class="story">...</p>
        """
    soup = BeautifulSoup(html_doc, 'html.parser',from_encoding='utf-8')
    # print(soup.prettify())
    # print dir(soup)
    # print dir(soup.title)
    print soup.title
    print soup.title.name
    print soup.title.string
    print soup.title.parent.name
    print soup.p
    print soup.p['class']
    print soup.a
    print soup.find_all('a')
    print soup.find(id="link3")

    for link in soup.find_all('a'):
        print(link.get('href'))

    print(soup.get_text())

    # 获取所有链接 
    for link in soup.find_all('a'):
        print link.name,link['href'],link.get_text()

    # 获取lacie的链接
    lacie_node = soup.find('a',href='http://example.com/lacie')
    print lacie_node.name,lacie_node['href'],lacie_node.get_text()

    # 正则匹配
    tillie_node = soup.find('a',href=re.compile(r'ill'))
    print tillie_node.name,tillie_node['href'],tillie_node.get_text()

    # 获取 p 段落文字
    pnode = soup.find('p',class_='title')
    print pnode.name,pnode.get_text()

if __name__ == '__main__':
    test_bs4_demo()
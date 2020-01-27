# -*- coding: utf-8 -*-
import requests
import bs4
import os
import random
import json
import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def search_item(keyword='充气娃娃',page=1,s=1):
    '''
    根据关键字搜索京东商品
    '''
    try:
        # 搜索商品
        url = 'https://search.jd.com/Search'
        params = {
            'keyword': keyword,
            'enc': 'utf-8',
            'wq': keyword,
            'qrst':1,
            'rt':1,
            'stop':1,
            'vt':2,
            'page':page,
            's':s,
            'click':0
        }
        headers = {
            'referer': 'https://www.jd.com/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        response = requests.get(url=url, params=params, headers=headers)
        response.raise_for_status()
        response.encoding = 'utf-8'
        response_text = response.text

        # 解析商品页面
        url = response.url
        parse_item(url,response_text)
    except Exception as e:
        print('获取商品列表异常',e)

def parse_item(url,html_origin):
    '''
    解析商品列表页面结构
    '''
    try:
        # 解析商品列表页面结构
        soup = bs4.BeautifulSoup(html_origin, 'html.parser')
        html_prettify = soup.prettify('utf-8')

        # 先提前创建 html 目录,再保存原始网页和美化后网页
        parse_item_origin_path = './html/parse_item_origin.html'
        parse_item_prettify_path = './html/parse_item_prettify.html'
        if not os.path.exists(os.path.dirname(parse_item_origin_path)):
          os.mkdir(os.path.dirname(parse_item_origin_path))
        with open(parse_item_origin_path, 'w', encoding='utf-8') as wf:
            wf.write(html_origin)
        with open(parse_item_prettify_path, 'wb') as wbf:
            wbf.write(html_prettify)

        # 解析商品列表
        for item_li in soup.find_all('li',class_='gl-item'):
            # 详情链接
            item_detail = item_li.find('a')
            item_detail_url = 'https:%s' % item_detail['href']

            # 封面图片链接
            item_img = item_li.find('img')
            item_img_url = 'https:%s' % item_img['source-data-lazy-img']

            # 标题描述
            item_title = item_li.find('div',class_='p-name p-name-type-2').find('em')
            item_title_text = item_title.get_text()

            # 下载图片
            download_image(item_detail_url,item_img_url)

            # 访问商品详情
            # visit_item_detail(item_detail_url)

            print(f'标题: {item_title_text} 图片: {item_img_url} 详情: {item_detail_url}')
    except Exception as e:
        print('解析商品列表异常',e)

def visit_item_detail(url):
    '''
    访问京东商品详情页面
    '''
    try:
        # 搜索商品
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        response.encoding = 'gbk'
        response_text = response.text

        # 解析商品页面
        parse_item_detail(url,response_text)
    except Exception as e:
        print('访问商品详情异常')

def parse_item_detail(url,html):
    '''
    解析商品详情页面结构
    '''
    try:
        # 保存原始网页数据
        detail_item_html_name = os.path.basename(url)
        with open('./html/parse_item_detail_%s' % detail_item_html_name, "w", encoding="utf-8") as wf:
            wf.write(html)

        # 批量获取商品评价
        detail_item_product_id = detail_item_html_name[:detail_item_html_name.rindex('.html')]
        batch_get_comment(detail_item_product_id)
    except Exception as e:
        print('解析商品详情异常',e)

def get_comment(productId,page=0):
    '''
    分页获取商品评论数据
    '''
    try:
        # 评价商品
        url = 'https://club.jd.com/comment/productPageComments.action'
        params = {
            'productId': productId,
            'score': 0,
            'sortType': 5,
            'page':page,
            'pageSize':10,
            'isShadowSku':0,
            'fold':1
        }
        headers = {
            'referer': 'https://item.jd.com/%s.html' % productId,
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        response = requests.get(url=url, params=params, headers=headers)
        response.raise_for_status()
        response_json = response.json()

        # 保留原始评论数据
        with open('./comment/%s_%d.json' % (productId,page), 'w') as wf:
            wf.write(json.dumps(response_json, indent=4, ensure_ascii=False))

        # 遍历追加评论内容
        comment_txt_name = './comment/%s.txt' % productId
        for comments in response_json.get('comments'):
            with open(comment_txt_name, 'a') as af:
                af.write(comments.get('content') + '\n')
    except Exception as e:
        print('获取商品评价异常',e)

def download_image(item_detail_url,item_img_url):
    '''
    下载商品封面图
    '''
    try:
        # 提前创建 image 目录
        detail_item_html_name = os.path.basename(item_detail_url)
        detail_item_product_id = detail_item_html_name[:detail_item_html_name.rindex('.html')]
        detail_item_img_name = os.path.basename(item_img_url)
        parse_item_origin_path = './image/download_image_%s_%s' % (detail_item_product_id,detail_item_img_name)
        if not os.path.exists(os.path.dirname(parse_item_origin_path)):
          os.mkdir(os.path.dirname(parse_item_origin_path))
        
        # 下载图片
        if not os.path.exists(parse_item_origin_path):
          response = requests.get(item_img_url)
          response.raise_for_status()
          response_content = response.content
          with open(parse_item_origin_path, 'wb') as wbf:
              wbf.write(response_content)
    except Exception as e:
        print('下载商品异常',e)

def cut_word(productId):
    '''
    对评论数据进行分词
    '''
    comment_txt_name = './comment/%s.txt' % productId
    if os.path.exists(comment_txt_name):
      with open(comment_txt_name,'r') as rf:
          comment_txt = rf.read()
          wordlist = jieba.cut(comment_txt, cut_all=True)
          wl = ' '.join(wordlist)
          # 保存原始分词结果
          jieba_txt_name = './jieba/%s.txt' % productId
          if not os.path.exists(jieba_txt_name):
            with open(jieba_txt_name, 'w') as wf:
              wf.write(wl)

def create_word_cloud(productId):
    '''
    生成词云
    '''
    # 设置词云形状图片
    wc_mask = np.array(Image.open('./cover/3958b11408cc3e88.jpg'))
    # 设置词云的一些配置，如：字体，背景色，词云形状，大小
    wc = WordCloud(background_color="white", max_words=2000, mask=wc_mask, scale=4,
                   max_font_size=50, random_state=42, font_path='/System/Library/Fonts/STHeiti Medium.ttc')
    # 生成词云
    jieba_txt_name = './jieba/%s.txt' % productId
    if os.path.exists(jieba_txt_name):
      with open(jieba_txt_name,'r') as rf:
          jieba_txt = rf.read()
          wc.generate(text=jieba_txt)

          # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
          plt.imshow(wc, interpolation="bilinear")
          plt.axis("off")
          plt.figure()
          plt.show()

          # 保存到文件
          wc.to_file('./wordcloud/%s.png' % productId)

def batch_search_item(keyword='充气娃娃'):
    '''
    批量分页搜索京东商品
    '''
    for pn in range(1, 4):
        # page 是 2pn-1 
        page = pn * 2 - 1
        # 不固定请求参数 s,大概相差 60
        s = pn * 60 - random.randint(50, 60)
        search_item(keyword,page,s)

def batch_get_comment(productId):
    '''
    批量分页搜索京东商品
    '''
    comment_txt_name = './comment/%s.txt' % productId
    if os.path.exists(comment_txt_name):
        os.remove(comment_txt_name)
    for i in range(3):
        get_comment(productId,page=i)
    # 生成词云
    create_word_cloud(productId)

def main():
    # batch_search_item('充气娃娃')
    search_item('充气娃娃')


if __name__ == '__main__':
    main()
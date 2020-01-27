# -*- coding: utf-8 -*-
import requests
import urllib
import bs4
import os
import random
import time
import json
import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def batch_search_item(keyword='充气娃娃'):
    '''
    批量分页搜索京东商品
    '''
    for pn in range(1, 10):
        # page 是 2pn-1 
        page = pn * 2 - 1
        # 不固定请求参数 s,大概相差 60
        s = pn * 60 - random.randint(50, 60)
        search_item(keyword,page,s)
        time.sleep(random.randint(5, 60))

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
        url_result = urllib.parse.urlsplit(url)
        query = dict(urllib.parse.parse_qsl(url_result.query))
        page = query.get('page')
        pn = int((int(page)+1)/2)
        parse_item_origin_path = './html/parse_item_origin_%d.html' % pn
        parse_item_prettify_path = './html/parse_item_prettify_%d.html' % pn
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

            print(f'图片: {item_img_url} 详情: {item_detail_url}')

            # 下载图片
            download_image(item_detail_url,item_img_url)

            # 批量读取商品评价
            batch_get_comment(item_detail_url)
    except Exception as e:
        print('解析商品列表异常',e)

def download_image(item_detail_url,item_img_url):
    '''
    下载商品封面图
    '''
    try:
        # 提前创建 image 目录
        detail_item_html_name = os.path.basename(item_detail_url)
        detail_item_product_id = detail_item_html_name[:detail_item_html_name.rindex('.html')]
        detail_item_img_name = os.path.basename(item_img_url)
        download_image_path = './image/download_image_%s_%s' % (detail_item_product_id,detail_item_img_name)
        if not os.path.exists(os.path.dirname(download_image_path)):
          os.mkdir(os.path.dirname(download_image_path))
        
        # 下载图片
        if not os.path.exists(download_image_path):
          response = requests.get(item_img_url)
          response.raise_for_status()
          response_content = response.content
          with open(download_image_path, 'wb') as wbf:
              wbf.write(response_content)
    except Exception as e:
        print('下载商品异常',e)

def batch_get_comment(item_detail_url):
    '''
    批量分页搜索京东商品
    '''
    # 提前创建 comment 目录
    detail_item_html_name = os.path.basename(item_detail_url)
    detail_item_product_id = detail_item_html_name[:detail_item_html_name.rindex('.html')]
    batch_get_comment_txt_path = './comment/batch_get_comment_%s.txt' % detail_item_product_id
    if not os.path.exists(os.path.dirname(batch_get_comment_txt_path)):
      os.mkdir(os.path.dirname(batch_get_comment_txt_path))
    if os.path.exists(batch_get_comment_txt_path):
      os.remove(batch_get_comment_txt_path)
    # 批量获取评论数据
    for i in range(10):
        get_comment(item_detail_url,page=i)
        time.sleep(random.randint(5, 60))

    # 中文分词处理
    if os.path.exists(batch_get_comment_txt_path):
      with open(batch_get_comment_txt_path,'r') as rf:
          comment_txt = rf.read()
          cut_word(item_detail_url,comment_txt)

    # 生成词云
    cut_word_txt_path = './jieba/cut_word_txt_path_%s.txt' % detail_item_product_id
    if os.path.exists(cut_word_txt_path):
      with open(cut_word_txt_path,'r') as rf:
          jieba_txt = rf.read()
          create_wordcloud(item_detail_url,jieba_txt)

def get_comment(item_detail_url,page=0):
    '''
    分页获取商品评论数据
    '''
    try:
        # 解析商品 id
        detail_item_html_name = os.path.basename(item_detail_url)
        detail_item_product_id = detail_item_html_name[:detail_item_html_name.rindex('.html')]

        #  获取商品评价数据
        url = 'https://club.jd.com/comment/productPageComments.action'
        params = {
            'productId': detail_item_product_id,
            'score': 0,
            'sortType': 5,
            'page':page,
            'pageSize':10,
            'isShadowSku':0,
            'fold':1
        }
        headers = {
            'referer': item_detail_url,
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        response = requests.get(url=url, params=params, headers=headers)
        response.raise_for_status()
        response_json = response.json()

        # 保存原始评论数据
        get_comment_json_path = './comment/get_comment_%s_%d.json' % (detail_item_product_id,page)
        if not os.path.exists(os.path.dirname(get_comment_json_path)):
          os.mkdir(os.path.dirname(get_comment_json_path))
        with open(get_comment_json_path, 'w') as wf:
            wf.write(json.dumps(response_json, indent=4, ensure_ascii=False))

        # 遍历追加评论内容
        batch_get_comment_txt_path = './comment/batch_get_comment_%s.txt' % detail_item_product_id
        for comments in response_json.get('comments'):
            with open(batch_get_comment_txt_path, 'a') as af:
                af.write(comments.get('content') + '\n')
    except Exception as e:
        print('获取商品评价异常',e)

def cut_word(item_detail_url,word):
    '''
    对评论数据进行分词
    '''
    detail_item_html_name = os.path.basename(item_detail_url)
    detail_item_product_id = detail_item_html_name[:detail_item_html_name.rindex('.html')]
    cut_word_txt_path = './jieba/cut_word_%s.txt' % detail_item_product_id
    if not os.path.exists(os.path.dirname(cut_word_txt_path)):
      os.mkdir(os.path.dirname(cut_word_txt_path))
    
    # jieba 分词处理
    wordlist = jieba.cut(word, cut_all=True)
    wl = ' '.join(wordlist)
    with open(cut_word_txt_path, 'w') as wf:
      wf.write(wl)

def create_wordcloud(item_detail_url,word):
    '''
    生成词云
    '''
    # 生成词云
    detail_item_html_name = os.path.basename(item_detail_url)
    detail_item_product_id = detail_item_html_name[:detail_item_html_name.rindex('.html')]
    create_wordcloud_img_path = './wordcloud/create_wordcloud_%s.png' % detail_item_product_id
    if not os.path.exists(os.path.dirname(create_wordcloud_img_path)):
      os.mkdir(os.path.dirname(create_wordcloud_img_path))

    # 匹配搜索 image 目录下的封面图
    if os.path.exists('./image'):
      for name in os.listdir('./image'):
        if os.path.splitext(name)[0].startswith('download_image_%s' % detail_item_product_id):
          # 设置词云形状图片
          wc_mask = np.array(Image.open('./image/%s' % name))
          # 设置词云的一些配置，如：字体，背景色，词云形状，大小
          wc = WordCloud(background_color="white", max_words=2000, mask=wc_mask, scale=4,
                         max_font_size=50, random_state=42, font_path='/System/Library/Fonts/STHeiti Medium.ttc')
          wc.generate(text=word)
          plt.imshow(wc, interpolation="bilinear")
          plt.axis("off")
          # plt.figure()
          # plt.show()

          # 保存到文件
          wc.to_file(create_wordcloud_img_path) 
          break 

def main():
    batch_search_item('充气娃娃')

if __name__ == '__main__':
    main()
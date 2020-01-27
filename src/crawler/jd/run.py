# -*- coding: utf-8 -*-
import requests
import bs4
import os
import random
import json

def batch_search_item(keyword='充气娃娃'):
    '''
    批量分页搜索京东商品
    '''
    for pn in range(1,101):
        # page 是 2pn-1 
        page = pn * 2 - 1
        # 不固定请求参数 s,大概相差 60
        s = pn * 60 - random.randint(50, 60)
        search_item(keyword,page,s)

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
        parse_item(url,response_text)
    except Exception as e:
        print('搜索商品异常')

def parse_item(url,html):
    '''
    解析商品列表页面结构
    '''
    try:
        # 保存原始网页数据
        with open('./html/parse_item.html', "w", encoding="utf-8") as wf:
            wf.write(html)

        # 解析商品列表页面结构
        soup = bs4.BeautifulSoup(html, 'html.parser')

        # 解析商品列表
        '''
        <div class="goods-list-v2 gl-type-1 J-goods-list" id="J_goodsList">
         <ul class="gl-warp clearfix" data-tpl="1">
          <li class="gl-item" data-sku="3521615">
           <div class="gl-i-wrap">
            <div class="p-img">
             <a href="//item.jd.com/3521615.html" onclick="searchlog(1,3521615,0,2,'','flagsClk=1614811784')" target="_blank" title="【杜杜春节不打烊！】新春特惠，限时低价！戳入会场享更多优惠！">
              <img class="" data-img="1" data-lazy-img="done" height="220" source-data-lazy-img="" src="//img10.360buyimg.com/n7/jfs/t1/90763/31/10918/278051/5e240f0fE3309a556/3c72ea48e9cf8ea0.jpg" width="220"/>
             </a>
             <div class="picon" data-catid="1502" data-done="1" data-lease="" data-presale="" data-venid="1000001462" style="background:url(//img30.360buyimg.com/jgsq-productsoa/jfs/t1/108472/40/3021/3997/5e0c7527Ea65f0ceb/64344882b9a8d89b.png) no-repeat 0 0;_background-image:none;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//img30.360buyimg.com/jgsq-productsoa/jfs/t1/108472/40/3021/3997/5e0c7527Ea65f0ceb/64344882b9a8d89b.png',sizingMethod='noscale');">
             </div>
            </div>
            <div class="p-price">
             <strong class="J_3521615" data-done="1">
              <em>
               ￥
              </em>
              <i>
               59.00
              </i>
             </strong>
             <span class="price-plus-1" title="PLUS会员专享价">
              <em>
               ￥56.90
              </em>
              <i>
              </i>
             </span>
            </div>
            <div class="p-name p-name-type-2">
             <a href="//item.jd.com/3521615.html" onclick="searchlog(1,3521615,0,1,'','flagsClk=1614811784')" target="_blank" title="【杜杜春节不打烊！】新春特惠，限时低价！戳入会场享更多优惠！">
              <em>
               <img class="p-tag3" src="//img14.360buyimg.com/uba/jfs/t6919/268/501386350/1257/92e5fb39/5976fcf9Nd915775f.png"/>
               杜蕾斯
               <font class="skcolor_ljg">
                避孕套
               </font>
               安全套 超薄尊享三合一18 超薄润滑 成人用品 男用套套(超薄10＋倍滑超薄4+紧型超薄4) Durex
              </em>
              <i class="promo-words" id="J_AD_3521615">
               【杜杜春节不打烊！】新春特惠，限时低价！戳入会场享更多优惠！
              </i>
             </a>
            </div>
            <div class="p-commit" data-done="1">
             <strong>
              <a href="//item.jd.com/3521615.html#comment" id="J_comment_3521615" onclick="searchlog(1,3521615,0,3,'','flagsClk=1614811784')" target="_blank">
               470万+
              </a>
              条评价
             </strong>
            </div>
            <div class="p-shop" data-done="1" data-dongdong="" data-reputation="99" data-score="5" data-selfware="1">
             <span class="J_im_icon">
              <a class="curr-shop hd-shopname" href="//mall.jd.com/index-1000001462.html" onclick="searchlog(1,1000001462,0,58)" target="_blank" title="durex杜蕾斯京东自营官方旗舰店">
               durex杜蕾斯京东自营官方旗舰店
              </a>
              <b class="im-02" onclick="searchlog(1,1000001462,0,61)" style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;" title="联系客服">
              </b>
             </span>
            </div>
            <div class="p-icons" data-done="1" id="J_pro_3521615">
             <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1" data-tips="京东自营，品质保障">
              自营
             </i>
             <i class="goods-icons4 J-picon-tips" data-tips="购买本商品送赠品">
              赠
             </i>
            </div>
            <div class="p-operate">
             <a class="p-o-btn contrast J_contrast" data-sku="3521615" href="javascript:;" onclick="searchlog(1,3521615,0,6,'','flagsClk=1614811784')">
              <i>
              </i>
              对比
             </a>
             <a class="p-o-btn focus J_focus" data-sku="3521615" href="javascript:;" onclick="searchlog(1,3521615,0,5,'','flagsClk=1614811784')">
              <i>
              </i>
              关注
             </a>
             <a class="p-o-btn addcart" data-limit="0" href="//cart.jd.com/gate.action?pid=3521615&amp;pcount=1&amp;ptype=1" onclick="searchlog(1,3521615,0,4,'','flagsClk=1614811784')" target="_blank">
              <i>
              </i>
              加入购物车
             </a>
            </div>
           </div>
          </li>
         </ul>
         <span class="clr">
         </span>
        </div>
        '''
        for item_li in soup.find_all('li',class_='gl-item'):
            # 详情链接
            item_detail = item_li.find('a')
            item_detail_url = 'https:%s' % item_detail['href']

            # 封面图片链接
            item_img = item_li.find('img')
            item_img_url = 'https:%s' % item_img['source-data-lazy-img']

            # 普通价格
            item_normal_price = item_li.find('strong')
            item_normal_price_text = item_normal_price.get_text()

            # 标题描述
            item_title = item_li.find('div',class_='p-name p-name-type-2').find('em')
            item_title_text = item_title.get_text()

            # 下载图片
            download_cover(item_img_url)

            # 访问商品详情
            visit_item_detail(item_detail_url)

            print(f'商品详情: {item_detail_url} 商品图片: {item_img_url} 普通价格: {item_normal_price_text} 标题描述: {item_title_text}')
    except Exception as e:
        print('解析商品异常',e)

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

def batch_get_comment(productId):
    '''
    批量分页搜索京东商品
    '''
    comment_txt_name = './comment/%s.txt' % productId
    if os.path.exists(comment_txt_name):
        os.remove(comment_txt_name)
    for i in range(100):
        get_comment(productId,page=i)

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

def download_cover(url):
    '''
    下载商品封面图
    '''
    try:
        # 下载图片
        response = requests.get(url)
        response.raise_for_status()
        response_content = response.content
        img_name = os.path.basename(url)
        with open('./cover/%s' % img_name, 'wb') as wbf:
            wbf.write(response_content)
    except Exception as e:
        print('下载商品异常')


def main():
    batch_search_item('充气娃娃')

if __name__ == '__main__':
    main()
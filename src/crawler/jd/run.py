# -*- coding: utf-8 -*-
import requests

def search_item(keyword='充气娃娃'):
    '''
    根据关键字搜索京东商品,默认搜索'充气娃娃'.
    '''
    try:
        url = 'https://search.jd.com/Search'
        params = {
            'keyword': keyword,
            'enc': 'utf-8',
            'wq': keyword,
            'pvid':'cc0ea522e3404a07bae40b721ca4a603'
        }
        headers = {
            'referer': 'https://www.jd.com/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        response = requests.get(url=url, params=params, headers=headers)
        response.raise_for_status()
        response.encoding = 'utf-8'

        response_text = response.text
        print(response_text)
    except:
        print('搜索商品异常')

def main():
    search_item('充气娃娃')

if __name__ == '__main__':
    main()
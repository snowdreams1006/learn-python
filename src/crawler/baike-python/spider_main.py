# -*- coding: utf-8 -*-
from baike-python import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object);
    def __init__(self):
        self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url);
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.download(new_url)


def main():
    # 入口 url
    root_url = 'https://baike.baidu.com/item/Python/407313'
    spider = SpiderMain()
    spider.craw(root_url)

if __name__ == '__main__':
    main()
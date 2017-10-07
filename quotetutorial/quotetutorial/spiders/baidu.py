# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def __init__(self, category=None, *args, **kwargs):
        super(BaiduSpider, self).__init__(*args, **kwargs)
        self.category = category

    def parse(self, response):
        self.logger.info(self.category)

    def parse_index(self, response):
        print('BaiDu', response.status)
        self.logger.info(response.status)

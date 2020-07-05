# -*- coding: utf-8 -*-
import scrapy
import pretty_errors

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    # 这网站会显示你请求的ip地址
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        # pass
        print(response.text)

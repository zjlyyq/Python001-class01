# -*- coding: utf-8 -*-
import scrapy


class ProxyipSpider(scrapy.Spider):
    name = 'proxyip'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(response.text)
        # pass

# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from homework.items import HomeworkItem
import pandas as pd
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']


    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        items = []
        items.append({"name": "电影名", "actors": "主演", "date": "发行时间", "movie_type": "类型"})
        # print(response.text)
        moviesxpath = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        moviesxpath = moviesxpath[:10]
        for movie in moviesxpath:
            item = HomeworkItem()
            infos = movie.xpath('./div[contains(@class, "movie-hover-title")]')
            name = infos[0].xpath('./span[contains(@class, "name ")]/text()')[0].extract()
            movietype = infos[1].xpath('./text()')[1].extract().strip()
            actors = infos[2].xpath('./text()')[1].extract().strip()
            date = infos[3].xpath('./text()')[1].extract().strip()
            # print(movietype)
            item['name'] = name 
            item['movie_type'] = movietype
            item['actors'] = actors
            item['date'] = date
            # print(item)
            items.append(item)
        print(items)
        movietable = pd.DataFrame(data = items)
        # windows需要使用gbk字符集
        movietable.to_csv('./maoyan_homework.csv', encoding='utf8', index=False, header=False)
        return items



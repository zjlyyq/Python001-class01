import scrapy
from bs4 import BeautifulSoup as bs
from first_scrapy_project.items import FirstScrapyProjectItem
class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']


    def start_requests(self):
        for i in range(1):
            url = f'https://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url=url, callback=self.parse)

            
    # def parse(self, response):
    #     pass

    def parse(self, response):
        items = []
        bs_info = bs(response.text, 'html.parser')
        for div_tag in bs_info.find_all('div', attrs={"class": "hd"}):
            # print('共有电影' + str(len(div_tag)) + "部")
            for a_tag in div_tag.find_all('a'):
                item = FirstScrapyProjectItem()
                # 获取电影链接
                link = a_tag.get('href')
                # # 获取a标签下第一个span——电影名
                title = a_tag.find('span',).text
                item['title'] = title
                item['link'] = link
                yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
        # return items

    # 处理电影详情页面返回
    def parse2(self, response):
        item = response.meta['item']
        bs_detail_info = bs(response.text, 'html.parser')
        content = bs_detail_info.find('div', attrs={'class': 'related-info'}).get_text().strip()
        item['content'] = content
        yield item



import scrapy
# from first_scrapy_project.items import FirstScrapyProjectItem
from  scrapy.selector import Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']


    def start_requests(self):
        for i in range(1):
            print(i)
            url = f'https://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)



    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="hd"]')
        for movie in movies:
            # 路径使用 / .  .. 不同的含义　
            title = movie.xpath('./a/span/text()')
            link = movie.xpath('./a/@href')
            print(title)
            print(link)
            print(title.extract())
            print(link.extract())
            print(title.extract_first())
            print(link.extract_first())
            print(title.extract_first().strip())
            print(link.extract_first().strip())
        

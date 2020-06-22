import requests
import lxml.etree

# 电影详情地址
detail_url = "https://movie.douban.com/subject/1291546/"

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {}
header['user-agent'] = user_agent
response = requests.get(detail_url, headers=header)

# xml处理
selector = lxml.etree.HTML(response.text)
# print(selector)

# 电影
filmname = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
# 上映日期
releasedate = selector.xpath('//*[@id="info"]/span[11]/text()')
# rating 
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
movieinfo = [filmname, releasedate, rating]
print(movieinfo)
import pandas as pd
movie1 = pd.DataFrame(data = movieinfo)
# windows需要使用gbk字符集
movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)

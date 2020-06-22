import requests
from bs4 import BeautifulSoup as bs
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent':user_agent}

url = "https://movie.douban.com/top250"

responsed = requests.get(url, headers=header)
bs_info = bs(responsed.text, 'html.parser')

# print(responsed.text)
# print(responsed.status_code)

for div_tag in bs_info.find_all('div', attrs={"class": "hd"}):
    # print('共有电影' + str(len(div_tag)) + "部")
    for a_tag in div_tag.find_all('a'):
        print(a_tag.get('href'))
        # 获取a标签下第一个span——电影名
        print(a_tag.find('span',).text)
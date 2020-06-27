import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://maoyan.com/films?showType=3'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent':user_agent}
header['cookie'] = 'uuid_n_v=v1; uuid=DBBF8080B84B11EAA2F937AFDFBC83F6E3D6500DF3334AB688D90E995F4FF5B9; _csrf=414bcb23617f9f8a1b66b28cae1da336fdc919f8fa8c45112a5ac5d3336e2c06; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593244647; _lxsdk_cuid=172f4c7fca6c8-0b3b8d4aeedb8b-143f6257-13c680-172f4c7fca6c8; _lxsdk=DBBF8080B84B11EAA2F937AFDFBC83F6E3D6500DF3334AB688D90E995F4FF5B9; mojo-uuid=bd3c15ae11ee359cae6c7c6c2f4fe5e5; mojo-session-id={"id":"26646d636d55c8f70534cd9d2e034b49","time":1593247366288}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593247445; __mta=147593096.1593244647388.1593247366993.1593247445259.3; _lxsdk_s=172f4c7fca8-670-919-7cb%7C%7C11'
response = requests.get(url, headers=header)

# print(response.text)
bs_info = bs(response.text, 'html.parser')

movies_info = bs_info.find_all('div', attrs={"class": "movie-item-hover"})
movies = []
for info in movies_info:
    movie = {}
    movie_name = info.find('span', attrs={'class': 'name'}).text
    print(f'电影名：{movie_name}')
    movie['name'] = movie_name
    other =  info.find_all('div', attrs={"class": "movie-hover-title"}) 
    movie['type'] = other[1].text.rstrip("\n")
    movie['actors'] = other[2].text.rstrip("\n")
    movie['date'] = other[3].text.rstrip("\n")
    movies.append(movie)
    if len(movies) > 9:
        break

print(movies)

movietable = pd.DataFrame(data = movies)
# windows需要使用gbk字符集
movietable.to_csv('./maoyan.csv', encoding='utf8', index=False, header=False)
    


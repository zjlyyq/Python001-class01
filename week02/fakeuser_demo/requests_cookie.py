import requests
import pretty_errors
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://accounts.douban.com/passport/login?source=book'
}
print(headers)
# 在同一个 Session 实例发出的所有请求之间保持 cookie
# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie，
# 期间使用 urllib3 的 connection pooling 功能。
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
s = requests.Session()

login_url = 'https://accounts.douban.com/j/mobile/login/basic'

form_data = {
    'ck': '',
    'name': '2868986985@qq.com',
    'password': '123456',
    'remember': 'false',
    'ticket': ''
}

r = s.post(login_url, data=form_data, headers=headers)
print(r.text)

from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
# 模拟不同的浏览器
print(ua.chrome)
print(ua.safari)

# 随机返回头部信息
print(ua.random)
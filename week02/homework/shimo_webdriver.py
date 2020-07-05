from selenium import webdriver
import pretty_errors
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/login?from=home')
    # 获取用户名输入区域
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('you phone')
    time.sleep(1)
    # 获取密码输入区域
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('you passwd')
    time.sleep(1)
    # 获取登陆按钮
    login_bt = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')
    login_bt.click()
    time.sleep(3)
except Exception as e:
    print(e)
    pass
finally:
    browser.close()
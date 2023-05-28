"""示例代码一：使用 selenium+浏览器 打开百度"""

from selenium import webdriver
import time

# 创建浏览器对象
_ = webdriver.ChromeOptions()
_.add_argument("--start-maximized")
driver = webdriver.Chrome(options=_)
driver.get('http://www.baidu.com/')
# 5秒钟后关闭浏览器
time.sleep(5)
driver.quit()

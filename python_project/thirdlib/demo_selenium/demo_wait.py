"""
元素等待
概念
· 显示等待是针对某一个元素进行相关等待判定；
· 隐式等待不针对某一个元素进行等待，全局元素等待。只能判断元素是否可见
a.相关模块
WebDriverWait 显示等待针对元素必用
expected_conditions 预期条件类（里面包含方法可以调用，用于显示等待）
NoSuchElementException 用于隐式等待抛出异常
By 用于元素定位
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait		    #注意字母大写
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
"""
from time import sleep, ctime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# 显示等待
# 案例：检测百度页面搜索按钮是否存在，存在就输入关键词“自学网 Selenium” 然后点击搜索
_ = webdriver.ChromeOptions()
_.add_argument("--start-maximized")
driver = webdriver.Chrome(options=_)

driver.get("http://www.baidu.com")

driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("自学网 Selenium")
sleep(2)

# 显示等待--判断搜索按钮是否存在
element = WebDriverWait(driver, 5, 0.5).until(ec.presence_of_element_located((By.ID, "su")))
element.click()
sleep(3)

input("继续")

# 隐式等待
driver.get("http://www.baidu.com")
driver.implicitly_wait(5)  # 隐式等待时间设定 5秒
# 检测搜索框是否存在
try:
    print(ctime())
    driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("Python")
    driver.find_element(By.CSS_SELECTOR, "#su").click()
except ec.NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())

input("结束")
driver.quit()

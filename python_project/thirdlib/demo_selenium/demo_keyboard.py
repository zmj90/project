"""
node.send_keys(Keys.SPACE)
node.send_keys(Keys.CONTROL, 'a')
node.send_keys(Keys.CONTROL, 'c')
node.send_keys(Keys.CONTROL, 'v')
node.send_keys(Keys.ENTER)
# 案例： 在百度搜索关键词“Python” 然后将关键词复制或剪切到搜狗搜索框进行搜索
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

_ = webdriver.ChromeOptions()
_.add_argument("--start-maximized")
driver = webdriver.Chrome(options=_)

driver.get("http://www.baidu.com")
driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("Python")

time.sleep(2)
# 键盘全选操作 Ctrl+A
driver.find_element(By.CSS_SELECTOR, "#kw").send_keys(webdriver.Keys.CONTROL, 'a')

# 键盘选择复制或剪切操作 Ctrl+C
driver.find_element(By.CSS_SELECTOR, "#kw").send_keys(webdriver.Keys.CONTROL, 'c')
driver.find_element(By.CSS_SELECTOR, "#kw").send_keys(webdriver.Keys.CONTROL, 'x')

# 打开搜狗页面
driver.get("http://www.sogou.com/")
time.sleep(2)

# 粘贴复制内容
driver.find_element(By.CSS_SELECTOR, ".sec-input").send_keys(webdriver.Keys.CONTROL, 'v')
time.sleep(2)

# 点击搜索按钮
# driver.find_element_by_xpath("//input[@id='stb']").click()
driver.find_element(By.CSS_SELECTOR, "#stb").click()

input("结束符：")
driver.quit()

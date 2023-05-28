"""示例代码二：打开百度，搜索赵丽颖，点击搜索，查看"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

# 1.创建浏览器对象 - 已经打开了浏览器
_ = webdriver.ChromeOptions()
_.add_argument("--start-maximized")
driver = webdriver.Chrome(options=_)
# 2.输入: http://www.baidu.com/
driver.get('http://www.baidu.com/')
# 3.找到搜索框,向这个节点发送文字: 赵丽颖
# driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('赵丽颖')
# ele = driver.find_elements(By.XPATH, '//*[@id="kw1"]')
r = WebDriverWait(driver, 5).until_not(ec.presence_of_element_located((By.XPATH, '//*[@id="kw1"]')))
print(r)

# 4.找到 百度一下 按钮,点击一下
# driver.find_element(By.XPATH, '//*[@id="su"]').click()

input("退出：")
driver.quit()

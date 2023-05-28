import time

from selenium import webdriver
from selenium.webdriver.common.by import By

_ = webdriver.ChromeOptions()
_.add_argument("--start-maximized")
driver = webdriver.Chrome(options=_)

driver.get("https://ke.qq.com/")

# 方式1
# target = driver.find_element(By.XPATH, "//h3[text()='为你推荐']")
# 将该模块与浏览器顶部对齐
# driver.execute_script('arguments[0].scrollIntoView();', target)
# 将该模块与浏览器底部对齐
# driver.execute_script('arguments[0].scrollIntoView(false);', target)

# 方式2
# 滚动到页面最底部
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(3)
# 滚动到页面最顶部
# driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

# 方式3
# 将滚动调拖到最底部
# driver.execute_script("var action=document.documentElement.scrollTop=10000")
# time.sleep(3)
# 将滚动条拖到最顶部
# driver.execute_script("var action=document.documentElement.scrollTop=0")

# 方式4
# 滚动到页面最底部
driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
time.sleep(3)
# 滚动到页面最顶部
driver.execute_script("window.scrollTo(document.documentElement.scrollHeight,0)")



input("结束符：")
driver.quit()





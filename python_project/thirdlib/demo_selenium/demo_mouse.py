from selenium import webdriver
from selenium.webdriver.common.by import By

_ = webdriver.ChromeOptions()
_.add_argument("--start-maximized")
driver = webdriver.Chrome(options=_)
driver.get("https://www.baidu.com/")

ele_set = driver.find_element(By.XPATH, "//span[text()='设置']")
webdriver.ActionChains(driver).move_to_element(ele_set).perform()

# 单击，弹出的Ajax元素，根据链接节点的文本内容查找
driver.find_element(By.LINK_TEXT, '高级搜索').click()





input("结束符：")
driver.quit()

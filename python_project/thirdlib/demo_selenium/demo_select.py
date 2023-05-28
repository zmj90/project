import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://cdn2.byhy.net/files/selenium/test2.html")
handles1 = driver.current_window_handle
print(id(handles1), type(handles1), handles1)

e1 = driver.find_element(By.CSS_SELECTOR, "#s_radio>input[checked]")
r1 = e1.get_attribute("value")
print(id(r1), type(r1), r1)

driver.find_element(By.CSS_SELECTOR, "#s_radio>input[value='小雷老师']").click()

e2 = driver.find_element(By.ID, "ss_single")
s1 = Select(e2)
s1.select_by_index(0)

time.sleep(6)
driver.quit()

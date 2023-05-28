from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def demo_id_and_name():
    _ = webdriver.ChromeOptions()
    _.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=_)
    driver.get("http://www.baidu.com")

    driver.find_element(By.ID, "kw").send_keys("Selenium我要自学网")
    driver.find_element(By.NAME, "wd").send_keys("Selenium我要自学网")

    sleep(2)
    driver.find_element(By.ID, "su").click()
    driver.close()


def demo_tag_name():
    # 案例：打开我要自学网页面，在用户名输入框输入用户名“selenium”
    _ = webdriver.ChromeOptions()
    _.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=_)
    driver.get("http://www.51zxw.com")
    # 定位标签名为input的元素
    driver.find_element(By.TAG_NAME, "input").send_keys("selenium")
    # 获取页面所有标签名称为“input”的标签。
    driver.find_elements(By.TAG_NAME, "input")[0].send_keys("selenium")
    sleep(3)
    driver.quit()


def demo_class_name():
    # 根据标签中属性class来进行定位的一种方法
    _ = webdriver.ChromeOptions()
    _.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=_)
    driver.get("http://www.baidu.com")
    driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("Selenium 我要自学网")
    sleep(2)
    driver.find_element(By.ID, "su").click()
    sleep(3)
    driver.quit()


def demo_link():
    # link_text定位就是根据超链接文字进行定位。
    _ = webdriver.ChromeOptions()
    _.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=_)
    driver.get("http://www.51zxw.net/")
    driver.find_element(By.LINK_TEXT, '程序设计').click()
    sleep(3)
    driver.find_element(By.PARTIAL_LINK_TEXT, '数据库教程').click()
    sleep(3)
    driver.quit()


if __name__ == '__main__':
    # demo_id_and_name()
    # demo_tag_name()
    # demo_class_name()
    demo_link()

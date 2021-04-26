from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")

# driver.find_element_by_id('kw').send_keys("weather")
# driver.find_element_by_id('su').click()

wb = webdriver.Chrome()
wb.get("https://www.baidu.com")
wb.find_element_by_id("kw").send_keys("china")
wb.find_element_by_id("su").click()

# wd.find_element_by_css_selector("ss").send_keys(Keys.CONTROL,)

time.sleep(3)

wb.close()

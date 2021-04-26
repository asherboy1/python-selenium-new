from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select #导入select类

wd = webdriver.Chrome()
wd.get("http://cdn1.python3.vip/files/selenium/test2.html")
wd.implicitly_wait(5)

select = Select(wd.find_element_by_css_selector("#ss_multi"))

select.deselect_all()       #所有选项清除
time.sleep(2)

select.select_by_index(0)
time.sleep(2)

select.select_by_index(1)
time.sleep(2)

select.deselect_all()

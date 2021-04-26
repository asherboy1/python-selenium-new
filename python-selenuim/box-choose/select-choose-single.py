from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select #导入select类

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/test2.html")
wd.implicitly_wait(5)

#select 为 select标签  select option 以用select类封装

element = Select(wd.find_element_by_css_selector('#ss_single')) #创建Select对象 选择到select对象

# 选择方式:

#1.按照次序 select_by_index 根据选项次序选择(从0开始)
element.select_by_index(0)
time.sleep(2)

#2.按照可见文本 select_by_visible_text
element.select_by_visible_text("小雷老师")
time.sleep(2)

#3.按照属性中value select_by_value
element.select_by_value("小江老师")
time.sleep(2)

#去选中方式：
# 1.按照次序 deselect_by_index

# 2.按照可见文本 deselect_by_visible_text

# 3.按照属性中value deselect_by_value

# 4.常用 deselect_all 全部去选中

element.deselect_all()
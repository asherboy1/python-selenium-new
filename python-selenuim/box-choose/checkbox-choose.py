from selenium import webdriver
import time

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/test2.html")
wd.implicitly_wait(5)

#checkbox 多选框

#思路 : 先把已经选中的对象全部点击一下 确保为未选状态  已选中对象特征属性 checked="checked"
#再次选择所需选择对象

elements = wd.find_elements_by_css_selector('#s_checkbox input[checked="checked"]')
for element in elements:
    element.click()

element = wd.find_element_by_css_selector('#s_checkbox input[value="小江老师"]')
element.click()

print(element.get_attribute("outerHTML"))
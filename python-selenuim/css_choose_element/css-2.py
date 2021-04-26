from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")
wd.implicitly_wait(5)
#选择 子元素 和 后代元素  后代元素 只要在内部 就算

#子元素----------------------------------
#元素1 > 元素2  直接子元素 最终选择元素2
#元素1 > 元素2 > 元素3 > 元素4 最终选择 元素4

#后代元素---------------------------------
#元素1 元素2 空格隔开 选择的只要是后代几个 可以之间隔多层

#后代 与 子元素可混用 例如 元素1 元素2 > 元素3  就是在元素1中的后代子元素2中 选择在元素2中的直接子元素 元素3

element = wd.find_element_by_css_selector('#container #inner11')        # id 前跟# 
element = wd.find_element_by_css_selector('#container > div > div')     # tag名直接输入 
element = wd.find_element_by_css_selector('#bottom .date')              # css 或 class名 前面加.

print(element.text)

elements = wd.find_elements_by_css_selector('#bottom div')
for element in elements:
    print("----------")
    print(element.get_attribute("outerHTML"))

elements = wd.find_elements_by_css_selector('.animal span')

for element in elements:
    print("----------")
    print(element.get_attribute("outerHTML"))

    
wd.quit()
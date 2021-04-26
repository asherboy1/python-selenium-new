from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")


#css .class 属性 例子 .animal{} {}中为修饰语句  
#color background-color

#find_element_by_css_selector(CSS Selector参数)  主流使用

element = wd.find_element_by_css_selector('.animal') 
 #注意 . 表示使用的哪一个 如果没有. 等效于 wd.find_element_by_tag_name("animal")

element1 = wd.find_element_by_css_selector('#searchtext')  
#注意 此句使用# 表示通过id查找 等效于 wd.find_element_by_id('serachtext')


print(element1.get_attribute('outerHTML'))


print(element.get_attribute('outerHTML'))
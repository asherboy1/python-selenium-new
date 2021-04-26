from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/test1.html")

wd.implicitly_wait(10)

#在xpath中 可以使用 逻辑判断方法 and or
# //*[@class="multi_choice" or @class="single_choice"]

#寻求父节点 /..   //p[@id="b1"]/..  表示元素为p 属性中id为b1 的父节点

#寻找兄弟节点 following-sibling::   
# //*[@class="multi_choice"]/following-sibling::*   表示class为 multi_choice 的所有兄弟节点
# //*[@class="multi_choice"]/following-sibling::span  表示class为 multi_choice 中 tag名为span兄弟节点
# //h4/following-sibling::select[@class="single_choice"]

#preceding-sibling::  可选择父节点的兄弟节点 
# //*[@class="single_choice"]/preceding-sibling::h4

#一般通过wd对象进行全局查找
#如果以element为对象 查找时需加. 使其在element中使用xpath查找

china = wd.find_element_by_id("china")

elements = china.find_elements_by_xpath(".//p")  #注意.  没有. 表示还是从全局查找
for element in elements:
    print(element.get_attribute("innerHTML"))

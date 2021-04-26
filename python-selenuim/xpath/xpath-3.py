from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/test1.html")

wd.implicitly_wait(10)

elements = wd.find_elements_by_xpath('//p[2]')  #p类型的第二个元素 等价于 css中 p:nth-of-type(2)

for element in elements:
    print(element.get_attribute("innerHTML"))

elements = wd.find_elements_by_xpath('//div/*[2]') #所有以tag名为div 为父节点的所有第二个子节点 
for element in elements:
    print(element.get_attribute("innerHTML"))

elements = wd.find_elements_by_xpath('//div/*[last() - 1]')  #last() 本身表示倒数第一 -1 则为倒数第二
for element in elements:
    print(element.get_attribute("innerHTML"))

#与css 新功能 position() 根据范围选择

elements = wd.find_elements_by_xpath('//option[position()<=2]')     #可获取最新信息 最新两个  
for element in elements:
    print(element.get_attribute("innerHTML"))

# 同样也可以使用 last()  //option[position()>=last()-1]  表示最后两个 灵活运用
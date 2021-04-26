#appium 唯一支持xpath 
#与css 择优选择

#xpath 明确 上下结构

from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/test1.html")

wd.implicitly_wait(10)

element = wd.find_element_by_xpath('/html/body/div') # 从根节点写 类似于绝对路径 /表示直接子节点
print(element.get_attribute('innerHTML'))

element = wd.find_element_by_xpath('//div/p')    #相对路径 // 表示不管在文档的什么位置 相当于css中 直接俄使用tag名寻找
print(element.get_attribute('innerHTML'))

# //div/* *为通配符 为div中所有的内容
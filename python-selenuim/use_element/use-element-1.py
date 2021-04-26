from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://www.baidu.com")

wd.implicitly_wait(10)

wd.find_element_by_id("kw").send_keys("taobao")     # send_ key 输入文本
element = wd.find_element_by_id("su")
element.click()     # click 点击 元素操作

element = wd.find_element_by_id('1')

print(element.text)     # text 获取 >< 中的文本信息

print(element.get_attribute("srcid"))       # get_attribute  获取元素 中 属性内容 (同级)

element = element.find_element_by_tag_name("a")
print(element.get_attribute("href"))

print(element.get_attribute('outerHTML'))       #get_attribute('outerHTML')获取 当前元素整个的html  1.测试中对于错误的数据收集 2.静态文本分析

print("----------------")

print(element.get_attribute("innerHTML"))       #get_attribute("innerHTML") 获取 当前元素中 内部的html

#当遇到input的输入框 需用 value 获取其中的值  get_attribute("value")

#当有些界面内容无法获取text   可以使用 get_attribute("innerText") 获取

wd.quit()   #关闭窗口与驱动


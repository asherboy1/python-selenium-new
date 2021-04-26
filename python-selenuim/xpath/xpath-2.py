from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/test1.html")

wd.implicitly_wait(10)

element = wd.find_element_by_xpath('//*[@id="west"]')  #表示所有属性中 id为west的 注意用法 @  类似于css中[id="west"]
#//p[@class="west"] tag名为p下属性class为west 类似于 css中 p .west
#所有属性用@ 表示
print(element.get_attribute('innerHTML'))

#可使用 contains 包含  //p[contains(@class,"xxx")]/input  在tag名为p下 class包含xxx中的input 元素

elements = wd.find_elements_by_xpath('//p[contains(@class,"huge")]')

for element in elements:
    print(element.text)

#startwith(@class,"xxx") 以xxx开头
#endwith(@class,"xxx") 以xxx结尾

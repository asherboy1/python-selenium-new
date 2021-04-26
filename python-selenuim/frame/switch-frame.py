from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/sample2.html")
wd.implicitly_wait(5)

#如果有嵌入在网页里面的html 需先切换至 被嵌入的文档中 wd.switch_to.frame(frame_reference)
# frame_reference 可以是 frame 元素的属性 name 或者 ID 

# wd.switch_to_frame('frame1')

#如果无name 或 id  利用寻找frame目标
wd.switch_to_frame(wd.find_element_by_css_selector('iframe[src="sample1.html"]'))

elements = wd.find_elements_by_css_selector('.animal')

for element in elements:
    print('----')
    print(element.get_attribute('innerHTML'))


#切换到外层框架
wd.switch_to_default_content()

wd.find_element_by_id('outerbutton').click()

wd.quit()



from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")
wd.implicitly_wait(5)

elements = wd.find_elements_by_css_selector('.plant,.animal')       #多条件选择 中间加,分隔

for element in elements:
    print("---------------")
    print(element.text)




wd.quit()
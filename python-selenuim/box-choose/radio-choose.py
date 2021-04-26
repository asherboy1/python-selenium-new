from selenium import webdriver
import time

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/test2.html")
wd.implicitly_wait(5)

#checked 为默认选择的值
#radio 单选
wd.find_element_by_css_selector('#s_radio [type="radio"]').click()
time.sleep(3)
wd.find_element_by_css_selector('#s_radio [value="小雷老师"]').click()

elements = wd.find_elements_by_css_selector('#s_radio input')
for element in elements:
    element.click()
    print(element.get_attribute('value'))
    time.sleep(1)

# wd.quit()
from selenium import webdriver
import time
wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/test4.html")

wd.implicitly_wait(10)

#alert 弹出警告 confirm 确认 prompt 提供信息

#alert
wd.find_element_by_css_selector('#b1').click()
print(wd.switch_to.alert.text)      #获取alter弹出的文本信息 wd.switch_to.alter.text
time.sleep(2)

wd.switch_to.alert.accept()     #确认信息 wd.switch_to.alter.accept()

#confirm
wd.find_element_by_css_selector('#b2').click()
print(wd.switch_to.alert.text)      #confirm 获取alter弹出框与 确认信息 与 alter一致
time.sleep(2)

wd.switch_to.alert.accept()

wd.find_element_by_css_selector('#b2').click()
wd.switch_to.alert.dismiss()        #相当于点击了取消
time.sleep(2)

#prompt
#获取文本 确认信息 取消 与前面一致

#输入信息

wd.find_element_by_css_selector('#b3').click()
pm = wd.switch_to.alert     #可储存在一个变量中
pm.send_keys("python!")
pm.accept()
pm.dismiss()

time.sleep(2)






wd.quit()
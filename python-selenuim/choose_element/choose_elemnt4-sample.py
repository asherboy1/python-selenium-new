from selenium import webdriver
import time

wd = webdriver.Chrome()
wd.get("http://www.baidu.com")

wd.implicitly_wait(10)   #重要! 隐式等待时间  对于那些 find 的语句 每过半秒 都会再去查找元素 在10s内直到元素查到找 并不会直接抛出错误

wd.find_element_by_id("kw").send_keys("taobao")
wd.find_element_by_id("su").click()

# time.sleep(3)       #注意响应的速度问题 程序很快 但服务器会需要时间去响应

id_1 = wd.find_element_by_id("1")       #如果为 elements 会返回空列表
print(id_1.text)
id_1.find_element_by_tag_name("a").click()

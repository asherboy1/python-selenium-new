from selenium import webdriver

wd = webdriver.Chrome()
wd.get("http://www.baidu.com")

#find_elemnet_by_id  返回对象为element对象------------ 可通过返回的对象 对其进行操作
element = wd.find_element_by_id("kw")
element.send_keys("lol\n")      # \n代表回车

# send_keys() 发送内容---------------
wd.find_element_by_id("kw").send_keys("date")       #选择元素  根据id选择对应元素  id在本页面 唯一    

wd.find_element_by_id("su").click()         #元素常用操作 输入 点击 传值 悬停 滚动  重点在与如何找到所需元素



from selenium import webdriver
from selenium.webdriver import ActionChains  #导入模块 高级动作

wd = webdriver.Chrome()
wd.get("http://www.baidu.com")

wd.implicitly_wait(5)



# element = wd.find_element_by_css_selector('[href = "http://www.baidu.com/more/"]')

# #ActionChains(wd) 初始化对象    .perform() 提交所有ActionChains类中存储的行为
# ActionChains(wd).move_to_element(element).perform()   

ac = ActionChains(wd)       #实例化ac   
ac.move_to_element(
    wd.find_element_by_css_selector('[href="http://www.baidu.com/more/"]')
).perform()     #别忘了 perfrom!

# 鼠标常用操作： ac.context_click() 右击 ac.double_click() 双击  ac.drag_and_drop() 拖动  ac.move_to_element() 移动至


#冻结页面 实用 js代码 网页console中 执行 setTimeout(function(){debugger}, 5000)  表示5s后 冻结

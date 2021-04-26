from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://www.baidu.com")

wd.implicitly_wait(10)

wd.get_window_size()       #获取窗口大小
wd.set_window_size(1280,960)        #自定义窗口大小

print(wd.current_url)       #获取当前url

wd.get_screenshot_as_file('1.png')      #截图并保存为
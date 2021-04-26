from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/sample3.html")
wd.implicitly_wait(5)

print(wd.title)     #.title会返回当前控制页面的标题

#切换到新窗口 wd.switch_to.window(handle)  handle 句柄 窗口的id  
# WebDriver对象有window_handles 属性，这是一个列表对象， 里面包括了当前浏览器里面所有的窗口句柄。

wd.find_element_by_css_selector('a[href]').click()


mainhandle = wd.current_window_handle        #用于记录保存 当前原始窗口句柄

#根据每一个handle 查找并切换 当发现 Bing在现在的title中时 就跳出  这样既可操作新的所需要操作的窗口
for handle in wd.window_handles:
    #1.
    # wd.switch_to_window(handle)
    # if 'Bing' in wd.title:
    #     break

    #2.
    if handle != mainhandle:
        wd.switch_to_window(handle)
        break


    
print(wd.title)

#如果想要切换回原窗口  就可利用所记录的原始窗口的句柄
wd.switch_to_window(mainhandle)
print(wd.title)

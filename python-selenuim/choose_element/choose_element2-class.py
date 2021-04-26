from selenium import webdriver

wb = webdriver.Chrome()
wb.get("http://cdn1.python3.vip/files/selenium/sample1.html")

# wb.find_element_by_class_name()  选择一个对应的class_name的元素

# element = wb.find_element_by_class_name("animal")       #仅会返回第一个 注意 find_element 与 find_elements 区别
# print(element.text)


elements = wb.find_elements_by_class_name("plant")  #选择多个对应的class_name的元素  元素返回以列表形式

for element in elements:
    print(element.text)         #.text 得出element中文本

# try:        #可使用 抛出异常 是否来寻找到对应元素
#     test = wb.find_element_by_class_name("77")  
# except:
#     print("77 not in class")
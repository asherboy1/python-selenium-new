from selenium import webdriver

wb = webdriver.Chrome()
wb.get("http://cdn1.python3.vip/files/selenium/sample1.html")


#根据对应需求 选择寻找元素的方式 
elements = wb.find_elements_by_tag_name("span")  #tag根据标签寻找 span为一个标签 
for element in elements:
    print(element.text)

# 当以wb为对象进行查找 查找作用对象为整个网页
# 也可以让 返回的element为对象 这样其作用域仅为目前这个对象的内部
#例如:

print("------------")
id_test = wb.find_element_by_id("container")

# print(id_test.text)     #也会直接显示最底层文本内容
# print("------------")

spans = id_test.find_elements_by_tag_name("span")       #从id_test对象 中 选择寻找对象 

for span in spans:
    print(span.text)

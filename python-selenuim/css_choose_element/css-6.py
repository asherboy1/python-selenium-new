from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/sample1b.html")
wd.implicitly_wait(5)

#按次序选择子节点 :nth-child(num) 父节点的第num个子节点 可在:前加上限定

elements = wd.find_elements_by_css_selector('span:nth-child(2)')  #子元素tag名为span 且为 父元素的第二个子节点
                                    # #t2 :nth-child(2)   id为t2 中第二个子节点 组合 (注意空格 含义不一样)

for element in elements:
    print('------------1')
    print(element.get_attribute('outerHTML'))

#按次序倒着选择子节点 :nth-last-child(num) 父节点的倒数第num个子节点 可在:前加上限定

elements = wd.find_elements_by_css_selector('p:nth-last-child(1)')
for element in elements:
    print('------------2')
    print(element.get_attribute('outerHTML'))

#父元素的第几个 某类型 的子节点 :nth-of-type(num)  是父元素的第num个 某类型的 子节点 
#例如 span:nth-of-type(2) 表示父节点中第二个tag名为span的子节点

#:nth-of-type 与 :nth-child 灵活使用  str:nth-child(num) 位置固定 必为父节点中的num位置且属性为str
# 而 str:nth-of-type(num) 更加灵活 为满足str的type中的第num个


elements = wd.find_elements_by_css_selector('h3:nth-of-type(1)')
for element in elements:
    print('------------3')
    print(element.get_attribute('outerHTML'))

#父元素的倒数第几个 某类型 的子节点 :nth-last-of-type(num)  是父元素的倒数第num个 某类型的 子节点 
#例如 span:nth-last-of-type(2) 表示父节点中倒数第二个tag名为span的子节点
elements = wd.find_elements_by_css_selector('span:nth-last-of-type(1)')
for element in elements:
    print('------------4')
    print(element.get_attribute('outerHTML'))

# 奇数节点和偶数节点  交叉出现会有用

# 如果要选择的是父元素的  偶数节点，使用 nth-child(even)
# p:nth-child(even) 且满足 名为p

# 如果要选择的是父元素的  奇数节点，使用 nth-child(odd)
# p:nth-child(odd) 且满足 名为p

# 如果要选择的是父元素的 某类型偶数节点，使用 :nth-of-type(even)
# 如果要选择的是父元素的 某类型奇数节点，使用 :nth-of-type(odd)


#相邻兄弟节点 + 号表示
#h3 + span 紧跟h3的span节点
elements = wd.find_elements_by_css_selector('h3 + span')
for element in elements:
    print('------------5')
    print(element.get_attribute('outerHTML'))

#所有的兄弟节点 ~ 号表示
#h3 ~ span h3同级节点中 的所有span节点
elements = wd.find_elements_by_css_selector('h3 ~ span')
for element in elements:
    print('------------6')
    print(element.get_attribute('innerHTML'))

wd.quit()
from selenium import webdriver

wd = webdriver.Chrome()

wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")
wd.implicitly_wait(5)

element = wd.find_element_by_css_selector('[href="http://www.miitbeian.gov.cn"]')  #[]内 直接通过所知的 属性与属性值 进行查找
element = wd.find_element_by_css_selector('[href]')     #[] 直接通过某一个元素 所有的属性 进行查找 (当满足所查属性唯一时)

#tag名,class,id 也可以和属性组合  .b[href] 表示class名为b 的 属性中有href的元素  

#都可以和 子元素 与 后代元素 组合

#当查询目标过长时 可以在浏览器中 elements 中 ctrl f  先查询语句 检查是否有匹配 可以节约时间提高效率
element = wd.find_element_by_css_selector('a[href]')     # a[href] 表示 tag名为a 的 属性中有href的元素

# span.date 表示 标签名为span的 class为date的元素 直接组合 等同于 span[class="date"]


print(element.get_attribute('outerHTML'))

wd.quit()

#包含 [href*="xxx"]  包含xxx即可
#以xxx开头 [href^="xxx"] 以xxx开头
#以xxx结尾 [href$="xxx"] 以xxx结尾
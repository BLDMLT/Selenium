import time

from selenium import webdriver

driver = webdriver.Chrome()
# 浏览器最大化
# driver.maximize_window()

driver.get('https://www.baidu.com')
# Note: 1 find elements
# driver.find_element_by_id('kw').send_keys('john')
# driver.find_element_by_name('wd').send_keys('test')
# driver.find_element_by_id('su').click()

# Note: 2 class属性定位
# class1 = driver.find_element_by_class_name('title-content-title')   # 默认第一个class属性
# print(class1.text)

# elements = driver.find_elements_by_class_name('title-content-title')    # 是个列表

# 打印列表
# for i in elements:
#     print(i.text)

# element = driver.find_elements_by_class_name('title-content-title')[0] #  第一个
# print(element.text)
# element.click()

# Note: 3 tagName 标签定位，标签是重复的，input span div
# span1 = driver.find_element_by_tag_name('span') # 第一个span标签
# print(span1.text)
# 所有标签
# span2 = driver.find_elements_by_tag_name('span')
# for i in span2:
#     print(i.text)

# Note: 4 link 和 partial_link 定位    超链接 <a href = "https://www.baidu.com"> </a>
# link1 = driver.find_element_by_link_text('新闻')    # 必须写全
# link1.click()
# partial_link 定位文本值，可以不用写全
# link2 = driver.find_element_by_partial_link_text('学术')
# link2.click()

# xpath 定位 id, name, class, tagname
# 页面 会很不好定位 -> xpath 定位 (绝对路径写法和表达式写法)
# input1 = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input')
# input1.send_keys('xpath')

# 表达式写法 依照属性进行定位 格式: [@属性="属性值"]    / 根节点    // 所有节点    * 所有元素
# input2 = driver.find_element_by_xpath('//*[@id="kw"]')
# input2.send_keys('xpath')

# Note: 5 css表达式定位
    # 1 css属性定位 id class tag
# element = driver.find_element_by_css_selector('#kw') # 相当于 driver.find_element_by_id('kw')
# element.send_keys('css')

# class属性，多值 用.
# elements = driver.find_elements_by_css_selector('.title-content-title')
# for i in elements:
#     print(i.text)

# 等待时间
# time.sleep(3)   #  等待3s
# 关闭浏览器
# driver.quit()

    # 2 css标签定位 <input> <div> <span>
# elements = driver.find_elements_by_css_selector('span')
# for i in elements:
#     print(i.text)

    # css层级定位   有父子关系
# element = driver.find_element_by_css_selector('#head_wrapper #kw')    # 元素 （空格） 后代元素
# element.send_keys('css')
#
# element = driver.find_element_by_css_selector('#head_wrapper .s_btn')
# element.click()

# css标签属性定位 <input type='text' id='kw' class='s_tr' name='wd'>
# element = driver.find_element_by_css_selector('input[id="kw"]')   # 注意单双引号
# element.send_keys('css')

# 或者
# driver.find_element_by_css_selector('input[id="kw"]').send_keys('css')

# 八种定位方式 id, name, class_name, tag_name. link text, partial link text, Xpath, and CSS

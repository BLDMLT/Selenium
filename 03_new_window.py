#   步骤
#   1、打开浏览器
#   2、访问网址
#   3、点击链接
#   4、在新窗口中输入内容

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.baidu.com')

driver.find_element_by_link_text('新闻').click()

# 切换到新窗口中去，用swith to
# 1、把打开到所有窗口的句柄都获取到
all_handles = driver.window_handles
# 2、显示全部窗口
for handle in all_handles:
    # 切换到新到窗口
    driver.switch_to.window(handle)
    # 判断要进入到窗口 -> 窗口名
    # 如果窗口标题到字符串符合，就跳出循环
    if '百度新闻' in driver.title:
        break


driver.find_element_by_id('ww').send_keys('new window')






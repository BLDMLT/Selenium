#   步骤
#   1、打开浏览器
#   2、放大窗口
#   3、访问网址
#   4、登陆（找到输入框，找按钮点击）
#   5、等待几秒
#   6、关闭
#
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.126.com')
# 1.标签写错，2.特殊元素 iframe
# 1、切换到iframe 内部    //*所有节点到元素，找iframe的父节点，定位到iframe
# iframe1 = driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe')
# 2、跳转到iframe内部里面
# driver.switch_to.frame(iframe1)
# driver.find_element_by_name('email').send_keys('name')
# 3、切回主页面
# driver.switch_to.default_content()
# driver.find_element_by_id('lbApp').click()
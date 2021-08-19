from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get('')

# driver.find_element_by_css_selector('input[value="[peach]').click() #   单选框

# 复选框
#   1、取消全部选择
elements = driver.find_elements_by_css_selector('input[checked="checked"]')
for element in elements:
    element.click()

#   2、选择
driver.find_elements_by_css_selector('#s_checkbox input[value="peach"]').click()

# 下拉框
# 导入Select包
# alt+enter 自动import包
Select(driver.find_element_by_id("aoe")).select_by_visible_text('banana')


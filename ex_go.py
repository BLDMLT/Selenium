from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.google.com')

driver.find_elements_by_class_name('gb_f')[1].click()
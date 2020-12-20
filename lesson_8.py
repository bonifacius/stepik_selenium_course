from selenium import webdriver
import time
import math

try:
	
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	x = browser.find_element_by_id("num1").text
	y = browser.find_element_by_id("num2").text
	sum_num = str(int(x) + int(y))
	from selenium.webdriver.support.ui import Select
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(sum_num)
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(10)
	browser.quit()

from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)

	img_gold = browser.find_element_by_tag_name('img')
	x = img_gold.get_attribute('valuex')
	y = calc(x)
	input1 = browser.find_element_by_id('answer').send_keys(y)
	input2 = browser.find_element_by_id('robotCheckbox').click()
	input3 = browser.find_element_by_id('robotsRule').click()
	button = browser.find_element_by_css_selector("button.btn").click()
finally:
	time.sleep(10)
	browser.quit()

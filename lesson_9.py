from selenium import webdriver
import time
import math

#Важное!!!считываем число со страницы мы как str(), потом передаем в функцию как int()
#А функция должна вернуть как str()!
def calc(x):
	return str(math.log(abs(12 * math.sin(x))))

try:
	
	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)
	#Находим элемент х на странице

	x = browser.find_element_by_id("input_value").text

	#Получаем значение через функцию
	y = calc(int(x))

	#Вводим результат в строку
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)

	
	#Используем код для скролинга страницы так как checkbox перекрыт футером.
	button = browser.find_element_by_id("robotCheckbox")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()

	#Ставим чекбокс2 
	input3 = browser.find_element_by_id('robotsRule').click()
	#submit
	button = browser.find_element_by_css_selector("button.btn").click()
	

finally:
	time.sleep(10)
	browser.quit()

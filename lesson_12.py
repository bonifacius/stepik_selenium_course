# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

# Сценарий для реализации выглядит так:

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
# Если все сделано правильно и достаточно быстро 
# (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
# Отправьте полученное число в качестве ответа на это задание.

from selenium import webdriver
import time
import math

#Создаем функцию для расчета задачи.
def calc(x):
	return str(math.log(abs(12 * math.sin(x))))


try:
	
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	button = browser.find_element_by_css_selector("button.btn").click()

	#С поомщью метода handles() получаем массив из имен всех вкладок.
	#Пиешм 1 так как новая вклдака это вторая в массиве.
	new_window = browser.window_handles[1]
	
	#Запоминае первую вкладку на всякий.
	first_window = browser.window_handles[0]

	#Переходим на новую вкладку
	browser.switch_to.window(new_window)

	
	

	#получаем знaчение, ищем поле ввода, вводим значение и submit
	x = browser.find_element_by_id("input_value").text
	y = calc(int(x))
	browser.find_element_by_id("answer").send_keys(y)

	button = browser.find_element_by_css_selector("button.btn").click()

finally:
	time.sleep(10)
	browser.quit()	
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
# Отправьте полученное число в качестве ответа на это задание.

from selenium import webdriver
import time
import math

#Создаем функцию для расчета задачи.
def calc(x):
	return str(math.log(abs(12 * math.sin(x))))

try:
	
	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	button = browser.find_element_by_css_selector("button.btn").click()

	#Переключамся на модальное окно 
	confirm = browser.switch_to.alert
	confirm.accept()

	#получаем знaчение, ищем поле ввода, вводим значение и submit
	x = browser.find_element_by_id("input_value").text
	y = calc(int(x))
	browser.find_element_by_id("answer").send_keys(y)

	button = browser.find_element_by_css_selector("button.btn").click()

finally:
	time.sleep(10)
	browser.quit()	
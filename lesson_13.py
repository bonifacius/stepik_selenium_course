# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из 
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

#Создаем функцию для расчета задачи.
def calc(x):
	return str(math.log(abs(12 * math.sin(x))))

try:
	
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	#Используем импортирование конструкции из expected_conditions as EC.
	#Что бы заставить скрипт ждать пока "price" не равен "$100".
	wait = WebDriverWait(browser, 40).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100")
	)

	#press button
	button = browser.find_element_by_css_selector("button.btn").click()
	
	#получаем знaчение, ищем поле ввода, вводим значение и submit
	x = browser.find_element_by_id("input_value").text
	y = calc(int(x))
	browser.find_element_by_id("answer").send_keys(y)

	button_1 = browser.find_element_by_id("solve").click()


#Переключаемся на allert и разделяем текст с помощью ":" и сохраняем
#в буфер обмена число после ":". Это и есть наш ответ.
	alert = browser.switch_to.alert
	alert_text = alert.text
	addToClipBoard = alert_text.split(': ')[-1]
	pyperclip.copy(addToClipBoard)



finally:
	time.sleep(10)
	browser.quit()	
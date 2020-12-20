from selenium import webdriver
import time
import os
#Загружаем файл с компьютера на сайт!

try:
	
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

	

	#Вводим результат в строку
	input1 = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
	input1.send_keys('Roman')
	input2 = browser.find_element_by_xpath("//input[@placeholder='Enter last name']")
	input2.send_keys('Basmanov')
	input3 = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
	input3.send_keys('b')
	


	# вернет нам путь до директории файла с текущим кодом 
	current_dir = os.path.abspath(os.path.dirname(__file__))  
	
	#В переменную file_path мы записываем путь до нашего питон скрипта
	#и дополняем названием файла который хотим скачать. Все вместе и будет путем до этого файла   
	file_path = os.path.join(current_dir, "file.txt")           
	
	#Проверяем наличия файла в папке скрипта и если его нет, то создаем.
	if not os.path.isfile("file.txt"):
		with open(file_path, 'w') as f:
			pass
	

	#Находим кнопку загрузить файл и передаем ему параметр file_path
	element = browser.find_element_by_xpath('//input[@type="file"]').send_keys(file_path)
	
	#submit
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	


finally:
	time.sleep(10)
	browser.quit()

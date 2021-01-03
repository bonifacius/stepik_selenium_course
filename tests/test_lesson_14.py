#Оформляем тесты в стиле unittest 
import unittest
from selenium import webdriver
import time


class Test(unittest.TestCase):
    def test_1(self):
     
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
            input1.send_keys("Roman")
            input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
            input2.send_keys("Basmanov")
            input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
            input3.send_keys("Chelyabinsk")
            input4 = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[1]/input")
            input4.send_keys("Russia")
            button = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/input")
            button.click()

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
            
            # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта    
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
 
   
    def test_2(self):
        
         #Код, который заполняет обязательные поля
        try: 
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
            input1.send_keys("Roman")
            input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
            input2.send_keys("Basmanov")
            input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
            input3.send_keys("Chelyabinsk")
            input4 = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[1]/input")
            input4.send_keys("Russia")
            button = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/input")
            button.click()

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
            
            # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта    
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        

if __name__ == "__main__": unittest.main()
 
 
      
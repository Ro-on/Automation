from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("ok")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("ok")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("ok")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # получаем путь к директории текущего исполняемого файла 
    # os.path.dirname(__file__)возвращает родительский каталог текущего выполняемого скрипта (т.е. ../)
    # os.path.dirname(os.path.dirname(__file__))возвращает родительский каталог 
    # родительского каталога текущего выполняемого скрипта. (т.е. ../../)
    file_path = os.path.join(current_dir, 'file.txt')
    # добавляем к этому пути имя файла 
    
    element = browser.find_element(By.NAME, "file") # находим элемент с добавлением файла
    element.send_keys(file_path) # посылаем в качестве ответа путь до файла
    
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    
finally:
    time.sleep(5)
    browser.quit
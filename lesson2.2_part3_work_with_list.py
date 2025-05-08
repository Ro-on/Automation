from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"

try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text # <-- без скобок!
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text
    sum = int(x) + int(y)
    
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(sum)) # Мы выбираем по тексту! str это строка!
    
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()#<-- скобки обязательны!
    
    
finally:
    time.sleep(5)
    browser.quit()
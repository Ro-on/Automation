from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # Мы выдернули цифру с помощью find element, 
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. 
    # Например, text для данного элемента <div class="message">У вас новое сообщение</div> вернёт строку: 
    # "У вас новое сообщение".
    # y присвоили значение метода calc(x), который до этого просчитал математическое уравнение

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()   # можно так


finally:
    time.sleep(5)
    browser.quit()
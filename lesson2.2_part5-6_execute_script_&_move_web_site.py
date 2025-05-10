"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    
 browser = webdriver.Chrome()
 link = "https://SunInJuly.github.io/execute_script.html"
 browser.get(link)
 button = browser.find_element(By.TAG_NAME, "button")находим элемент относительно которого будем двигать экран
 browser.execute_script("return arguments[0].scrollIntoView(true);", button)
 button.click()

finally:
    time.sleep(10)
    browser.quit
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/execute_script.html"
def calc(x):
  return math.log(abs(12*math.sin(int(x))))

try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    numX = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = numX.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    browser.execute_script("window.scrollBy(0, 100);") # двигаем экран вниз на 100 пикселей
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit
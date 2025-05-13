from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return math.log(abs(12*math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button").click()
    
    new_window = browser.window_handles[1] # узнаём имя новой вкладки, для того чтобы на неё переместиться
    browser.switch_to.window(new_window) # перемещаемся на new window
    # first_window = browser.window_handles[0] # сохранение имени текущей вкладки
    
    numX = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = numX.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button").click()
    
finally:
    time.sleep(5)
    browser.quit
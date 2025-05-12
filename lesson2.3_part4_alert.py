from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"
def calc(x):
  return math.log(abs(12*math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button").click()
    confirm = browser.switch_to.alert # модальное окно подтверждения
    confirm.accept() # подтверждение
    # confirm.dismiss() # отказ
    
    # alert = browser.switch_to.alert # алерт(можно только закрыть)
    # alert.accept()
    
    # alert = browser.switch_to.alert # для получения текста из алерт
    # alert_text = alert.text
    
    # prompt = browser.switch_to.alert # если что-то можно ввести
    # prompt.send_keys("My answer")
    # prompt.accept()
    
    numX = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = numX.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button").click()
    
finally:
    time.sleep(5)
    browser.quit
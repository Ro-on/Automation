from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    time.sleep(5)
    button.click()
    browser.quit()

finally:
    # закрываем браузер после всех манипуляций
    keyboard.wait('esc')
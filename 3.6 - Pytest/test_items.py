from selenium.webdriver.common.by import By
import time

def test_should_be_basket_button(r_browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
     r_browser.get(link)
     
     assert r_browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"), "Basket button not found"
     time.sleep(5)
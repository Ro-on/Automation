from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest

# pytest -v --tb=line --language=en -m need_review

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(r_browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(r_browser, link)
    page.open()
    
    page.add_to_bucket() # проверка добавления товара в корзину для гостя
    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(r_browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(r_browser, link)
    page.open()
    
    page.add_to_bucket()
    page.should_not_be_success_message() # проверка, что гость не видит уведомление об успешности добавления товара в корзину
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(r_browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(r_browser, link)
    page.open()
    
    page.add_to_bucket()
    page.should_be_success_message_is_disappeared() # проверка исчезновения сообщения о добавлении товара в корзину для гостя
    
def test_guest_should_see_login_link_on_product_page(r_browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(r_browser, link)
    page.open()
    page.should_be_login_link() # проверка видимости ссылки на логин
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(r_browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(r_browser, link)
    page.open()
    page.go_to_login_page() # проверка перехода на страницу логина с главной страницы для гостя
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(r_browser): 
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(r_browser, link)
    page.open()
    page.go_to_basket_page()
    r_browser.implicitly_wait(5)
    basket_page = BasketPage(r_browser, r_browser.current_url)
    basket_page.should_be_empty_basket_message() # проверка, что есть сообщение о пустой корзине для гостя
    
def test_guest_can_see_empty_basket_opened_from_product_page(r_browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(r_browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(r_browser, r_browser.current_url)
    basket_page.should_be_empty_basket() # проверка, что в корзине нету товара для гостя. Негатив-тест верхней проверки(он не отрицательный!)
    
@pytest.mark.user   
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, r_browser):
        
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(r_browser, link)
        page.open()
        
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "password"
        page.register_new_user(email, password)
        
        page.should_be_authorized_user() # сетап авторизации гостя
    
    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, r_browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
     page = ProductPage(r_browser, link)
     page.open()
    
     page.add_to_bucket()
     page.should_not_be_success_message() # проверка, что юзер не видит уведомление об успешном добавлении товара в корзину
     
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, r_browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
     page = ProductPage(r_browser, link)
     page.open()
     r_browser.implicitly_wait(5)
     page.add_to_bucket()
     r_browser.implicitly_wait(5)
     page.should_be_right_book()
     page.should_be_right_price() # проверка добавления юзером товара в корзину
     # иногда может не запуститься с первого раза(из-за ожидания)! Если было провалено - запустить тест снова.
     
    

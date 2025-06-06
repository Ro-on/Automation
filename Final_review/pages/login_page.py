from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        assert "login" in link, "Not current url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True
        
    def register_new_user(self, email, password):
        self.r_browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION).send_keys(email)
        self.r_browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION).send_keys(password)
        self.r_browser.find_element(*LoginPageLocators.REPEAT_PASSWORD).send_keys(password)
        self.r_browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
        
        
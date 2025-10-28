from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    EMAIL = (By.ID, 'email-2')
    PASSWORD = (By.ID, 'field')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'a.login-button.w-button')

    def input_email(self, email):
        self.input_text(email, *self.EMAIL)

    def input_password(self, password):
        self.input_text(password, *self.PASSWORD)
        self.click(*self.CONTINUE_BTN)
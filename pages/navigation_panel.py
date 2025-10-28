from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class NavigationPanel(Page):
    DEVELOPER_BTN = (By.CSS_SELECTOR, 'a[href*="for-developer"]')

    def click_developer_btn(self):
        self.wait_for_element(*self.DEVELOPER_BTN)
        self.click(*self.DEVELOPER_BTN)
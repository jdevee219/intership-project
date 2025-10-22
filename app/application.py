from pages.base_page import Page
from pages.for_developers_page import ForDevelopersPage
from pages.main_page import MainPage
from pages.navigation_panel import NavigationPanel
from pages.sign_in_page import SignInPage



class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.for_developers_page = ForDevelopersPage(driver)
        self.main_page = MainPage(driver)
        self.navigation_panel = NavigationPanel(driver)
        self.sign_in_page = SignInPage(driver)

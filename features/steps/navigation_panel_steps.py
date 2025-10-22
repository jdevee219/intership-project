from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

DEVELOPER_BTN = (By.CSS_SELECTOR, 'a[href*="for-developer"]')

@when('Click on Connect the developer button')
def click_developer_btn(context):
    context.driver.find_element(*DEVELOPER_BTN).click()

@when('Switch to new window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()

@then('Verify For Developers page is opened')
def verify_fd_opened(context):
    context.app.for_developers_page.verify_fd_opened()
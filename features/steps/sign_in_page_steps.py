from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when('Enter email {email}')
def input_email(context, email):
    context.app.sign_in_page.input_email(email)

@when('Enter password {password}')
def input_password(context, password):
    context.app.sign_in_page.input_password(password)
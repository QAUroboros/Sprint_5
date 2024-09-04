import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from constants import REGISTRATION_DATA



def test_check_personal_account(open_browser):
    driver = open_browser
    login_button_main = driver.find_element(*LOGIN_BUTTON_MAIN)
    login_button_main.click()
    email_field_auth = driver.find_element(*EMAIL_FIELD_LOGIN)
    email_field_auth.send_keys(REGISTRATION_DATA["email"])
    password_field_auth = driver.find_element(*PASSWORD_FIELD_LOGIN)
    password_field_auth.send_keys(REGISTRATION_DATA["password"])
    login_button = driver.find_element(*LOGIN_BUTTON_LOGIN)
    login_button.click()
    login_to_click = driver.find_element(*LOGIN_PAGE_LINK)
    login_to_click.click()
    constructor_link = driver.find_element(*BUTTON_CONSTRUCTOR)
    time.sleep(4)
    constructor_link.click()
    burger_text_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BURGER_ELEMENT_TXT))
    assert burger_text_element.is_displayed(), "Заголовок 'Соберите бургер' не отображается на странице"

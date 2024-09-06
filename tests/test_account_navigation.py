import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from constants import REGISTRATION_DATA



def test_check_personal_account(open_browser,generate_registration_data):
    driver = open_browser
    driver.implicitly_wait(10)
    login_button_main = driver.find_element(*LOGIN_BUTTON_MAIN)
    login_button_main.click()
    email_field_auth = driver.find_element(*EMAIL_FIELD_LOGIN)
    email_field_auth.send_keys(REGISTRATION_DATA["email"])
    password_field_auth = driver.find_element(*PASSWORD_FIELD_LOGIN)
    password_field_auth.send_keys(REGISTRATION_DATA["password"])
    login_button = driver.find_element(*LOGIN_BUTTON_LOGIN)
    login_button.click()
    time.sleep(3)
    login_to_click = driver.find_element(*LOGIN_PAGE_LINK)
    login_to_click.click()
    profile_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((PROFILE_TXT)))
    assert profile_element.is_displayed(), "Элемент 'Профиль' не отображается на странице."

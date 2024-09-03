import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import *
from constants import REGISTRATION_DATA



def test_check_personal_account(open_browser):
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
    time.sleep(2)
    text_profile = driver.find_element(*PROFILE_TXT).text
    assert "Профиль" in text_profile, "Текст 'Профиль' не найден на странице."

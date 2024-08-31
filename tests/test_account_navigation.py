import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import *


def test_check_personal_account(open_browser, registration_data):
    driver = open_browser
    driver.implicitly_wait(10)
    login_button_main = driver.find_element(*LOGIN_BUTTON_MAIN)
    login_button_main.click()
    email_field_auth = driver.find_element(*EMAIL_FIELD_LOGIN)
    email_field_auth.send_keys(registration_data["email"])
    password_field_auth = driver.find_element(*PASSWORD_FIELD_LOGIN)
    password_field_auth.send_keys(registration_data["password"])
    login_button = driver.find_element(*LOGIN_BUTTON_LOGIN)
    login_button.click()
    time.sleep(3)
    login_to_click = driver.find_element(*LOGIN_PAGE_LINK)
    login_to_click.click()
    time.sleep(2)
    text_profile = driver.find_element(By.TAG_NAME, "body").text
    assert "Профиль" in text_profile, "Текст 'Профиль' не найден на странице."

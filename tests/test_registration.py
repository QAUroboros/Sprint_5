import time
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import *
from constants import REGISTRATION_DATA
from constants import BAD_REGISTRATION_DATA_IN_PASSWORD
from conftest import generate_registration_data



def test_fill_registration_form(open_browser, generate_registration_data):
    driver = open_browser
    driver.implicitly_wait(10)
    login_to_click = driver.find_element(*LOGIN_PAGE_LINK)
    login_to_click.click()
    register_to_click = driver.find_element(*REGISTER_PAGE_LINK)
    register_to_click.click()
    name_field = driver.find_element(*NAME_FIELD)
    name_field.send_keys(REGISTRATION_DATA["name"])
    email_field_auth = driver.find_element(*EMAIL_FIELD)
    email_field_auth.send_keys(generate_registration_data["email"])
    time.sleep(3)
    password_field_auth = driver.find_element(*PASSWORD_FIELD_LOGIN)
    password_field_auth.send_keys(REGISTRATION_DATA["password"])
    button = driver.find_element(*BUTTON_REGISTRATION)
    button.click()


def test_failed_registration_form(open_browser):
    driver = open_browser
    wait = WebDriverWait(driver, 7)
    login_to_click = driver.find_element(*LOGIN_PAGE_LINK)
    login_to_click.click()
    register_to_click = driver.find_element(*REGISTER_PAGE_LINK)
    register_to_click.click()
    name_field = driver.find_element(*NAME_FIELD)
    name_field.send_keys(BAD_REGISTRATION_DATA_IN_PASSWORD["name"])
    email_field_auth = driver.find_element(*EMAIL_FIELD)
    email_field_auth.send_keys(BAD_REGISTRATION_DATA_IN_PASSWORD["email"])
    password_field_auth = driver.find_element(*PASSWORD_FIELD_LOGIN)
    password_field_auth.send_keys(BAD_REGISTRATION_DATA_IN_PASSWORD["password"])
    button = driver.find_element(*BUTTON_REGISTRATION)
    button.click()
    time.sleep(4)
    error_message_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")))
    assert error_message_element.text == "Некорректный пароль", "Сообщение об ошибке не отображается или текст не совпадает"
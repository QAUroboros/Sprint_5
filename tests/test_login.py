import time
from lib2to3.pgen2 import driver
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from locators import *



def test_enter_in_account_from_button_main_page(open_browser, registration_data):
    driver = open_browser
    login_button_main = driver.find_element(*LOGIN_BUTTON_MAIN)
    login_button_main.click()
    email_field_auth = driver.find_element(*EMAIL_FIELD_LOGIN)
    email_field_auth.send_keys(registration_data["email"])
    password_field_auth = driver.find_element(*PASSWORD_FIELD_LOGIN)
    password_field_auth.send_keys(registration_data["password"])
    login_button = driver.find_element(*LOGIN_BUTTON_LOGIN)
    login_button.click()


def test_enter_from_button_personal_account(open_browser, registration_data):
    driver = open_browser
    login_to_click = driver.find_element(*LOGIN_PAGE_LINK)
    login_to_click.click()
    email_field_auth = driver.find_element(*EMAIL_FIELD_LOGIN)
    email_field_auth.send_keys(registration_data["email"])
    password_field_auth = driver.find_element(*PASSWORD_FIELD_LOGIN)
    password_field_auth.send_keys(registration_data["password"])
    login_button = driver.find_element(*LOGIN_BUTTON_LOGIN)
    login_button.click()


def test_enter_in_account_from_registration_form(open_browser,registration_data):
    driver = open_browser
    login_button_main = driver.find_element(*LOGIN_BUTTON_MAIN)
    login_button_main.click()
    time.sleep(3)
    register_to_click = driver.find_element(*REGISTER_PAGE_LINK)
    register_to_click.click()
    login_link = driver.find_element(*LOGIN_LINK)
    login_link.click()
    email_field_auth = driver.find_element(*EMAIL_FIELD_LOGIN)
    email_field_auth.send_keys(registration_data["email"])
    password_field_auth = driver.find_element(*PASSWORD_FIELD_LOGIN)
    password_field_auth.send_keys(registration_data["password"])
    login_button = driver.find_element(*LOGIN_BUTTON_LOGIN)
    login_button.click()

def test_enter_in_account_from_forgot_password(open_browser,registration_data):
    driver = open_browser
    driver.implicitly_wait(10)
    login_button_main = driver.find_element(*LOGIN_BUTTON_MAIN)
    login_button_main.click()
    forgot_password_link = driver.find_element(*FORGOT_LINK)
    forgot_password_link.click()
    email_field_auth = driver.find_element(*EMAIL_FIELD_LOGIN)
    email_field_auth.send_keys(registration_data["email"])
    restore_button = driver.find_element(*BUTTON_RESTORE)
    restore_button.click()
    time.sleep(2)
    login_link = driver.find_element(*LOGIN_LINK)
    login_link.click()
    email_field = driver.find_element(*EMAIL_FIELD_LOGIN)
    email_field.send_keys(registration_data["email"])
    password_field = driver.find_element(*PASSWORD_FIELD_LOGIN)
    password_field.send_keys(registration_data["password"])
    button = driver.find_element(*LOGIN_BUTTON_MAIN)
    button.click()



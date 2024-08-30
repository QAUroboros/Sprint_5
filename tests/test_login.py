import time
from lib2to3.pgen2 import driver
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from locators import *



def test_enter_in_account_from_button_main_page(open_browser,registration_data):
    driver = open_browser
    login_button_main = driver.find_element(By.CLASS_NAME, "button_button__33qZ0")
    login_button_main.click()
    email_field_auth = driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text')]//input[@name='name']")
    email_field_auth.send_keys(registration_data["email"])
    password_field_auth = driver.find_element(By.XPATH,"//div[@class='input pr-6 pl-6 input_type_password input_size_default']//input[@name='Пароль']")
    password_field_auth.send_keys(registration_data["password"])
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()


def test_enter_from_button_personal_account(open_browser,registration_data):
    driver = open_browser
    login_to_click = driver.find_element(By.XPATH,"//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']")
    login_to_click.click()
    email_field_auth = driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text')]//input[@name='name']")
    email_field_auth.send_keys(registration_data["email"])
    password_field_auth = driver.find_element(By.XPATH,"//div[@class='input pr-6 pl-6 input_type_password input_size_default']//input[@name='Пароль']")
    password_field_auth.send_keys(registration_data["password"])
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()


def test_enter_in_account_from_registration_form(open_browser,registration_data):
    driver = open_browser
    login_button_main = driver.find_element(By.CLASS_NAME, "button_button__33qZ0")
    login_button_main.click()
    register_to_click = driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']")
    register_to_click.click()
    login_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Войти')]")
    login_link.click()
    email_field_auth = driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text')]//input[@name='name']")
    email_field_auth.send_keys(registration_data["email"])
    password_field_auth = driver.find_element(By.XPATH,"//div[@class='input pr-6 pl-6 input_type_password input_size_default']//input[@name='Пароль']")
    password_field_auth.send_keys(registration_data["password"])
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()

def test_enter_in_account_from_forgot_password(open_browser,registration_data):
    driver = open_browser
    driver.implicitly_wait(10)
    login_button_main = driver.find_element(By.CLASS_NAME, "button_button__33qZ0")
    login_button_main.click()
    forgot_password_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
    forgot_password_link.click()
    email_field_auth = driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text')]//input[@name='name']")
    email_field_auth.send_keys(registration_data["email"])
    restore_button = driver.find_element(By.CSS_SELECTOR,".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    restore_button.click()
    time.sleep(2)
    login_link = driver.find_element(By.XPATH,"//p[contains(text(), 'Вспомнили пароль?')]//a[contains(@href, '/login')]")
    login_link.click()
    email_field = driver.find_element(By.XPATH,"//div[@class='input pr-6 pl-6 input_type_text input_size_default']//input[@name='name']")
    email_field.send_keys(registration_data["email"])
    password_field = driver.find_element(By.XPATH,"//div[@class='input pr-6 pl-6 input_type_password input_size_default']//input[@name='Пароль']")
    password_field.send_keys(registration_data["password"])
    button = driver.find_element(By.CLASS_NAME, "button_button__33qZ0")
    button.click()



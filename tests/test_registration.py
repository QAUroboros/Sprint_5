import time
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import *


def test_fill_registration_form(open_browser, registration_data):
    driver = open_browser
    driver.implicitly_wait(10)
    login_to_click = driver.find_element(*LOGIN_PAGE_LINK)
    login_to_click.click()
    register_to_click = driver.find_element(*REGISTER_PAGE_LINK)
    register_to_click.click()
    name_field = driver.find_element(*NAME_FIELD)
    name_field.send_keys(registration_data["name"])
    email_field_auth = driver.find_element(*EMAIL_FIELD)
    email_field_auth.send_keys(registration_data["email"])
    password_field_auth = driver.find_element(*PASSWORD_FIELD_LOGIN)
    password_field_auth.send_keys(registration_data["password"])
    button = driver.find_element(*BUTTON_REGISTRATION)
    button.click()


def test_failed_registration_form(open_browser, bad_registration_data_in_password):
    driver = open_browser
    wait = WebDriverWait(driver, 7)
    login_to_click = driver.find_element(By.XPATH,"//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']")
    login_to_click.click()
    register_to_click = driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']")
    register_to_click.click()
    name_field = driver.find_element(By.XPATH, "//input[@name='name']")
    name_field.send_keys(bad_registration_data_in_password["name"])
    email_field = driver.find_element(By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default']//input[@name='name']")
    email_field.send_keys(bad_registration_data_in_password["email"])
    password_field = driver.find_element(By.XPATH,"//div[@class='input pr-6 pl-6 input_type_password input_size_default']//input[@name='Пароль']")
    password_field.send_keys(bad_registration_data_in_password["password"])
    button = driver.find_element(By.CLASS_NAME, "button_button__33qZ0")
    button.click()
    error_message_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")))
    assert error_message_element.text == "Некорректный пароль", "Сообщение об ошибке не отображается или текст не совпадает"





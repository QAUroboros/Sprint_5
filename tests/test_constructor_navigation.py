from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import *


def test_check_personal_account(open_browser,registration_data):
    driver = open_browser
    login_button_main = driver.find_element(By.CLASS_NAME, "button_button__33qZ0")
    login_button_main.click()
    email_field_auth = driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text')]//input[@name='name']")
    email_field_auth.send_keys(registration_data["email"])
    password_field_auth = driver.find_element(By.XPATH,"//div[@class='input pr-6 pl-6 input_type_password input_size_default']//input[@name='Пароль']")
    password_field_auth.send_keys(registration_data["password"])
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()
    login_to_click = driver.find_element(By.XPATH,"//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']")
    login_to_click.click()
    constructor_link = driver.find_element(By.XPATH, "//p[contains(text(), 'Конструктор')]")
    constructor_link.click()
    burger_text_element = driver.find_element(By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    assert burger_text_element.text == "Соберите бургер", "Заголовок 'Соберите бургер' не найден на странице"
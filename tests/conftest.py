import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10)
    yield driver
    driver.quit()


@pytest.fixture
def registration_data():
    return {
        "name": "Артём",
        "email": "ArtemKrivoshein13699@yandex.ru",
        "password": "123456"
    }

@pytest.fixture
def bad_registration_data_in_password():
    return {
        "name": "Артём",
        "email": "ArtemKrivoshein13459@yandex.ru",
        "password": "123"
    }
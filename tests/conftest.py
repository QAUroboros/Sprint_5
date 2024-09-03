import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from constants import BASE_URL
from constants import REGISTRATION_DATA
import random



@pytest.fixture
def open_browser():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    WebDriverWait(driver, 10)
    yield driver
    driver.quit()


@pytest.fixture
def generate_registration_data():
    return {
        "name": "Артём",
        "email": f"ArtemKrivoshein13{random.randint(100, 999)}@yandex.ru",
        "password": "123456"
    }
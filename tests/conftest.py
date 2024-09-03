import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from constants import BASE_URL



@pytest.fixture
def open_browser():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    WebDriverWait(driver, 10)
    yield driver
    driver.quit()
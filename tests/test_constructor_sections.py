import time
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import *


def test_constructor_sauces_section(open_browser):
    driver = open_browser
    sauces_section = driver.find_element(By.XPATH,"//span[text()='Соусы']")
    sauces_section.click()
    sauces_header = driver.find_element(By.XPATH, "//h2[text()='Соусы']")
    sauce_1 = driver.find_element(By.XPATH, "//p[text()='Соус Spicy-X']")
    sauce_2 = driver.find_element(By.XPATH, "//p[text()='Соус фирменный Space Sauce']")
    sauce_3 = driver.find_element(By.XPATH, "//p[text()='Соус традиционный галактический']")
    sauce_4 = driver.find_element(By.XPATH, "//p[text()='Соус с шипами Антарианского плоскоходца']")
    assert sauces_header.is_displayed(), "Заголовок 'Соусы' не отображается на странице"
    assert sauce_1.is_displayed(), "Соус Spicy-X не отображается на странице"
    assert sauce_2.is_displayed(), "Соус фирменный Space Sauce не отображается на странице"
    assert sauce_3.is_displayed(), "Соус традиционный галактический не отображается на странице"
    assert sauce_4.is_displayed(), "Соус с шипами Антарианского плоскоходца не отображается на странице"


def test_constructor_fillings_section(open_browser):
    driver = open_browser
    fillings_section = driver.find_element(By.XPATH, "//span[text()='Начинки']")
    fillings_section.click()
    fillings_header = driver.find_element(By.XPATH, "//h2[text()='Начинки']")
    ingredient_1 = driver.find_element(By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']")
    ingredient_2 = driver.find_element(By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']")
    ingredient_3 = driver.find_element(By.XPATH, "//p[text()='Биокотлета из марсианской Магнолии']")
    ingredient_4 = driver.find_element(By.XPATH, "//p[text()='Филе Люминесцентного тетраодонтимформа']")
    ingredient_5 = driver.find_element(By.XPATH, "//p[text()='Хрустящие минеральные кольца']")
    ingredient_6 = driver.find_element(By.XPATH, "//p[text()='Плоды Фалленианского дерева']")
    ingredient_7 = driver.find_element(By.XPATH, "//p[text()='Кристаллы марсианских альфа-сахаридов']")
    ingredient_8 = driver.find_element(By.XPATH, "//p[text()='Мини-салат Экзо-Плантаго']")
    ingredient_9 = driver.find_element(By.XPATH, "//p[text()='Сыр с астероидной плесенью']")

    assert fillings_header.is_displayed(), "Заголовок 'Начинки' не отображается на странице"
    assert ingredient_1.is_displayed(), "Мясо бессмертных моллюсков Protostomia не отображается на странице"
    assert ingredient_2.is_displayed(), "Говяжий метеорит (отбивная) не отображается на странице"
    assert ingredient_3.is_displayed(), "Биокотлета из марсианской Магнолии не отображается на странице"
    assert ingredient_4.is_displayed(), "Филе Люминесцентного тетраодонтимформа не отображается на странице"
    assert ingredient_5.is_displayed(), "Хрустящие минеральные кольца не отображаются на странице"
    assert ingredient_6.is_displayed(), "Плоды Фалленианского дерева не отображаются на странице"
    assert ingredient_7.is_displayed(), "Кристаллы марсианских альфа-сахаридов не отображаются на странице"
    assert ingredient_8.is_displayed(), "Мини-салат Экзо-Плантаго не отображается на странице"
    assert ingredient_9.is_displayed(), "Сыр с астероидной плесенью не отображается на странице"

def test_constructor_buns_section(open_browser):
    driver = open_browser
    driver.implicitly_wait(10)
    buns_section = driver.find_element(By.XPATH,"//span[text()='Булки']")
    driver.execute_script("arguments[0].scrollIntoView(true);", buns_section)
    driver.execute_script("arguments[0].click();", buns_section)
    buns_header = driver.find_element(By.XPATH, "//h2[text()='Булки']")
    ingredient_in_list_1 = driver.find_element(By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    ingredient_in_list_2 = driver.find_element(By.XPATH, "//p[text()='Краторная булка N-200i']")

    assert buns_header.is_displayed(), "Заголовок 'Булки' не отображается на странице"
    assert ingredient_in_list_1.is_displayed(), "Ингредиент 'Флюоресцентная булка R2-D3' не найден в списке"
    assert ingredient_in_list_2.is_displayed(), "Ингредиент 'Краторная булка N-200i' не найден в списке"


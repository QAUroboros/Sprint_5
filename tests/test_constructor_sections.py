import time
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import *


def test_constructor_sauces_section(open_browser):
    driver = open_browser
    sauces_tab = driver.find_element(*TABS["sauces"])
    sauces_tab.click()
    assert "tab_tab_type_current__2BEPc" in sauces_tab.get_attribute("class")
    fillings_tab = driver.find_element(*TABS["fillings"])
    buns_tab = driver.find_element(*TABS["buns"])
    assert "tab_tab_type_current__2BEPc" not in fillings_tab.get_attribute("class")
    assert "tab_tab_type_current__2BEPc" not in buns_tab.get_attribute("class")

def test_constructor_fillings_section(open_browser):
    driver = open_browser
    fillings_tab = driver.find_element(*TABS["fillings"])
    fillings_tab.click()
    assert "tab_tab_type_current__2BEPc" in fillings_tab.get_attribute("class")
    sauces_tab = driver.find_element(*TABS["sauces"])
    buns_tab = driver.find_element(*TABS["buns"])
    assert "tab_tab_type_current__2BEPc" not in sauces_tab.get_attribute("class")
    assert "tab_tab_type_current__2BEPc" not in buns_tab.get_attribute("class")

def test_constructor_buns_section(open_browser):
    driver = open_browser
    fillings_tab = driver.find_element(*TABS["fillings"])
    fillings_tab.click()
    buns_tab = driver.find_element(*TABS["buns"])
    buns_tab.click()
    assert "tab_tab_type_current__2BEPc" in buns_tab.get_attribute("class")
    sauces_tab = driver.find_element(*TABS["sauces"])
    fillings_tab = driver.find_element(*TABS["fillings"])
    assert "tab_tab_type_current__2BEPc" not in sauces_tab.get_attribute("class")
    assert "tab_tab_type_current__2BEPc" not in fillings_tab.get_attribute("class")

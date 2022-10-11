from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestItemsCase:
    def test_items(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
        assert button.is_enabled(), 'Purchase button is not active or doesnt exist.'

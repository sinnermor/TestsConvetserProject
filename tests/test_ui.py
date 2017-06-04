from selenium.webdriver.support import expected_conditions as EC, wait, ui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from pages.ConverterPage import ConverterLocators

text_for_ini = '''Курсы иностранных валют относятся только к физическим лицам.
Обратите внимание, при покупке или продаже валюты с использованием карты, списание средств со счета карты проводится по курсу, действующему на момент фактического списания, и может отличаться от курса на момент совершения операции
Внимание! Курс по картам (за исключением операции карта-вклад) можно посмотреть здесь'''

header_title = 'Калькулятор иностранных валют'

# @allure.feature('Check title and text information about currency changings')
def test_interface(app):
    app.open_home_page()
    app.page_maximize()
    assert app.convertpage.check_text_header_block(text_for_ini) == text_for_ini, 'Header info is not match with excpected'
    assert app.convertpage.get_page_header_title() == header_title, "Header is wrong. It shouls be"+header_title


# @allure.story('')
def test_ibank_inactive(app):
    app.open_home_page()
    app.page_maximize()
    app.convertpage.select_source("card")
    app.convertpage.select_destination("cash")
    assert not app.convertpage.get_check_status_element(ConverterLocators.EXCHANGE_IBANK), "Element should be inactive"

# @allure.story('')
def test_account_cash_inactive_elements(app):
    app.open_home_page()
    app.page_maximize()
    app.convertpage.select_source("account")
    app.convertpage.select_destination("cash")
    assert not app.convertpage.get_check_status_element(ConverterLocators.EXCHANGE_IBANK), "Element should be inactive "
    assert not app.convertpage.get_check_status_element(ConverterLocators.EXCHANGE_ATM), "Element should be inactive "



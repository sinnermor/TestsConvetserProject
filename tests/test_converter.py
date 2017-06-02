from selenium.webdriver.support import expected_conditions as EC, wait, ui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from pages.ConverterPage import ConverterLocators


def test_convert_money(app, csv_param):

    source = csv_param['source']
    destination = csv_param['destination']
    exchange = csv_param['exchange']
    app.open_home_page()
    app.page_maximize()
    app.convertpage.type_sum_convertation('300')
    WebDriverWait(app.driver, 30).until(EC.text_to_be_present_in_element_value((By.XPATH,"//div[contains(@class, 'rates-aside__filter-block-line-right')]/form/input"), "100 300"))
    # app.convertpage.choose_from_currency_value('EUR')
    app.convertpage.select_source(source)
    app.convertpage.select_destination(destination)
    app.convertpage.select_exchange(exchange)
    app.convertpage.click_show_button(ConverterLocators.SHOW_BUTTON_CONVERTER)


    #Test has money params

    # Выбрать валюту из
    # выбрать валюту в
    # Выбрать источник карта сбербанка
    # Choose get out - card
    # Choose change - internet bank
    # Choose time real
    # Press show
    # Check you have pop up with correct data
#
# def test_check_ui(app):
#     pass
#





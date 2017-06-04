from selenium.webdriver.support import expected_conditions as EC, wait, ui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from pages.ConverterPage import ConverterLocators


def test_convert_money_from_rub(app, csv_param):
    app.open_home_page()
    app.page_maximize()
    app.convertpage.type_sum_convertation('1000')
    WebDriverWait(app.driver, 50).until(EC.text_to_be_present_in_element_value((By.XPATH,'//div[contains(@class, "rates-aside__filter-block-line-right")]/form/input'), "1 000"))
    app.convertpage.choose_from_currency_value(csv_param['money_from'], 'From')

    app.convertpage.choose_from_currency_value(csv_param['money_to'], 'To')
    app.convertpage.select_source(csv_param['source'])
    app.convertpage.select_destination(csv_param['destination'])
    app.convertpage.select_exchange(csv_param['exchange'])
    app.convertpage.click_show_button(ConverterLocators.SHOW_BUTTON_CONVERTER)
    assert app.convertpage.calculated_sum(1000) == app.convertpage.get_total_sum(), "Sums calculated and given are different"

# def test_debug(app):
#     app.open_home_page()
#     app.page_maximize()
#     app.convertpage.choose_from_currency_value("EUR")
#     app.convertpage.cont_convert_sum('100300')

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





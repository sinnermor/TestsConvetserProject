from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pages.ConverterPage import ConverterLocators

def test_convert_money(app):
    app.open_home_page()
    app.page_maximize()
    app.convertpage.type_sum_convertation('300')
    # app.convertpage.choose_from_currency_value('EUR')
    WebDriverWait(app.driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@name='exchangeType' and @value='ibank']")))
    # app.convertpage.select_input_checkbox(ConverterLocators.SOURCE_CARD)
    app.convertpage.select_input_checkbox(ConverterLocators.EXCHANGE_IBANK)
    app.convertpage.select_input_checkbox(ConverterLocators.DESTINATION_CARD)

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





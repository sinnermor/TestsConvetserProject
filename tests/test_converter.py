from selenium.webdriver.support import expected_conditions as EC, wait, ui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from pages.ConverterPage import ConverterLocators
import allure


@allure.story('Check converter')
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
    with pytest.allure.step('Assert sum results'):
        assert app.convertpage.calculated_sum(1000) == app.convertpage.get_total_sum(), "Sums calculated and given are different"



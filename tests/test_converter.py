from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from pages.ConverterPage import ConverterLocators
import allure


@allure.story('Check converter')
def test_convert_money_from_rub(fixture, csv_param):
    fixture.open_home_page()
    fixture.page_maximize()
    fixture.convertpage.type_sum_convertation('1000')
    WebDriverWait(fixture.driver, 50). \
        until(EC.text_to_be_present_in_element_value((
        By.XPATH, '//div[contains(@class, '
                  '"rates-aside__filter-block-line-right")]'
                  '/form/input'), "1 000"))
    fixture.convertpage.choose_from_currency_value(csv_param['money_from'],
                                                   'From')
    fixture.convertpage.choose_from_currency_value(csv_param['money_to'],
                                                   'To')
    fixture.convertpage.select_source(csv_param['source'])
    fixture.convertpage.select_destination(csv_param['destination'])
    fixture.convertpage.select_exchange(csv_param['exchange'])
    fixture.convertpage.click_show_button(
        ConverterLocators.SHOW_BUTTON_CONVERTER)
    with pytest.allure.step('Assert sum results'):
        assert fixture.convertpage.calculated_sum(1000) == \
               fixture.convertpage.get_total_sum(), 'Sums calculated and given are different'

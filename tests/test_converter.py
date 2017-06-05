from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from pages.ConverterPage import ConverterLocators
import allure


@allure.story('Check converter')
def test_convert_money_from_rub(glob_fixture, csv_param):
    glob_fixture.open_home_page()
    glob_fixture.page_maximize()
    glob_fixture.convertpage.type_sum_convertation('1000')
    WebDriverWait(glob_fixture.driver, 50). \
        until(
        EC.text_to_be_present_in_element_value((
            By.XPATH,
            '//div[contains(@class, "rates-aside__filter-block-line-right")]'
            '/form/input'), "1 000"))
    glob_fixture.convertpage.choose_from_currency_value(
        csv_param['money_from'], 'From')
    glob_fixture.convertpage.choose_from_currency_value(
        csv_param['money_to'], 'To')
    glob_fixture.convertpage.select_source(csv_param['source'])
    glob_fixture.convertpage.select_destination(csv_param['destination'])
    glob_fixture.convertpage.select_exchange(csv_param['exchange'])
    glob_fixture.convertpage.click_show_button(
        ConverterLocators.SHOW_BUTTON_CONVERTER)
    with pytest.allure.step('Assert sum results'):
        assert glob_fixture.convertpage.calculated_sum(1000) == \
               glob_fixture.convertpage.get_total_sum(), 'Sums different'

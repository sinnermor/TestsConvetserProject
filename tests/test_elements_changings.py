import allure
import pytest
from pages.ConverterPage import ConverterLocators

@allure.story('Check element ibank is inactive when selected card and cash')
def test_ibank_inactive(app):
    app.open_home_page()
    app.page_maximize()
    app.convertpage.select_source("card")
    app.convertpage.select_destination("cash")
    with pytest.allure.step('Assert ibank is inactive'):
        assert not app.convertpage.get_check_status_element(ConverterLocators.EXCHANGE_IBANK), "Element should be inactive"

@allure.story('Check that ibank and atm is disabled when cash - cash is selected')
def test_account_cash_inactive_elements(app):
    app.open_home_page()
    app.page_maximize()
    app.convertpage.select_source("account")
    app.convertpage.select_destination("cash")
    with pytest.allure.step('Assert ibank and atm are inactive'):
        assert not app.convertpage.get_check_status_element(ConverterLocators.EXCHANGE_IBANK), "Element should be inactive "
        assert not app.convertpage.get_check_status_element(ConverterLocators.EXCHANGE_ATM), "Element should be inactive "

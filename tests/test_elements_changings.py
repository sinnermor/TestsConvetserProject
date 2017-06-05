import allure
import pytest
from pages.ConverterPage import ConverterLocators


@allure.story('Check element ibank inactive when selected card and cash')
def test_ibank_inactive(glob_fixture):
    glob_fixture.open_home_page()
    glob_fixture.page_maximize()
    glob_fixture.convertpage.select_source("card")
    glob_fixture.convertpage.select_destination("cash")
    with pytest.allure.step('Assert ibank is inactive'):
        assert not glob_fixture.convertpage.get_check_status_element(
            ConverterLocators.EXCHANGE_IBANK), "Element should be inactive"


@allure.story('Check that ibank and atm is disabled when cash'
              ' - cash is selected')
def test_account_cash_inactive_elements(glob_fixture):
    glob_fixture.open_home_page()
    glob_fixture.page_maximize()
    glob_fixture.convertpage.select_source("account")
    glob_fixture.convertpage.select_destination("cash")
    with pytest.allure.step('Assert ibank and atm are inactive'):
        assert not glob_fixture.convertpage.get_check_status_element(
            ConverterLocators.EXCHANGE_IBANK), "Element should be inactive"
        assert not glob_fixture.convertpage.get_check_status_element(
            ConverterLocators.EXCHANGE_ATM), "Element should be inactive "

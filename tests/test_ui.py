import pytest
import allure

header_title = 'Калькулятор иностранных валют'


@allure.feature('Check title and text information about currency changings')
def test_interface(glob_fixture):
    glob_fixture.open_home_page()
    glob_fixture.page_maximize()
    with pytest.allure.step('Assert test block'):
        glob_fixture.convertpage.assert_page_info_text()
    with pytest.allure.step('Assert header is the same as expected'):
        assert glob_fixture.convertpage.get_page_header_title()\
               == header_title, "Header is wrong."

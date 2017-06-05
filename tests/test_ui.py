import pytest
import allure

text_for_ini = '''Курсы иностранных валют относятся только к физическим
лицам.Обратите внимание, при покупке или продаже валюты с использованием
карты, списание средств со счета карты проводится по курсу, действующему на
момент фактического списания, и может отличаться от курса на момент
совершения операции
Внимание! Курс по картам (за исключением операции карта-вклад)
 можно посмотреть здесь'''

header_title = 'Калькулятор иностранных валют'


@allure.feature('Check title and text information about currency changings')
def test_interface(glob_fixture):
    glob_fixture.open_home_page()
    glob_fixture.page_maximize()
    with pytest.allure.step('Assert test block'):
        assert glob_fixture.convertpage.check_text_header_block() == \
               text_for_ini, 'Header info is not match with excpected'
    with pytest.allure.step('Assert header is the same as expected'):
        assert glob_fixture.convertpage.get_page_header_title()\
               == header_title, "Header is wrong."

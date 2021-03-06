import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
import allure
import pytest


class ConverterLocators(object):
    SUM_CONVERTATION_FIELS = (
        By.XPATH,
        '//div[contains(@class, "rates-aside__filter-block-line-right")]'
        '/form/input')
    FROM_CURRENCY_FIELD = (
        By.XPATH,
        '//div[contains(@class, "rates-aside__filter-block-line-right")]'
        '/div')
    TO_CURRENCY_FIELD = (
        By.XPATH,
        '//div[contains(@class, "rates-aside__filter-block-line-right")]/div'
    )
    FROM_CURRENCY_SELECTOR = \
        '//select[contains(@name, "converterFrom")]/following-sibling::div'
    TO_CURRENCY_SELECTOR = '//select[contains(@name, "converterTo")]' \
                           '/following-sibling::div'
    MONEY_STRING_FROM = \
        '//select[contains(@name, "converterFrom")]/' \
        'following-sibling::div/div/span[text()="'
    MONEY_STRING_TO = \
        '//select[contains(@name, "converterTo")]/following-sibling::div' \
        '/div/span[text()="'
    FROM_CURRENCY_CURRENT = (
        By.XPATH,
        '//select[@name="converterFrom"]/following-sibling::div/header/strong'
    )
    TO_CURRENCY_CURRENT = (
        By.XPATH,
        '//select[@name="converterTo"]/following-sibling::div/header/strong')
    HEADER_TITLE = (By.XPATH, '//h1')
    LABEL_LIST_FROM_CONVERTATION = (By.XPATH, "")
    SOURCE_CASH = '//input[@name="sourceCode" and @value="cash"]'
    SOURCE_CARD = '//input[@name="sourceCode" and @value="card"]'
    SOURCE_ACCOUNT = '//input[@name="sourceCode" and @value="account"]'
    DESTINATION_CARD = '//input[@name="destinationCode" and @value="card"]'
    DESTINATION_ACCOUNT = '//input[@name="destinationCode"' \
                          ' and @value="account"]'
    DESTINATION_CASH = '//input[@name="destinationCode" and @value="cash"]'
    EXCHANGE_IBANK = '//input[@name="exchangeType" and @value="ibank"]'
    EXCHANGE_OFFICE = '//input[@name="exchangeType" and @value="office"]'
    EXCHANGE_ATM = '//input[@name="exchangeType" and @value="atm"]'
    SHOW_BUTTON_CONVERTER = (
        By.XPATH,
        '//div[contains(@class, "rates-aside__filter-block")]'
        '/button[contains(@class, "rates-button")]'
    )
    SELL_BUY_VALUE = (
        By.XPATH,
        '//td[contains(@class, "rates-current__table-cell_column_buy")]'
        '/span/span[contains(@class, '
        '"rates-current__rate-value")]'
    )
    SELL_SELL_VALUE = (
        By.XPATH,
        '//td[contains(@class, "rates-current__table-cell_column_sell")]'
        '/span/span[contains(@class, '
        '"rates-current__rate-value")]'
    )
    TOTAL_SUM = (By.XPATH, '//span[contains(@class, '
                           '"rates-converter-result__total-to")]')
    TEXT_BLOXK_HEADER = (By.XPATH, '//div[contains(@class, '
                                   '"rates-current__note")]')
    INPUT_PARENT = (By.XPATH, '//input[@name="exchangeType"'
                              ' and @value="ibank"]/parent::label')


class ConverterPage(BasePage):
    @staticmethod
    def create_locator_for_input(locator_string):
        locator = locator_string + "/following-sibling::span"
        return locator

    @staticmethod
    def create_locator_for_money(money, param):
        if param == 'From':
            locator = '//select[contains(@name, "converterFrom")]/' \
                      'following-sibling::div/div/span' \
                      '[text()={zn}{test}{zn}]'

        else:
            locator = '//select[contains(@name, "converterTo")]/' \
                      'following-sibling::div/div/span' \
                      '[text()={zn}{test}{zn}]'
        return locator.format(test=money, zn='"')

    @allure.step('Get page header title')
    def get_page_header_title(self):
        element = self.driver.find_element(*ConverterLocators.HEADER_TITLE)
        return element.text

    @allure.step('Caclulate sum exchanged currency')
    def calculated_sum(self, sum):
        elem = self.driver.find_element(*ConverterLocators.SELL_SELL_VALUE)
        val = elem.text.replace(',', '.')
        sum_counted = round(float(sum) / float(val), 2)
        return sum_counted

    @allure.step('Get auto-calculated sum')
    def get_total_sum(self):
        element = self.driver.find_element(*ConverterLocators.TOTAL_SUM)
        sum_string = float(element.text.replace(',', '.')[:-4])
        return sum_string

    @allure.step('Clear and type value {1} in sum field')
    def type_sum_convertation(self, param):
        element = self.driver.find_element(
            *ConverterLocators.SUM_CONVERTATION_FIELS)
        WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(@class,'
                           ' "rates-aside__filter-block-line-right")]'
                           '/form/input')))
        element.clear()
        with pytest.allure.step('Check sum fiels id empty'):
            assert not element.text, 'Field is not empty'
        element.send_keys(param, Keys.ENTER)
        with pytest.allure.step('Check sum fiels id has value={1}'):
            element_fin = self.driver.find_element(
                *ConverterLocators.SUM_CONVERTATION_FIELS)
            text = element_fin.get_attribute('value').replace(' ', '')
            assert text == param, 'Sum is not the same with typed'

    @allure.step('Check currency value {1} matched with test param{2}')
    def check_currency_selected(self, currency, param):
        if param == 'From':
            element = self.driver.find_element(
                *ConverterLocators.FROM_CURRENCY_CURRENT)
        else:
            element = self.driver.find_element(
                *ConverterLocators.FROM_CURRENCY_CURRENT)
        if currency == element.text:
            return True
        else:
            return False

    # Function can be optimized
    @allure.step('Select currency - {1}')
    def choose_from_currency_value(self, value, param):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        with pytest.allure.step(
                'Check that value of test is not selected'):
            if self.check_currency_selected(value, param):
                pass
            else:
                with pytest.allure.step('Select converted "from" value'):
                    if param == 'From':
                        WebDriverWait(self.driver, 100).until(
                            EC.element_to_be_clickable(
                                (By.XPATH,
                                 ConverterLocators.FROM_CURRENCY_SELECTOR
                                 )))
                        element = self.driver.find_element_by_xpath(
                            ConverterLocators.FROM_CURRENCY_SELECTOR)
                        element.click()
                        money_locator = self.create_locator_for_money(
                            value, param)
                        WebDriverWait(self.driver, 120).until(
                            EC.element_to_be_clickable(
                                (By.XPATH, money_locator)))
                        curency_elem = self.driver.find_element_by_xpath(
                            money_locator)
                        curency_elem.click()
                        with pytest.allure.step(
                                'Check value selected is correct'):
                            fin_element = self.driver.find_element_by_xpath(
                                ConverterLocators.FROM_CURRENCY_SELECTOR)
                            assert fin_element.text == param, \
                                'Value selected incorrect'
                    else:
                        with pytest.allure.step(
                                'Select converted "to" value'):
                            WebDriverWait(self.driver, 100).until(
                                EC.element_to_be_clickable(
                                    (By.XPATH,
                                     ConverterLocators.TO_CURRENCY_SELECTOR
                                     )))
                            element = self.driver.find_element_by_xpath(
                                ConverterLocators.TO_CURRENCY_SELECTOR)
                            element.click()
                            money_locator = self.create_locator_for_money(
                                value, param)
                            WebDriverWait(self.driver, 120).until(
                                EC.element_to_be_clickable(
                                    (By.XPATH, money_locator)))
                            curency_elem = self.driver.find_element_by_xpath(
                                money_locator)
                            curency_elem.click()
                            with pytest.allure.step(
                                    'Check value selected is correct'):
                                fin_element =\
                                    self.driver.find_element_by_xpath(
                                        ConverterLocators.TO_CURRENCY_SELECTOR)
                                assert fin_element.text == value,\
                                    'Value selected incorrect'

    def select_input_checkbox(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        atr = element.get_attribute('checked')
        if atr is not None:
            pass
        else:
            element_select = self.create_locator_for_input(locator)
            elem = self.driver.find_element_by_xpath(element_select)
            WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable(
                    (By.XPATH, element_select)))
            elem.click()

    @allure.step('Select source - {1}')
    def select_source(self, param):
        if param == 'account':
            self.select_input_checkbox(ConverterLocators.SOURCE_ACCOUNT)
        elif param == 'cash':
            self.select_input_checkbox(ConverterLocators.SOURCE_CASH)
        else:
            self.select_input_checkbox(ConverterLocators.SOURCE_CARD)

    @allure.step('Select destination - {1}')
    def select_destination(self, param):
        if param == 'account':
            self.select_input_checkbox(
                ConverterLocators.DESTINATION_ACCOUNT)
        elif param == 'cash':
            self.select_input_checkbox(ConverterLocators.DESTINATION_CASH)
        else:
            self.select_input_checkbox(ConverterLocators.DESTINATION_CARD)

    @allure.step('Select exchange - {1}')
    def select_exchange(self, param):
        if param == 'ibank':
            self.select_input_checkbox(ConverterLocators.EXCHANGE_IBANK)
        elif param == 'office':
            self.select_input_checkbox(ConverterLocators.EXCHANGE_OFFICE)
        else:
            self.select_input_checkbox(ConverterLocators.EXCHANGE_ATM)

    @allure.step('Check element is inactive')
    def get_check_status_element(self, locator):
        parent_xpath = locator + '/parent::label'
        element = self.driver.find_element_by_xpath(parent_xpath)
        class_name = element.get_attribute('class')
        if class_name == 'filter-inactive':
            return False
        else:
            return True

    @allure.step('Get page header')
    def check_text_header_block(self):
        element = self.driver.find_element(
            *ConverterLocators.TEXT_BLOXK_HEADER)
        return element.text

    @allure.step('Click show results button')
    def click_show_button(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def assert_page_info_text(self):
        element = self.driver.find_element(
            *ConverterLocators.TEXT_BLOXK_HEADER)
        real_text = element.text
        # Here we should use global variable for Path to root dir
        with open(
                os.path.join(os.path.dirname(__file__)[:-5],
                             "data/header_text.txt"),
                'r', encoding='utf-8') \
                as f:
            expected_text = ''.join(f.readlines())
        assert real_text == expected_text, "Texts are different"

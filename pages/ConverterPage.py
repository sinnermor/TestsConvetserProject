from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
import allure

class ConverterLocators(object):
    SUM_CONVERTATION_FIELS =(By.XPATH, '//div[contains(@class, "rates-aside__filter-block-line-right")]/form/input')
    FROM_CURRENCY_FIELD = (By.XPATH, '//div[contains(@class, "rates-aside__filter-block-line-right")]/div')
    TO_CURRENCY_FIELD = (By.XPATH, '//div[contains(@class, "rates-aside__filter-block-line-right")]/div')
    FROM_CURRENCY_SELECTOR = '//select[contains(@name, "converterFrom")]/following-sibling::div'
    TO_CURRENCY_SELECTOR = '//select[contains(@name, "converterTo")]/following-sibling::div'
    # FROM_CURRENCY_FIELD_EUR = (By.XPATH, '//select[contains(@name, "converterFrom")]/following-sibling::div/div/span[text()="EUR"]')
    MONEY_STRING_FROM = '//select[contains(@name, "converterFrom")]/following-sibling::div/div/span[text()="'
    MONEY_STRING_TO = '//select[contains(@name, "converterTo")]/following-sibling::div/div/span[text()="'
    FROM_CURRENCY_CURRENT = (By.XPATH, '//select[@name="converterFrom"]/following-sibling::div/header/strong')
    TO_CURRENCY_CURRENT = (By.XPATH, '//select[@name="converterTo"]/following-sibling::div/header/strong')
    HEADER_TITLE = (By.XPATH, '//h1')

    LABEL_LIST_FROM_CONVERTATION = (By.XPATH, "")

    SOURCE_CASH = '//input[@name="sourceCode" and @value="cash"]'
    SOURCE_CARD = '//input[@name="sourceCode" and @value="card"]'
    SOURCE_ACCOUNT = '//input[@name="sourceCode" and @value="account"]'

    DESTINATION_CARD = '//input[@name="destinationCode" and @value="card"]'
    DESTINATION_ACCOUNT = '//input[@name="destinationCode" and @value="account"]'
    DESTINATION_CASH = '//input[@name="destinationCode" and @value="cash"]'


    EXCHANGE_IBANK = '//input[@name="exchangeType" and @value="ibank"]'

    EXCHANGE_OFFICE = '//input[@name="exchangeType" and @value="office"]'
    EXCHANGE_ATM = '//input[@name="exchangeType" and @value="atm"]'


    SHOW_BUTTON_CONVERTER = (By.XPATH, '//div[contains(@class, "rates-aside__filter-block")]/button[contains(@class, "rates-button")]')

    SELL_BUY_VALUE = (By.XPATH, '//td[contains(@class, "rates-current__table-cell_column_buy")]/span/span[contains(@class, "rates-current__rate-value")]')
    SELL_SELL_VALUE =(By.XPATH, '//td[contains(@class, "rates-current__table-cell_column_sell")]/span/span[contains(@class, "rates-current__rate-value")]')

    TOTAL_SUM = (By.XPATH, '//span[contains(@class, "rates-converter-result__total-to")]')

#     Locators for ui
    TEXT_BLOXK_HEADER = (By.XPATH, '//div[contains(@class, "rates-current__note")]')
    INPUT_PARENT = (By.XPATH, '//input[@name="exchangeType" and @value="ibank"]/parent::label')




class ConverterPage(BasePage):


    def create_locator_for_input(self, locator_string):
        locator = locator_string + "/following-sibling::span"
        return locator

    def create_locator_for_money(self, money, param):
        if param == 'From':
            locator = ConverterLocators.MONEY_STRING_FROM + money + '''"]'''
        else:
            locator = ConverterLocators.MONEY_STRING_TO + money + '''"]'''
        return locator

    @allure.step('Get page headet title')
    def get_page_header_title(self):
        element = self.driver.find_element(ConverterLocators.HEADER_TITLE)
        return element.text

    @allure.step('Caclulate sum exchanged currency')
    def calculated_sum(self, sum):
        elem = self.driver.find_element(*ConverterLocators.SELL_SELL_VALUE)
        val = elem.text.replace(',','.')
        sum_counted = round(float(sum)/float(val),2)
        return sum_counted

    @allure.step('Get auto-calculated sum')
    def get_total_sum(self):
        element = self.driver.find_element(*ConverterLocators.TOTAL_SUM)
        sum_string = float(element.text.replace(',','.')[:-4])
        return sum_string



    @allure.step('Clear and type value {1} in sum field')
    def type_sum_convertation(self, param):
        element = self.driver.find_element(*ConverterLocators.SUM_CONVERTATION_FIELS)
        element.clear()
        element.send_keys(param, Keys.ENTER)


    @allure.step('Check currency value {1} matched with test param{2}')
    def check_currency_selected(self, currency, param):
        if param == 'From':
            element = self.driver.find_element(*ConverterLocators.FROM_CURRENCY_CURRENT)
        else: element = self.driver.find_element(*ConverterLocators.FROM_CURRENCY_CURRENT)
        if currency == element.text:
            return True
        else: return False

    @allure.step('Select currency - {1}')
    def choose_from_currency_value(self, value, param):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if self.check_currency_selected(value, param):
            pass
        else:
            if param == 'From':
                WebDriverWait(self.driver, 100).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, ConverterLocators.FROM_CURRENCY_SELECTOR)))
                element = self.driver.find_element_by_xpath(ConverterLocators.FROM_CURRENCY_SELECTOR)
                element.click()
            else :
                WebDriverWait(self.driver, 100).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, ConverterLocators.TO_CURRENCY_SELECTOR)))
                element = self.driver.find_element_by_xpath(ConverterLocators.TO_CURRENCY_SELECTOR)
                element.click()
            money_locator = self.create_locator_for_money(value, param)
            WebDriverWait(self.driver, 120).until(
                EC.element_to_be_clickable(
                    (By.XPATH, money_locator)))
            selector = self.driver.find_element_by_xpath(money_locator)
            selector.click()

    def select_input_checkbox(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        atr = element.get_attribute('checked')
        if atr != None:
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
        else: self.select_input_checkbox(ConverterLocators.SOURCE_CARD)

    @allure.step('Select destination - {1}')
    def select_destination(self, param):
        if param == 'account':
            self.select_input_checkbox(ConverterLocators.DESTINATION_ACCOUNT)
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
        else: return True

    @allure.step('Get page header')
    def check_text_header_block(self, string):
        element = self.driver.find_element(*ConverterLocators.TEXT_BLOXK_HEADER)
        return element.text

    # @allure.step('Click show results button')
    def click_show_button(self, locator):
        element = self.driver.find_element(*(locator))
        element.click()


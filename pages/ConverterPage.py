from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
# import allure

class ConverterLocators(object):
    SUM_CONVERTATION_FIELS =(By.XPATH, '//div[contains(@class, "rates-aside__filter-block-line-right")]/form/input')
    FROM_CURRENCY_FIELD = (By.XPATH, '//div[contains(@class, "rates-aside__filter-block-line-right")]/div')
    FROM_CURRENCY_SELECTOR = (By.XPATH, '//select[contains(@name, "converterFrom")]')
    FROM_CURRENCY_FIELD_EUR = (By.XPATH, '//select[contains(@name, "converterFrom")]/following-sibling::div/div/span[text()="EUR"]')

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





class ConverterPage(BasePage):


    def create_locator_for_input(self, locator_string):
        locator = locator_string + "/following-sibling::span"
        return locator


    # @allure.step('Type value {1} in sum field')
    def type_sum_convertation(self, param):
        element = self.driver.find_element(*ConverterLocators.SUM_CONVERTATION_FIELS)
        element.send_keys(param, Keys.ENTER)

    # @allure.step()
    def choose_from_currency_value(self, value):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(@class, "rates-aside__filter-block-line-right")]/div')))
        element = self.driver.find_element(*ConverterLocators.FROM_CURRENCY_FIELD)
        element.click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//select[contains(@name, "converterFrom")]/following-sibling::div/div')))
        selector = self.driver.find_element(*ConverterLocators.FROM_CURRENCY_FIELD_EUR)
        selector.click()

    def select_input_checkbox(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        atr = element.get_attribute('checked')
        if atr != None:
            pass
        else:
            element_select = self.create_locator_for_input(locator)
            elem = self.driver.find_element_by_xpath(element_select)
            WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable(
                    (By.XPATH, element_select)))
            elem.click()

    def select_source(self, param):
        if param == 'account':
            self.select_input_checkbox(ConverterLocators.SOURCE_ACCOUNT)
        elif param == 'cash':
            self.select_input_checkbox(ConverterLocators.SOURCE_CASH)
        else: self.select_input_checkbox(ConverterLocators.SOURCE_CARD)

    def select_destination(self, param):
        if param == 'account':
            self.select_input_checkbox(ConverterLocators.DESTINATION_ACCOUNT)
        elif param == 'cash':
            self.select_input_checkbox(ConverterLocators.DESTINATION_CASH)
        else:
            self.select_input_checkbox(ConverterLocators.DESTINATION_CARD)

    def select_exchange(self, param):
        if param == 'ibank':
            self.select_input_checkbox(ConverterLocators.EXCHANGE_IBANK)
        elif param == 'office':
            self.select_input_checkbox(ConverterLocators.EXCHANGE_OFFICE)
        else:
            self.select_input_checkbox(ConverterLocators.EXCHANGE_ATM)



    def click_show_button(self, locator):
        element = self.driver.find_element(*(locator))
        element.click()


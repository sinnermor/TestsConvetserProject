
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
# import allure

class ConverterLocators(object):
    SUM_CONVERTATION_FIELS =(By.XPATH, "//div[contains(@class, 'rates-aside__filter-block-line-right')]/form/input")
    FROM_CURRENCY_FIELD = (By.XPATH, "//div[contains(@class, 'rates-aside__filter-block-line-right')]/div")
    FROM_CURRENCY_SELECTOR = (By.XPATH, "//select[contains(@name, 'converterFrom')]")
    FROM_CURRENCY_FIELD_EUR = (By.XPATH, '//select[contains(@name, "converterFrom")]/following-sibling::div/div/span[text()="EUR"]')

    SOURCE_CARD = (By.XPATH, "//input[@name='sourceCode' and @value='card']")
    SOURCE_ACCOUNT = (By.XPATH, "//input[@name='sourceCode' and @value='account']")
    SOURCE_CASH = (By.XPATH, "//input[@name='sourceCode' and @value='cash']")

    DESTINATION_CARD = (By.XPATH, "//input[@name='destinationCode' and @value='card']")
    DESTINATION_ACCOUNT = (By.XPATH, "//input[@name='destinationCode' and @value='account']")
    DESTINATION_CASH = (By.XPATH, "//input[@name='destinationCode' and @value='cash']")

    EXCHANGE_IBANK = (By.XPATH, "//input[@name='exchangeType' and @value='ibank']")
    EXCHANGE_OFFICE = (By.XPATH, "//input[@name='exchangeType' and @value='office']")
    EXCHANGE_ATM = (By.XPATH, "//input[@name='exchangeType' and @value='atm']")




class ConverterPage(BasePage):

    # def create_locator_for_input(self, name, value):


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
            EC.element_to_be_clickable(
                (By.XPATH, '//select[contains(@name, "converterFrom")]/following-sibling::div/div')))
        selector = self.driver.find_element(*ConverterLocators.FROM_CURRENCY_FIELD_EUR)
        selector.click()

    def select_input_checkbox(self, locator):
        element = self.driver.find_element(*(locator))
        element.click()



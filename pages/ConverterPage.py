
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
# import allure

class ConverterLocators(object):
    SUM_CONVERTATION_FIELS =(By.XPATH, "//div[contains(@class, 'rates-aside__filter-block-line-right')]/form/input")
    FROM_CURRENCY_FIELD = (By.XPATH, "//div[contains(@class, 'rates-aside__filter-block-line-right')]/div/header/em")
    FROM_CURRENCY_SELECTOR = (By.XPATH, "//select[contains(@name, 'converterFrom')]")



class ConverterPage(BasePage):

    # @allure.step('Type value {1} in sum field')
    def type_sum_convertation(self, param):
        element = self.driver.find_element(*ConverterLocators.SUM_CONVERTATION_FIELS)
        element.send_keys(param, Keys.ENTER)


    def choose_from_currency_value(self, value):

        element = self.driver.find_element(*ConverterLocators.FROM_CURRENCY_FIELD)
        element.click()

        #
        select = Select(self.driver.find_element(*ConverterLocators.FROM_CURRENCY_SELECTOR))
        select.select_by_visible_text(value).send_keys(Keys.ENTER)



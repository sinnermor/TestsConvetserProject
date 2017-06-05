from selenium.webdriver.support.ui import WebDriverWait
import sys
import logging
from pages.ConverterPage import ConverterPage
import allure
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


# Fixture base class
class GlobalFixture:

    # Fixture construstor, create Driver and declare all pages for tests
    def __init__(self, base_url, driver):
        self.driver = driver
        self.url = base_url
        self.driver.implicitly_wait(10)
        logging.info("initialized {}".format(self))
        self.convertpage = ConverterPage(self)

    # Maximise window for tests
    @allure.step('Maximize window')
    def page_maximize(self):
        self.driver.maximize_window()
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script(
            'return document.readyState') == 'complete')

    # Open page with base url
    @allure.step('Open main page')
    def open_home_page(self):
            self.driver.get(self.url)
            WebDriverWait(self.driver, 20).until(lambda d: d.execute_script(
                'return document.readyState') == 'complete')

    # Open any page with url - parametrized
    @allure.step('Open page URL {1}')
    def open_page(self, string):
        self.driver.get(self.url + string)
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script(
            'return document.readyState') == 'complete')

    # Destroy fixture. Close test window
    def destroy(self):
        self.driver.quit()

import Config

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:


    def __init__(self, driver):
        self.driver = driver
        self.url = Config.url


    def find_element(self, locator):
        return WebDriverWait(self.driver).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return WebDriverWait(self.driver).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.url)

    def go_for_tv(self):
        self.url_for_tv = Config.url_for_tv
        return self.driver.get(self.url_for_tv)
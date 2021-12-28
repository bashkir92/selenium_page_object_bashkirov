from BasePage import BasePage
from selenium.webdriver.common.by import By

class YandexTVLocators:

    LOCATOR_YANDEX_TV = (By.LINK_TEXT, "Программа")
    LOCATOR_CATEGORY_TV = (By.CLASS_NAME, 'dropdown')
    LOCATOR_FILMS_AND_SERIALS = (By.CLASS_NAME, "select__item")
    LOCATOR_CHANNEL_KINOPREMIERA = (By.CLASS_NAME, 'grid-channel__title')

class TVhHelper(BasePage):

    def go_to_tv(self):
        return self.find_element(YandexTVLocators.LOCATOR_YANDEX_TV).click()

    def view_category_tv(self):
        return self.find_element(YandexTVLocators.LOCATOR_CATEGORY_TV).click()

    def go_to_films_and_serials(self):
        list =  self.find_elements(YandexTVLocators.LOCATOR_FILMS_AND_SERIALS)
        list[3].click()

    def list_channel_films_and_serials(self):
        list_channel = []
        a = self.find_elements(YandexTVLocators.LOCATOR_CHANNEL_KINOPREMIERA)
        for i in a:
            one = i.text
            list_channel.append(one)
        return list_channel



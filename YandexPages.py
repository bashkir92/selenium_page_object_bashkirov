from BasePage import BasePage
from selenium.webdriver.common.by import By

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_IMAGE = (By.LINK_TEXT, 'Картинки')
    LOCATOR_YANDEX_ON_TELEPHONE = (By.LINK_TEXT, 'на телефон')
    LOCATOR_YANDEX_ON_TELEPHONE_ASSERT = (By.NAME, "text")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON).click()

    def click_on_image(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_IMAGE).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def click_on_telephone(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_ON_TELEPHONE).click()

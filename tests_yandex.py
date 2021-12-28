from YandexPages import SearchHelper
from selenium.webdriver.common.by import By

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Hello")
    yandex_main_page.click_on_the_search_button()
    elements = yandex_main_page.check_navigation_bar()
    assert "Картинки" and "Видео" in elements

def test_yandex_image(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Обои")
    yandex_main_page.click_on_the_search_button()
    yandex_main_page.click_on_image()
    window_after = browser.window_handles[1]
    browser.switch_to_window(window_after)
    yandex_main_page.click_on_telephone()
    browser.refresh()
    log = browser.find_element(By.NAME, "text")
    attrs = []
    for attr in log.get_property('attributes'):
        attrs.append([attr['name'], attr['value']])
    assert attrs[3] == ['value', 'Обои на телефон']
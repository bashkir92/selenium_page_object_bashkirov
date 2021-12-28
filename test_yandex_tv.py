from YandexTV import TVhHelper

def test_yandex_tv_channel(browser):
    yandex_tv_page = TVhHelper(browser)
    yandex_tv_page.go_for_tv()
    yandex_tv_page.go_to_tv()
    window_after = browser.window_handles[1]
    browser.switch_to_window(window_after)
    yandex_tv_page.view_category_tv()
    yandex_tv_page.go_to_films_and_serials()
    list_channel = yandex_tv_page.list_channel_films_and_serials()
    assert 'Кинохит' in list_channel, 'Данный канал отсутствует в списке'
    assert 'Hollywood' in list_channel, 'Данный канал отсутствует в списке'
    assert 'TV1000' in list_channel, 'Данный канал отсутствует в списке'
    assert 'TV XXI' in list_channel, 'Данный канал отсутствует в списке'
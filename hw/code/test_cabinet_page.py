from base_case import BaseCase

left_menu_sections = [
    ('Аудитории', 'https://ads.vk.com/hq/audience'),
    ('Бюджет', 'https://ads.vk.com/hq/budget/transactions'),
    ('Центр коммерции', 'https://ads.vk.com/hq/ecomm/catalogs'),
    ('Лид-формы и опросы', 'https://ads.vk.com/hq/leadads/leadforms'),
    ('Настройки', 'https://ads.vk.com/hq/settings'),
    ('Обзор', 'https://ads.vk.com/hq/overview'),
]


class TestCabinetPage(BaseCase):
    def test_go_to_left_menu_sections(self, cabinet_page):
        for section_name, url in left_menu_sections:
            cabinet_page.click_left_menu(section_name)
            assert self.is_opened(url)
            cabinet_page.click_close_button_if_education_is_offered()

    def test_replenishment_modal_page_became_visible(self, cabinet_page):
        cabinet_page.click_balance_button()
        assert cabinet_page.replenishment_modal_page_became_visible()

    def test_notifications_modal_page_became_visible(self, cabinet_page):
        cabinet_page.click_notifications_button()
        assert cabinet_page.notifications_modal_page_became_visible()

    def test_user_menu_became_visible(self, cabinet_page):
        cabinet_page.click_user_avatar()
        assert cabinet_page.user_menu_became_visible()

    def test_logout(self, cabinet_page):
        cabinet_page.click_user_avatar()
        cabinet_page.click_logout_button()
        assert self.is_opened('https://ads.vk.com/')

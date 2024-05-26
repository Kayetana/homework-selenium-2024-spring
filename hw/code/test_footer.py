from base_case import BaseCase
from ui.fixtures import main_page
import pytest


class TestFooter(BaseCase):
    def test_go_to_auth(self, main_page):
        main_page.click_footer_cabinet_button()
        assert self.is_opened('https://id.vk.com/auth')

    @pytest.mark.parametrize("item_name,url,open_in_new_tab", [
        ('Новости', 'https://ads.vk.com/news', False),
        ('Полезные материалы', 'https://ads.vk.com/insights', False),
        ('Мероприятия', 'https://ads.vk.com/events', False),
        ('Документы', 'https://ads.vk.com/documents', False),
        ('Обучение для бизнеса', 'https://expert.vk.com/', True),
        ('Кейсы', 'https://ads.vk.com/cases', False),
        ('Помощь', 'https://ads.vk.com/help', False),
        ('Монетизация', 'https://ads.vk.com/partner', True),
    ])
    def test_go_to_sections(self, main_page, item_name, url, open_in_new_tab):
        main_page.click_footer_item(item_name)
        if open_in_new_tab:
            main_page.go_to_new_tab()
        assert self.is_opened(url)

    def test_go_to_vk_business(self, main_page):
        main_page.click_vk_business_logo()
        main_page.go_to_new_tab()
        assert self.is_opened('https://vk.company/ru/company/business/')

    def test_change_language(self, main_page):
        main_page.change_language('English')
        assert main_page.get_selected_language_from_footer() == 'EN'

        main_page.change_language('Русский')
        assert main_page.get_selected_language_from_footer() == 'RU'

    @pytest.mark.parametrize("social_media_url", [
        'https://vk.com/vk_ads',
        'https://ok.ru/group/64279825940712',
        'https://t.me/vk_ads'
    ])
    def test_go_to_social_media(self, main_page, social_media_url):
        main_page.click_social_media_item(social_media_url)
        main_page.go_to_new_tab()
        assert self.is_opened(social_media_url)

    def test_go_to_about(self, main_page):
        main_page.click_footer_about()
        main_page.go_to_new_tab()
        assert self.is_opened('https://vk.company/ru/')

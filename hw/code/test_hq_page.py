import time

import pytest

from base_case import BaseCase

left_menu_sections = [
    ('Аудитории', 'https://ads.vk.com/hq/audience'),
    ('Бюджет', 'https://ads.vk.com/hq/budget/transactions'),
    ('Обзор', 'https://ads.vk.com/hq/overview'),
    ('Лид-формы', 'https://ads.vk.com/hq/leadads/leadforms'),
    ('Настройки', 'https://ads.vk.com/hq/settings'),
]


class TestHqPage(BaseCase):
    def test_go_to_left_menu_sections(self, hq_page):
        for section_name, url in left_menu_sections:
            hq_page.click_left_menu(section_name)
            assert self.is_opened(url)

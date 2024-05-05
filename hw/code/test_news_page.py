from base_case import BaseCase


class TestNewsPage(BaseCase):
    def test_title_is_displayed(self, news_page):
        assert news_page.get_page_title() == 'Новости'

    def test_go_to_page_of_news(self, news_page):
        news_title = news_page.get_news_title()
        news_page.click_news_item()

        assert self.is_opened('https://ads.vk.com/news/')
        assert news_page.get_page_title() == news_title

import time

from base_case import BaseCase


class TestUpvotePage(BaseCase):
    def test_open_comments(self, upvote_page):
        upvote_page.click_comment_button()
        assert upvote_page.comments_is_on_page()

    def test_check_comments_count(self, upvote_page):
        upvote_page.click_comment_button()
        assert upvote_page.get_comment_counter_from_button() == upvote_page.count_comment_items()

    def test_search_by_title(self, upvote_page):
        word = 'видео'
        upvote_page.perform_search(word)
        time.sleep(1)
        assert word in upvote_page.get_first_idea_title()

    def test_search_by_id(self, upvote_page):
        idea_id = '40'
        upvote_page.perform_search(idea_id)
        time.sleep(1)
        assert idea_id == upvote_page.get_first_idea_id()

    def test_open_theme_dropdown(self, upvote_page):
        upvote_page.open_filter_dropdown('Любая тема')

        themes = [
            'Лидформы',
            'Сообщества',
            'Форум идей',
            'Сайты',
            'Каталог товаров',
            'Мобильные приложения',
            'Другое'
        ]

        assert upvote_page.filter_dropdown_contain_items(themes)

    def test_open_status_dropdown(self, upvote_page):
        upvote_page.click_cancel_filter_button()
        upvote_page.open_filter_dropdown('Любой статус')

        statuses = [
            'Голосование',
            'Уже в работе',
            'Реализована',
            'Отклонено'
        ]

        assert upvote_page.filter_dropdown_contain_items(statuses)

    def test_filter_theme(self, upvote_page):
        upvote_page.open_filter_dropdown('Любая тема')

        theme = 'Лидформы'
        upvote_page.select_filter(theme)
        assert upvote_page.get_first_idea_theme() == theme

    def test_filter_status(self, upvote_page):
        upvote_page.click_cancel_filter_button()
        upvote_page.open_filter_dropdown('Любой статус')

        status = 'Уже в работе'
        upvote_page.select_filter(status)
        assert upvote_page.get_first_idea_status() == status

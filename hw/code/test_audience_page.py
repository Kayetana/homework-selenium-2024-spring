from datetime import datetime
from base_case import BaseCase

CUSTOM_AUDIENCE_NAME = 'MusicOn ' + datetime.now().strftime('%d-%m-%Y')
SOURCE_TITLE = 'MusicOn source'
KEY_PHRASES = ['music', 'tracks']
NEGATIVE_PHRASES = ['remixes']
SEARCH_PERIOD_IN_DAYS = 30


class TestAudiencePage(BaseCase):

    def test_error_long_audience_name(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.enter_audience_name('a' * (audience_page.MAX_LENGTH_OF_AUDIENCE_NAME + 1))
        assert audience_page.get_error() == audience_page.ERROR_TOO_LONG_AUDIENCE_NAME

    def test_add_source_by_key_phrases(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.add_key_phrases_source(SOURCE_TITLE, KEY_PHRASES, NEGATIVE_PHRASES, SEARCH_PERIOD_IN_DAYS)

        assert audience_page.get_source_title_on_card() == SOURCE_TITLE
        assert audience_page.get_key_phrases_on_card() == KEY_PHRASES
        assert audience_page.get_negative_phrases_on_card() == NEGATIVE_PHRASES
        assert audience_page.get_search_period_on_card() == SEARCH_PERIOD_IN_DAYS

    def test_create_audience(self, audience_page):
        audience_page.click_create_audience_button()

        audience_page.add_key_phrases_source(SOURCE_TITLE, KEY_PHRASES, NEGATIVE_PHRASES, SEARCH_PERIOD_IN_DAYS)
        audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
        audience_page.click_submit_audience_button()

        assert audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME

        audience_page.delete_audience()
        audience_page.wait_until_audience_deleted()

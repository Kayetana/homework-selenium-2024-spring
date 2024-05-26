import pytest
from datetime import datetime
from base_case import BaseCase

CUSTOM_AUDIENCE_NAME = 'MusicOn ' + datetime.now().strftime('%d-%m-%Y')
SOURCE_NAME = 'Ключевые фразы'
KEY_PHRASES = ['music', 'tracks']
NEGATIVE_PHRASES = ['']
SEARCH_PERIOD_IN_DAYS = 30


@pytest.fixture
def create_audience_modal_page(audience_page):
    audience_page.click_create_audience_button()


@pytest.fixture
def key_phrases_source(create_audience_modal_page, audience_page):
    audience_page.click_add_source_button()
    audience_page.select_source(SOURCE_NAME)
    audience_page.enter_key_phrases(KEY_PHRASES)
    audience_page.click_modal_page_submit_button()


class TestAudiencePage(BaseCase):
    def test_default_audience_name(self, create_audience_modal_page, audience_page):
        assert audience_page.get_default_audience_name() == audience_page.DEFAULT_AUDIENCE_NAME

    def test_error_long_audience_name(self, create_audience_modal_page, audience_page):
        audience_page.enter_audience_name('a' * (audience_page.MAX_LENGTH_OF_AUDIENCE_NAME + 1))
        assert audience_page.get_error() == audience_page.ERROR_TOO_LONG_AUDIENCE_NAME

    def test_add_source_by_key_phrases(self, key_phrases_source, audience_page):
        source_card_content = audience_page.get_source_card_content()
        for key_phrase in KEY_PHRASES:
            assert key_phrase in source_card_content

    def test_create_audience(self, key_phrases_source, audience_page):
        audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
        assert audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME
        audience_page.delete_audience()

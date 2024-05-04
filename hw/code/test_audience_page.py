import time

from base_case import BaseCase
from datetime import datetime


payload = {
    'name': 'MusicOn ' + datetime.now().strftime('%d-%m-%Y'),
    'key_phrases': 'music'
}


class TestAudiencePage(BaseCase):
    def test_default_audience_name(self, audience_page):
        audience_page.click_create_audience()
        assert audience_page.get_default_audience_name() == 'Аудитория ' + datetime.now().strftime('%Y-%m-%d')

    def test_error_long_audience_name(self, audience_page):
        audience_page.click_create_audience()
        audience_page.enter_audience_name('name' * 64)
        assert audience_page.get_error() == 'Максимальная длина 255 символов'

    def test_add_source(self, audience_page):
        audience_page.click_create_audience()
        audience_page.add_source_by_key_phrases(payload['key_phrases'])
        assert 2 == 2

    def test_create_audience(self, audience_page):
        audience_page.click_create_audience()
        audience_page.enter_audience_name(payload['name'])
        time.sleep(5)
        audience_page.add_source_by_key_phrases(payload['key_phrases'])
        time.sleep(5)
        audience_page.submit_audience()
        time.sleep(5)

        assert audience_page.get_created_audience_title() == payload['name']

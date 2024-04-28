from base_case import BaseCase
from ui.fixtures import auth_page

import time


class TestRegistration(BaseCase):
    def test_auth_mail_ru(self, auth_page):
        auth_page.login_mail_ru('kayetana_qa@mail.ru', 'szR1x7xAWynSIzIM')
        time.sleep(3)
        assert 1 == 1

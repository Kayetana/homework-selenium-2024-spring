from base_case import BaseCase
import time


class TestPartner(BaseCase):
    def test_is_button_disabled(self, partner_page):
        assert partner_page.check_if_button_is_disabled()


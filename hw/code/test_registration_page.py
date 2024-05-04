import pytest

from base_case import BaseCase
from ui.pages.registration_page import RegistrationNewPage


class TestRegistrationPage(BaseCase):
    def test_open_new_cabinet_registration(self, credentials, registration_page):
        registration_page.go_to_new_cabinet_registration(*credentials)
        assert self.is_opened(RegistrationNewPage.url)

    def test_checked_language(self, registration_new_page):
        assert registration_new_page.get_selected_language() == 'Русский'
        registration_new_page.select_language('English')
        assert registration_new_page.get_selected_language() == 'English'
        registration_new_page.select_language('Русский')
        assert registration_new_page.get_selected_language() == 'Русский'

    @pytest.mark.parametrize("country,currencies", [
        ('Казахстан', ('Доллар США (USD)', 'Евро (EUR)')),
        ('Россия', ('Российский рубль (RUB)',)),
    ])
    def test_currency_dropdown(self, registration_new_page, country, currencies):
        registration_new_page.select_country(country)
        assert registration_new_page.currency_dropdown_contain_items(currencies)

    def test_error_empty_email(self, registration_new_page):
        registration_new_page.click_submit_button()
        assert registration_new_page.get_email_error() == 'Обязательное поле'

    def test_incorrect_email(self, registration_new_page):
        registration_new_page.enter_email('incorrect@email')
        registration_new_page.click_submit_button()
        assert registration_new_page.get_email_error() == 'Некорректный email адрес'

    def test_error_unaccepted_offer(self, registration_new_page):
        registration_new_page.click_offer_checkbox()
        registration_new_page.click_submit_button()
        assert registration_new_page.get_offer_error() == 'Обязательное поле'

    @pytest.mark.parametrize("incorrect_inn,error", [
        ('1003035398', 'Минимальная длина 12'),
        ('10030353984300', 'Максимальная длина 12 символов')
    ])
    def test_error_inn(self, registration_new_page, incorrect_inn, error):
        registration_new_page.enter_inn(incorrect_inn)
        registration_new_page.click_submit_button()
        assert registration_new_page.get_inn_error() == error

    def test_account_types(self, registration_new_page):
        registration_new_page.select_account_type('Агентство')
        assert registration_new_page.physical_type_became_invisible()

        registration_new_page.select_account_type('Рекламодатель')
        assert registration_new_page.physical_type_became_visible()

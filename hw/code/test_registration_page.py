import pytest
from base_case import BaseCase


@pytest.fixture
def new_cabinet(registration_page):
    registration_page.click_create_new_cabinet_button()


class TestRegistrationPage(BaseCase):
    def test_open_new_cabinet_registration(self, new_cabinet):
        assert self.is_opened('https://ads.vk.com/hq/registration/new')

    def test_checked_language(self, new_cabinet, registration_page):
        assert registration_page.get_selected_language() == 'Русский'
        registration_page.select_language('English')
        assert registration_page.get_selected_language() == 'English'
        registration_page.select_language('Русский')
        assert registration_page.get_selected_language() == 'Русский'

    @pytest.mark.parametrize("country,currencies", [
        ('Казахстан', ('Доллар США (USD)', 'Евро (EUR)')),
        ('Россия', ('Российский рубль (RUB)',)),
    ])
    def test_currency_dropdown(self, new_cabinet, registration_page, country, currencies):
        registration_page.select_country(country)
        assert registration_page.currency_dropdown_contain_items(currencies)

    def test_error_empty_email(self, new_cabinet, registration_page):
        registration_page.click_submit_button()
        assert registration_page.get_email_error() == 'Обязательное поле'

    def test_incorrect_email(self, new_cabinet, registration_page):
        registration_page.enter_email('incorrect@email')
        registration_page.click_submit_button()
        assert registration_page.get_email_error() == 'Некорректный email адрес'

    def test_error_unaccepted_offer(self, new_cabinet, registration_page):
        registration_page.click_offer_checkbox()
        registration_page.click_submit_button()
        assert registration_page.get_offer_error() == 'Обязательное поле'

    @pytest.mark.parametrize("incorrect_inn,error", [
        ('1003035398', 'Минимальная длина 12'),
        ('10030353984300', 'Максимальная длина 12 символов')
    ])
    def test_error_inn(self, new_cabinet, registration_page, incorrect_inn, error):
        registration_page.enter_inn(incorrect_inn)
        registration_page.click_submit_button()
        assert registration_page.get_inn_error() == error

    def test_account_types(self, new_cabinet, registration_page):
        registration_page.select_account_type('Агентство')
        assert registration_page.physical_type_became_invisible()

        registration_page.select_account_type('Рекламодатель')
        assert registration_page.physical_type_became_visible()

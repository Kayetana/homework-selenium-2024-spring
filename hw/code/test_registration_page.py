import pytest
from base_case import BaseCase
from ui.pages.cabinet_page import CabinetPage
from ui.pages.settings_page import SettingsPage

EMAIL = 'kayetana@gmail.com'


@pytest.fixture
def new_cabinet(registration_page):
    registration_page.click_create_new_cabinet_button()


class TestRegistrationPage(BaseCase):
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

    def test_register_cabinet(self, new_cabinet, registration_page):
        registration_page.enter_email(EMAIL)
        registration_page.click_submit_button()

        assert self.is_opened(CabinetPage.url)

        self.load_url(SettingsPage.url)
        settings_page = SettingsPage(self.get_driver())

        assert settings_page.get_email_general_field_value() == EMAIL

        settings_page.delete_cabinet()

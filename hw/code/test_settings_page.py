from base_case import BaseCase


class TestSettingsPage(BaseCase):
    FULL_NAME = 'Тест'
    INN = '526317984689'

    def test_error_invalid_phone_number(self, settings_page):
        settings_page.enter_phone_number('79221110500')
        settings_page.click_save_button()
        assert settings_page.get_phone_number_error() == settings_page.ERROR_INVALID_PHONE_NUMBER

    def test_additional_email_inputs_became_visible(self, settings_page):
        email_fields_counter = 0
        settings_page.click_add_email_button()
        assert settings_page.additional_email_input_became_visible(email_fields_counter)

        email_fields_counter += 1
        settings_page.click_add_email_button()
        assert settings_page.additional_email_input_became_visible(email_fields_counter)

        email_fields_counter += 1
        settings_page.click_add_email_button()
        assert settings_page.additional_email_input_became_visible(email_fields_counter)

    def test_error_invalid_email(self, settings_page):
        settings_page.click_add_email_button()
        settings_page.enter_email('invalid')
        settings_page.click_save_button()
        assert settings_page.get_email_error() == settings_page.ERROR_INVALID_EMAIL

    def test_error_empty_email(self, settings_page):
        settings_page.click_add_email_button()
        settings_page.enter_email('')
        settings_page.click_save_button()
        assert settings_page.get_email_error() == settings_page.ERROR_EMPTY_FIELD

    def test_error_too_short_inn(self, settings_page):
        settings_page.enter_inn('111111')
        settings_page.click_save_button()
        assert settings_page.get_inn_error() == settings_page.ERROR_TOO_SHORT_INN

    def test_error_invalid_inn(self, settings_page):
        settings_page.enter_inn('11111111111a')
        settings_page.click_save_button()
        assert settings_page.get_inn_error() == settings_page.ERROR_INVALID_INN

    def test_logout_other_devices(self, settings_page):
        settings_page.click_logout_other_devices_button()
        assert settings_page.logout_devices_success_message_became_visible()

    def test_cancel_changes(self, settings_page):
        initial_full_name = settings_page.get_full_name_field_value()

        settings_page.enter_full_name(self.FULL_NAME)
        assert settings_page.get_full_name_field_value() == self.FULL_NAME

        settings_page.click_cancel_button()
        assert settings_page.get_full_name_field_value() == initial_full_name

    def test_save_changes(self, settings_page):
        initial_full_name = settings_page.get_full_name_field_value()
        initial_inn = settings_page.get_inn_field_value()

        settings_page.enter_full_name(self.FULL_NAME)
        settings_page.enter_inn(self.INN)

        settings_page.click_save_button()
        self.get_driver().refresh()

        assert settings_page.get_full_name_field_value() == self.FULL_NAME
        assert settings_page.get_inn_field_value() == self.INN

        settings_page.enter_full_name(initial_full_name)
        settings_page.enter_inn(initial_inn)
        settings_page.click_save_button()

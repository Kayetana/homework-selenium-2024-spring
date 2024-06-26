from selenium.webdriver.support import expected_conditions as ec
from ui.pages.base_page import BasePage
from ui.locators.settings_page_locators import SettingsPageLocators


class SettingsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings'
    locators = SettingsPageLocators()

    ERROR_INVALID_PHONE_NUMBER = 'Некорректный номер телефона'
    ERROR_INVALID_EMAIL = 'Некорректный email адрес'
    ERROR_EMPTY_FIELD = 'Обязательное поле'
    ERROR_TOO_SHORT_INN = 'Длина ИНН должна быть 12 символов'
    ERROR_INVALID_INN = 'Некорректный ИНН'

    def enter_full_name(self, full_name: str):
        full_name_input = self.find(self.locators.FULL_NAME_INPUT)
        full_name_input.clear()
        full_name_input.send_keys(full_name)

    def get_full_name_field_value(self) -> str:
        return self.find(self.locators.FULL_NAME_INPUT).get_attribute('value')

    def get_email_general_field_value(self) -> str:
        return self.find(self.locators.EMAIL_GENERAL_INPUT).get_attribute('value')

    def get_inn_field_value(self) -> str:
        return self.find(self.locators.INN_INPUT).get_attribute('value')

    def enter_phone_number(self, phone_number: str):
        phone_number_input = self.find(self.locators.PHONE_NUMBER_INPUT)
        phone_number_input.clear()
        phone_number_input.send_keys(phone_number)

    def get_phone_number_error(self) -> str:
        return self.find(self.locators.PHONE_NUMBER_ERROR).text

    def click_add_email_button(self):
        self.click(self.locators.ADD_EMAIL_BUTTON)

    def additional_email_input_became_visible(self, counter: int) -> bool:
        return self.became_visible(self.locators.ADDITIONAL_EMAIL_INPUT(counter))

    def enter_email(self, email: str, counter: int = 0):
        email_input = self.find(self.locators.ADDITIONAL_EMAIL_INPUT(counter))
        email_input.clear()
        email_input.send_keys(email)

    def get_email_error(self) -> str:
        return self.find(self.locators.EMAIL_ERROR).text

    def get_full_name_error(self) -> str:
        return self.find(self.locators.FULL_NAME_ERROR).text

    def enter_inn(self, inn: str):
        inn_input = self.find(self.locators.INN_INPUT)
        inn_input.clear()
        inn_input.send_keys(inn)

    def get_inn_error(self) -> str:
        return self.find(self.locators.INN_ERROR).text

    def click_logout_other_devices_button(self):
        self.click(self.locators.LOGOUT_OTHER_DEVICES_BUTTON)

    def logout_devices_success_message_became_visible(self) -> bool:
        return self.became_visible(self.locators.LOGOUT_OTHER_DEVICES_SUCCESS_MESSAGE)

    def click_save_button(self):
        self.scroll_and_click(self.locators.SAVE_BUTTON)

    def click_cancel_button(self):
        self.scroll_and_click(self.locators.CANCEL_BUTTON)

    def delete_cabinet(self):
        self.scroll_and_click(self.locators.DELETE_CABINET_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_CABINET_BUTTON)
        self.wait().until(ec.invisibility_of_element(self.locators.DELETE_MODAL_PAGE))

from ui.pages.base_page import BasePage
from ui.locators.registration_page_locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()
    url = 'https://ads.vk.com/hq/registration'

    def click_create_new_cabinet_button(self):
        self.click(self.locators.CREATE_NEW_CABINET_BUTTON)

    def get_selected_language(self) -> str:
        return self.find(self.locators.SELECTED_LANGUAGE).text

    def select_language(self, language: str):
        self.click(self.locators.LANGUAGE_BUTTON(language))

    def select_country(self, country_name: str):
        self.click(self.locators.COUNTRY_DROPDOWN)
        self.click(self.locators.COUNTRY_DROPDOWN_ITEM(country_name))

    def currency_dropdown_contain_items(self, item_names: list):
        self.click(self.locators.CURRENCY_DROPDOWN)
        for item_name in item_names:
            item = self.find(self.locators.CURRENCY_DROPDOWN_ITEM(item_name))
            if item is None:
                return False

            return True

    def click_submit_button(self):
        self.scroll_and_click(self.locators.SUBMIT_BUTTON)

    def get_email_error(self) -> str:
        return self.find(self.locators.EMAIL_ERROR).text

    def get_inn_error(self) -> str:
        return self.find(self.locators.INN_ERROR).text

    def get_offer_error(self) -> str:
        return self.find(self.locators.OFFER_ERROR).text

    def click_offer_checkbox(self):
        self.scroll_and_click(self.locators.OFFER_CHECKBOX)

    def enter_email(self, email: str):
        elem = self.find(self.locators.EMAIL_INPUT)
        elem.clear()
        elem.send_keys(email)

    def enter_inn(self, inn: str):
        elem = self.find(self.locators.INN_INPUT)
        elem.clear()
        elem.send_keys(inn)

    def select_account_type(self, account_type: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_BUTTON(account_type))

    def physical_type_became_invisible(self) -> bool:
        return self.became_invisible(self.locators.ACCOUNT_TYPE_BUTTON('Физическое лицо'))

    def physical_type_became_visible(self) -> bool:
        return self.became_visible(self.locators.ACCOUNT_TYPE_BUTTON('Физическое лицо'))

from ui.pages.base_page import BasePage
from ui.locators.partner_page_locators import PartnerPageLocators


class PartnerPage(BasePage):
    locators = PartnerPageLocators()
    url = 'https://ads.vk.com/partner'

    def click_cabinet_button(self):
        self.click(self.locators.CABINET_BUTTON)

    def click_help_button(self):
        self.click(self.locators.HELP_BUTTON)

    def click_format_tab(self, tab_name):
        self.scroll_and_click(self.locators.FORMAT_TAB(tab_name))

    def page_contain_formats(self, item_names):
        for item_name in item_names:
            item = self.find(self.locators.FORMAT_ITEM_TITLE(item_name))
            if item is None:
                return False

        return True

    def submit_button_is_disabled(self):
        if self.find(self.locators.SUBMIT_BUTTON).get_attribute("disabled") is not None:
            return True
        return False

    def enter_name_and_email(self, name, email):
        elem = self.find(self.locators.NAME_INPUT)
        elem.clear()
        elem.send_keys(name)
        elem = self.find(self.locators.EMAIL_INPUT)
        elem.clear()
        elem.send_keys(email)

    def click_submit_button(self):
        self.scroll_and_click(self.locators.SUBMIT_BUTTON)

    def submit_message_is_on_page(self):
        if self.find(self.locators.SUBMIT_MESSAGE) is not None:
            return True
        return False

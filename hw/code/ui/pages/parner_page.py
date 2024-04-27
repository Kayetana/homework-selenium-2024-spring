from ui.pages.base_page import BasePage
from ui.locators.partner_page_locators import PartnerPageLocators


class PartnerPage(BasePage):
    locators = PartnerPageLocators()
    url = 'https://ads.vk.com/partner'

    def check_if_button_is_disabled(self):
        return self.find(self.locators.SUBMIT_BUTTON).get_attribute("disabled")

    def find_submit_message(self):
        return self.find(self.locators.SUBMIT_MESSAGE)


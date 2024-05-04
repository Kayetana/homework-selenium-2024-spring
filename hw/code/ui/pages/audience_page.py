import time
from ui.pages.base_page import BasePage
from ui.locators.audience_page_locators import AudiencePageLocators


class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    def click_create_audience(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON)

    def get_default_audience_name(self):
        return self.find(self.locators.AUDIENCE_NAME_INPUT).get_attribute('value')

    def enter_audience_name(self, audience_name):
        elem = self.find(self.locators.AUDIENCE_NAME_INPUT)
        elem.clear()
        elem.send_keys(audience_name)

    def get_error(self):
        return self.find(self.locators.ERROR).text

    def add_source_by_key_phrases(self, key_phrases):
        self.click(self.locators.ADD_SOURCE_BUTTON)
        self.click(self.locators.SOURCE_ITEM('Ключевые фразы'))

        elem = self.find(self.locators.KEY_PHRASES_INPUT)
        elem.clear()
        elem.send_keys(key_phrases)

        self.click(self.locators.AUDIENCE_PANEL_SUBMIT_BUTTON)

    def submit_audience(self):
        self.click(self.locators.AUDIENCE_PANEL_SUBMIT_BUTTON)

    def get_created_audience_title(self):
        return self.find(self.locators.CREATED_AUDIENCE_TITLE).text

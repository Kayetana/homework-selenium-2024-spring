from selenium.common import TimeoutException
from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.audience_page_locators import AudiencePageLocators
from datetime import datetime


class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    DEFAULT_AUDIENCE_NAME = 'Аудитория ' + datetime.now().strftime('%Y-%m-%d')
    ERROR_TOO_LONG_AUDIENCE_NAME = 'Максимальная длина 255 символов'
    MAX_LENGTH_OF_AUDIENCE_NAME = 255

    def click_create_audience_button(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON)

    def get_default_audience_name(self):
        return self.find(self.locators.AUDIENCE_NAME_INPUT).get_attribute('value')

    def enter_audience_name(self, audience_name: str):
        elem = self.find(self.locators.AUDIENCE_NAME_INPUT)
        elem.clear()
        elem.send_keys(audience_name)
        elem.send_keys(Keys.ENTER)

    def get_error(self) -> str:
        return self.find(self.locators.ERROR).text

    def click_add_source_button(self):
        self.click(self.locators.ADD_SOURCE_BUTTON)

    def select_source(self, source_name):
        self.click(self.locators.SOURCE_ITEM(source_name))

    def enter_key_phrases(self, key_phrases: list):
        key_phrases_input = self.find(self.locators.KEY_PHRASES_INPUT)
        key_phrases_input.clear()
        key_phrases_input.send_keys(' '.join(key_phrases))

    def click_modal_page_submit_button(self):
        try:
            self.click(self.locators.MODAL_PAGE_SUBMIT_BUTTON)
        except TimeoutException:
            pass

    def get_source_card_content(self) -> str:
        return self.find(self.locators.SOURCE_CARD_CONTENT).text

    def get_created_audience_title(self) -> str:
        return self.find(self.locators.CREATED_AUDIENCE_TITLE).text

    def delete_audience(self):
        self.hover(self.locators.AUDIENCE_OPTIONS_BUTTON)
        self.click(self.locators.AUDIENCE_DELETE_BUTTON)
        self.click(self.locators.AUDIENCE_CONFIRM_DELETE_BUTTON)

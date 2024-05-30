from ui.pages.base_page import BasePage
from ui.locators.audience_page_locators import AudiencePageLocators
from datetime import datetime
from selenium.webdriver.support import expected_conditions as ec


class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    DEFAULT_AUDIENCE_NAME = 'Аудитория ' + datetime.now().strftime('%Y-%m-%d')
    ERROR_TOO_LONG_AUDIENCE_NAME = 'Максимальная длина 255 символов'
    MAX_LENGTH_OF_AUDIENCE_NAME = 255

    def click_create_audience_button(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON)

    def enter_audience_name(self, audience_name: str):
        elem = self.find(self.locators.AUDIENCE_NAME_INPUT)
        elem.clear()
        elem.send_keys(audience_name)

    def get_error(self) -> str:
        return self.find(self.locators.ERROR).text

    def add_key_phrases_source(self, source_title: str, key_phrases: list, negative_phrases: list, search_period: int):
        self.click(self.locators.ADD_SOURCE_BUTTON)
        self.click(self.locators.SOURCE_ITEM('Ключевые фразы'))

        source_title_input = self.find(self.locators.SOURCE_TITLE_INPUT)
        source_title_input.clear()
        source_title_input.send_keys(source_title)

        key_phrases_input = self.find(self.locators.KEY_PHRASES_INPUT)
        key_phrases_input.clear()
        key_phrases_input.send_keys(' '.join(key_phrases))

        negative_phrases_input = self.find(self.locators.NEGATIVE_PHRASES_INPUT)
        negative_phrases_input.clear()
        negative_phrases_input.send_keys(' '.join(negative_phrases))

        search_period_input = self.find(self.locators.SEARCH_PERIOD_INPUT)
        search_period_input.clear()
        search_period_input.send_keys(str(search_period))

        self.click_submit_source_button()

    def click_submit_source_button(self):
        self.scroll_and_click(self.locators.SUBMIT_SOURCE_BUTTON)

    def click_submit_audience_button(self):
        self.scroll_and_click(self.locators.SUBMIT_AUDIENCE_BUTTON)

    def get_source_title_on_card(self) -> str:
        return self.find(self.locators.SOURCE_TITLE_ON_CARD).text

    def get_key_phrases_on_card(self) -> list:
        key_phrases: str = self.find_multiple(self.locators.SOURCE_CONTENT_ON_CARD)[0].text
        return key_phrases.split()

    def get_negative_phrases_on_card(self) -> list:
        negative_phrases: str = self.find_multiple(self.locators.SOURCE_CONTENT_ON_CARD)[1].text
        return negative_phrases.split()

    def get_search_period_on_card(self) -> int:
        search_period: str = self.find_multiple(self.locators.SOURCE_CONTENT_ON_CARD)[2].text
        return int(search_period.split()[0])

    def get_created_audience_title(self) -> str:
        return self.find(self.locators.CREATED_AUDIENCE_TITLE).text

    def delete_audience(self):
        self.hover(self.locators.AUDIENCE_OPTIONS_BUTTON)
        self.click(self.locators.AUDIENCE_DELETE_BUTTON)
        self.click(self.locators.AUDIENCE_CONFIRM_DELETE_BUTTON)
        self.wait().until(ec.invisibility_of_element(self.locators.CREATED_AUDIENCE_TITLE))

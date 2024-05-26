import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from ui.pages.base_page import BasePage
from ui.locators.campaigns_page_locators import CampaignsPageLocators


class CampaignsPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard/ad_plans'
    locators = CampaignsPageLocators()

    MIN_BUDGET_AMOUNT = 100
    ERROR_EMPTY_FIELD = 'Обязательное поле'
    ERROR_TOO_SMALL_BUDGET_AMOUNT = 'Бюджет кампании должен быть не меньше 100₽'
    SECOND_STEP_NAME = 'Группы объявлений'
    THIRD_STEP_NAME = 'Объявления'

    def skip_help(self):
        try:
            self.click(self.locators.SKIP_HELP_BUTTON)
        except TimeoutException:
            pass

    def click_create_campaign_button(self):
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON)

    def select_site(self):
        self.click(self.locators.SITE_BUTTON)

    def get_error(self) -> str:
        return self.find(self.locators.ERROR).text

    def click_continue_button(self):
        self.scroll_and_click(self.locators.CONTINUE_BUTTON)

    def enter_site_url(self, url: str):
        elem = self.find(self.locators.SITE_INPUT)
        elem.clear()
        elem.send_keys(url)
        elem.send_keys(Keys.ENTER)

    def enter_budget_amount(self, amount: str):
        elem = self.find(self.locators.BUDGET_INPUT)
        elem.clear()
        elem.send_keys(amount)

    def fill_second_step(self, region: str, gender: str):
        region_input = self.find(self.locators.REGION_INPUT)
        region_input.clear()
        region_input.send_keys(region)
        self.click(self.locators.REGION_SEARCH_RESULTS)

        self.click(self.locators.SECTION_DEMOGRAPHY)
        self.click(self.locators.GENDER_BUTTON(gender))
        self.click(self.locators.DO_NOT_ADD_UTM_TAGS_BUTTON)

    def get_displayed_region(self) -> str:
        return self.find(self.locators.REGION_SELECTED_AND_DISPLAYED).text

    def enter_title_and_description(self, title: str, description: str):
        elem = self.find(self.locators.TITLE)
        elem.clear()
        elem.send_keys(title)

        elem = self.find(self.locators.DESCRIPTION)
        elem.clear()
        elem.send_keys(description)

    def fill_third_step(self, title: str, description: str, text_on_button: str, filepath: str):
        self.enter_title_and_description(title, description)
        self.click(self.locators.TEXT_ON_BUTTON_DROPDOWN)
        self.click(self.locators.TEXT_ON_BUTTON_ITEM(text_on_button))

        load_image_input = self.find(self.locators.LOAD_IMAGE_INPUT)
        time.sleep(3)
        load_image_input.send_keys(filepath)

    def get_preview_title(self) -> str:
        return self.find(self.locators.TITLE_ON_PREVIEW).text

    def get_preview_description(self) -> str:
        return self.find(self.locators.DESCRIPTION_ON_PREVIEW).text

    def is_button_displayed_on_preview(self, text_on_button: str) -> bool:
        return self.became_visible(self.locators.BUTTON_ON_PREVIEW(text_on_button))

    def is_video_displayed_on_preview(self) -> bool:
        return self.became_visible(self.locators.VIDEO_ON_PREVIEW, timeout=10)

    def is_images_group_displayed(self) -> bool:
        return self.became_visible(self.locators.IMAGES_GROUP)

    def click_publish_button(self):
        self.click(self.locators.PUBLISH_BUTTON)

    def confirm_publish(self):
        try:
            self.click(self.locators.CONFIRM_PUBLISH_BUTTON)
        except TimeoutException:
            pass

    def get_created_campaign_name(self) -> str:
        return self.find(self.locators.CAMPAIGN_ITEM).text

    def get_created_campaign_budget(self) -> int:
        budget = self.find(self.locators.CAMPAIGN_ITEM_BUDGET).text
        return int(''.join(symbol for symbol in budget if str.isdigit(symbol)))

    def delete_campaign(self):
        self.hover(self.locators.CAMPAIGN_ITEM)
        self.hover(self.locators.OPTIONS_ITEM)
        self.click(self.locators.DELETE_CAMPAIGN_BUTTON)

import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from ui.pages.base_page import BasePage
from ui.locators.campaigns_page_locators import CampaignsPageLocators


class CampaignsPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard/ad_plans'
    locators = CampaignsPageLocators()

    def skip_help(self):
        try:
            self.click(self.locators.SKIP_HELP_BUTTON)
        except TimeoutException:
            pass

    def click_create_campaign(self):
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON)

    def select_site(self):
        self.click(self.locators.SITE)

    def site_input_became_visible(self):
        return self.became_visible(self.locators.SITE_INPUT)

    def get_error(self):
        return self.find(self.locators.ERROR).text

    def click_continue_button(self):
        self.scroll_and_click(self.locators.CONTINUE_BUTTON)

    def enter_site_url(self, url):
        elem = self.find(self.locators.SITE_INPUT)
        elem.clear()
        elem.send_keys(url)
        elem.send_keys(Keys.ENTER)

    def options_became_visible(self):
        return (self.became_visible(self.locators.GOAL_DROPDOWN)
                and self.became_visible(self.locators.STRATEGY_DROPDOWN)
                and self.became_visible(self.locators.BUDGET_INPUT)
                and self.became_visible(self.locators.DATES))

    def get_start_date(self):
        return self.find(self.locators.START_DATE).get_attribute('value')

    def enter_budget_amount(self, amount):
        elem = self.find(self.locators.BUDGET_INPUT)
        elem.clear()
        elem.send_keys(amount)

    def is_active_step(self, step_name):
        try:
            self.find(self.locators.ACTIVE_STEP(step_name))
            return True
        except TimeoutException:
            return False

    def select_regions(self):
        self.click(self.locators.REGION_QUICK_SELECTION)

    def get_panel_title(self):
        return self.find(self.locators.PANEL_TITLE).text

    def click_media_button(self):
        self.click(self.locators.MEDIA_BUTTON)

    def select_image(self):
        self.click(self.locators.GENERATED_IMAGES_TAB)
        self.click(self.locators.IMAGE_ITEM)

    def is_image_selected(self):
        try:
            self.find(self.locators.SELECTED_IMAGE)
            return True
        except TimeoutException:
            return False

    def enter_title_and_description(self, title, description):
        elem = self.find(self.locators.TITLE)
        elem.clear()
        elem.send_keys(title)

        elem = self.find(self.locators.DESCRIPTION)
        elem.clear()
        elem.send_keys(description)

    def click_publish_button(self):
        self.click(self.locators.PUBLISH_BUTTON)

import time
from ui.pages.base_page import BasePage
from ui.locators.hq_page_locators import HqPageLocators


class HqPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = HqPageLocators()

    def click_left_menu(self, item_name):
        self.click(self.locators.LEFT_MENU_ITEM(item_name))

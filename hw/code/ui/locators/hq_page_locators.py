from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class HqPageLocators(BasePageLocators):
    @staticmethod
    def LEFT_MENU_ITEM(item_name):
        return By.XPATH, f"//*[@data-testid='left-menu']//span[text()='{item_name}']"

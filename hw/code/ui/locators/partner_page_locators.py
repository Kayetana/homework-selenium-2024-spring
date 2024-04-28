from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class PartnerPageLocators(BasePageLocators):
    CABINET_BUTTON = (By.XPATH, "//*[contains(@class, 'PartnerContent_headerButton__')]")
    HELP_BUTTON = (By.XPATH, "//*[contains(@class, 'PartnerContent_headerButtonSecondary__')]")

    @staticmethod
    def FORMAT_TAB(tab_name):
        return By.XPATH, f"//*[contains(@class, 'Tabs_tab__') and text()='{tab_name}']"

    @staticmethod
    def FORMAT_ITEM_TITLE(item_name):
        return By.XPATH, f"//*[contains(@class, 'Slider_title__') and text()='{item_name}']"

    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'Form_button__')]")
    SUBMIT_MESSAGE = (By.XPATH, "//*[contains(@class, 'Form_success__')]")

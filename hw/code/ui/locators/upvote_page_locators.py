from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class UpvotePageLocators(BasePageLocators):
    COMMENT_BUTTON = (By.XPATH, "//*[contains(@class, 'ButtonComment_button__')]")
    COMMENT_ITEM = (By.XPATH, "//*[contains(@class, 'Comment_cell__')]")

    COMMENT_COUNTER = (
        By.XPATH,
        "//*[contains(@class, 'ButtonComment_button__')]//span[contains(@class, 'vkuiButton__content')]"
    )

    SEARCH_FIELD = (By.XPATH, "//*[contains(@class, 'vkuiSearch__input')]")

    IDEA_TITLE = (By.XPATH, "//*[contains(@class, 'Idea_title__')]")
    IDEA_DATE_AND_ID = (By.XPATH, "//*[contains(@class, 'vkuiSimpleCell__text')]")
    IDEA_THEME = (By.XPATH, "//*[contains(@class, 'Tag_tag__')]")
    IDEA_STATUS = (By.XPATH, "//*[contains(@class, 'Status_wrap__')]")

    CANCEL_FILTER_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiIcon--cancel')]")

    @staticmethod
    def SELECTED_FILTER(filter_name):
        return By.XPATH, f"//*[contains(@class, 'vkuiSelect__title') and text()='{filter_name}']"

    @staticmethod
    def FILTER_OPTION(option_name):
        return By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption__') and text()='{option_name}']"


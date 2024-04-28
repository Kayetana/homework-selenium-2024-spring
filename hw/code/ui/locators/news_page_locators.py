from selenium.webdriver.common.by import By
from ui.locators.base_sections_page_locators import BaseSectionsPageLocators


class NewsPageLocators(BaseSectionsPageLocators):
    NEWS_ITEM = (By.XPATH, "//a[contains(@class, 'News_wrapper__')]")
    NEWS_TITLE = (By.XPATH, "//*[contains(@class, 'News_title__')]")
    NEWS_MORE_DETAILS_BUTTON = (By.XPATH, "//*[contains(@class, 'News_button__')]")

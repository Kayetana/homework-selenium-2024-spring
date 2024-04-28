from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class BaseSectionsPageLocators(BasePageLocators):
    PAGE_TITLE = (By.XPATH, "//*[@data-test-id='summary-title-ads']")

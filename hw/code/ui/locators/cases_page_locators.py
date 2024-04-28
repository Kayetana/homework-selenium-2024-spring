from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class CasesPageLocators(BasePageLocators):
    PAGE_TITLE = (By.XPATH, "//*[@data-test-id='summary-title-ads']")
    CASE_ITEM = (By.XPATH, "//a[contains(@class, 'Case_wrapper__')]")
    CASE_TITLE = (By.XPATH, "//*[contains(@class, 'Case_title__')]")
    CASE_MORE_DETAILS_BUTTON = (By.XPATH, "//*[contains(@class, 'Case_button__')]")

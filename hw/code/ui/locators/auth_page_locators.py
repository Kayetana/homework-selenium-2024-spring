from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class AuthPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")
    CONTINUE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content')]")
    ALERT = (By.LINK_TEXT, 'Account not found')

    MAIL_RU_AUTH_BUTTON = (By.XPATH, "//*[@data-test-id='oAuthService_mail_ru']")
    MAIL_RU_LOGIN = (By.NAME, 'username')
    MAIL_RU_PASSWORD = (By.NAME, "password")
    MAIL_RU_NEXT_BUTTON = (By.XPATH, "//*[@data-test-id='next-button']")
    MAIL_RU_SUBMIT_BUTTON = (By.XPATH, "//*[@data-test-id='submit-button']")

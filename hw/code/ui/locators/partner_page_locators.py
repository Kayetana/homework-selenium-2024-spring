from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class PartnerPageLocators(BasePageLocators):
    CABINET_BUTTON = (By.LINK_TEXT, "Перейти в кабинет")
    HELP = (By.LINK_TEXT, "Справка")

    FOR_APPS_TAB = (By.LINK_TEXT, 'Для приложений')
    FOR_WEBSITES_TAB = (By.LINK_TEXT, 'Для сайтов')

    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'Form_button__')]")
    SUBMIT_MESSAGE = (By.XPATH, "//*[contains(@class, 'Form_success__')]")


from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class CabinetPageLocators(BasePageLocators):
    CLOSE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiModalDismissButton')]")

    @staticmethod
    def LEFT_MENU_ITEM(item_name):
        return By.XPATH, f"//*[@data-testid='left-menu']//span[text()='{item_name}']"

    BALANCE_BUTTON = (By.XPATH, "//*[contains(@class, 'balance_balance__')]")
    REPLENISHMENT_MODAL_PAGE = (By.XPATH, "//*[contains(@class, 'vkuiModalPage__')]//h3[text()='Пополнение счёта']")

    NOTIFICATIONS_BUTTON = (By.XPATH, "//*[contains(@class, 'BellNotifications_buttonWrapper__')]")
    NOTIFICATIONS_MODAL_PAGE = (By.XPATH, "//*[contains(@class, 'BellNotificationsContent_card__')]")

    USER_AVATAR = (By.XPATH, "//*[contains(@class, 'userMenu_avatar__')]")

    LOGOUT_BUTTON = (By.XPATH, "//*[contains(@class, 'userMenu_logoutButton__')]")

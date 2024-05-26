from selenium.common import TimeoutException

from ui.pages.base_page import BasePage
from ui.locators.cabinet_page_locators import CabinetPageLocators


class CabinetPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = CabinetPageLocators()

    def skip_education(self):
        try:
            self.click(self.locators.CLOSE_BUTTON)
        except TimeoutException:
            pass

    def click_balance_button(self):
        self.click(self.locators.BALANCE_BUTTON)

    def replenishment_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.REPLENISHMENT_MODAL_PAGE)

    def click_notifications_button(self):
        self.click(self.locators.NOTIFICATIONS_BUTTON)

    def notifications_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.NOTIFICATIONS_MODAL_PAGE)

    def logout(self):
        self.click(self.locators.USER_AVATAR)
        self.click(self.locators.LOGOUT_BUTTON)

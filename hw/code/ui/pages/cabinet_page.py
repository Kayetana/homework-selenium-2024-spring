from selenium.common import TimeoutException

from ui.pages.base_page import BasePage
from ui.locators.cabinet_page_locators import CabinetPageLocators
from ui.locators.budget_page_locators import BudgetPageLocators


class CabinetPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = CabinetPageLocators()
    budget_locators = BudgetPageLocators()

    def click_close_button_if_education_is_offered(self):
        try:
            self.click(self.locators.CLOSE_BUTTON)
        except TimeoutException:
            pass

    def click_left_menu(self, item_name):
        self.click(self.locators.LEFT_MENU_ITEM(item_name))

    def click_balance_button(self):
        self.click(self.locators.BALANCE_BUTTON)

    def replenishment_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.budget_locators.REPLENISHMENT_MODAL_PAGE)

    def click_notifications_button(self):
        self.click(self.locators.NOTIFICATIONS_BUTTON)

    def notifications_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.NOTIFICATIONS_MODAL_PAGE)

    def click_user_avatar(self):
        self.click(self.locators.USER_AVATAR)

    def user_menu_became_visible(self) -> bool:
        return self.became_visible(self.locators.USER_MENU)

    def click_logout_button(self):
        self.click(self.locators.LOGOUT_BUTTON)

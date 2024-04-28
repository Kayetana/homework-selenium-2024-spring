import time

from ui.pages.base_page import BasePage
from ui.locators.auth_page_locators import AuthPageLocators


class AuthPage(BasePage):
    locators = AuthPageLocators()
    url = 'https://ads.vk.com/hq/registration'

    def login_mail_ru(self, login, password):
        self.click(self.locators.MAIL_RU_AUTH_BUTTON)

        elem = self.find(self.locators.MAIL_RU_LOGIN)
        elem.send_keys(login)
        self.click(self.locators.MAIL_RU_NEXT_BUTTON)

        elem = self.find(self.locators.MAIL_RU_PASSWORD)
        elem.send_keys(password)
        self.click(self.locators.MAIL_RU_SUBMIT_BUTTON)

from ui.pages.base_page import BasePage
from ui.locators.cases_page_locators import CasesPageLocators


class CasesPage(BasePage):
    locators = CasesPageLocators()
    url = 'https://ads.vk.com/cases'

    def get_page_title(self):
        return self.find(self.locators.PAGE_TITLE).text

    def get_case_title(self):
        return self.find(self.locators.CASE_TITLE).text

    def click_case_item(self):
        self.click(self.locators.CASE_ITEM)

    def click_more_details_button(self):
        self.click(self.locators.CASE_MORE_DETAILS_BUTTON)

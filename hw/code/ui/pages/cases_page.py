from ui.pages.base_sections_page import BaseSectionsPage
from ui.locators.cases_page_locators import CasesPageLocators


class CasesPage(BaseSectionsPage):
    locators = CasesPageLocators()
    url = 'https://ads.vk.com/cases'

    def get_case_title(self):
        return self.find(self.locators.CASE_TITLE).text

    def click_case_item(self):
        self.click(self.locators.CASE_ITEM)

    def click_more_details_button(self):
        self.click(self.locators.CASE_MORE_DETAILS_BUTTON)

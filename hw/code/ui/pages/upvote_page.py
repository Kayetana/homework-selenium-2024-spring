from ui.pages.base_page import BasePage
from ui.locators.upvote_page_locators import UpvotePageLocators
from selenium.webdriver.common.keys import Keys


class UpvotePage(BasePage):
    locators = UpvotePageLocators()
    url = 'https://ads.vk.com/upvote'

    def click_comment_button(self):
        self.click(self.locators.COMMENT_BUTTON)

    def comments_is_on_page(self):
        if self.find(self.locators.COMMENT_ITEM) is not None:
            return True
        return False

    def get_comment_counter_from_button(self):
        return int(self.find(self.locators.COMMENT_COUNTER).text)

    def count_comment_items(self):
        return len(self.find_multiple(self.locators.COMMENT_ITEM))

    def perform_search(self, text):
        search_field = self.find(self.locators.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)

    def get_first_idea_title(self):
        return self.find(self.locators.IDEA_TITLE).text

    def get_first_idea_id(self):
        date_and_id = self.find(self.locators.IDEA_DATE_AND_ID).text.split()
        return date_and_id[len(date_and_id)-1]

    def get_first_idea_status(self):
        return self.find(self.locators.IDEA_STATUS).text

    def get_first_idea_theme(self):
        return self.find(self.locators.IDEA_THEME).text

    def click_cancel_filter_button(self):
        self.click(self.locators.CANCEL_FILTER_BUTTON)

    def open_filter_dropdown(self, filter_name):
        self.click(self.locators.SELECTED_FILTER(filter_name))

    def select_filter(self, option_name):
        self.click(self.locators.FILTER_OPTION(option_name))

    def filter_dropdown_contain_items(self, item_names):
        for item_name in item_names:
            item = self.find(self.locators.FILTER_OPTION(item_name))
            if item is None:
                return False

            return True

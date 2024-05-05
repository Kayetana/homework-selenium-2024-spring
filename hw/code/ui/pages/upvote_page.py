from ui.pages.base_page import BasePage
from ui.locators.upvote_page_locators import UpvotePageLocators
from selenium.webdriver.common.keys import Keys


class UpvotePage(BasePage):
    locators = UpvotePageLocators()
    url = 'https://ads.vk.com/upvote'

    THEMES = [
        'Лидформы',
        'Сообщества',
        'Форум идей',
        'Сайты',
        'Каталог товаров',
        'Мобильные приложения',
        'Другое'
    ]

    STATUSES = [
        'Голосование',
        'Уже в работе',
        'Реализована',
        'Отклонено'
    ]

    def click_add_idea_button(self):
        self.click(self.locators.ADD_IDEA)

    def upvote_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.UPVOTE_MODAL_PAGE)

    def click_comment_button(self):
        self.click(self.locators.COMMENT_BUTTON)

    def comments_became_visible(self) -> bool:
        return self.became_visible(self.locators.COMMENT_ITEM)

    def get_comment_counter_from_button(self) -> int:
        return int(self.find(self.locators.COMMENT_COUNTER).text)

    def count_comment_items(self) -> int:
        return len(self.find_multiple(self.locators.COMMENT_ITEM))

    def perform_search(self, text: str):
        search_field = self.find(self.locators.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)

    def get_first_idea_title(self) -> str:
        return self.find(self.locators.IDEA_TITLE).text

    def get_first_idea_id(self) -> str:
        date_and_id = self.find(self.locators.IDEA_DATE_AND_ID).text.split()
        return date_and_id[len(date_and_id)-1]

    def get_first_idea_status(self) -> str:
        return self.find(self.locators.IDEA_STATUS).text

    def get_first_idea_theme(self) -> str:
        return self.find(self.locators.IDEA_THEME).text

    def click_cancel_filter_button(self):
        self.click(self.locators.CANCEL_FILTER_BUTTON)

    def open_filter_dropdown(self, filter_name: str):
        self.click(self.locators.SELECTED_FILTER(filter_name))

    def select_filter(self, option_name: str):
        self.click(self.locators.FILTER_OPTION(option_name))

    def filter_dropdown_contain_items(self, item_names: list) -> bool:
        for item_name in item_names:
            item = self.find(self.locators.FILTER_OPTION(item_name))
            if item is None:
                return False

            return True

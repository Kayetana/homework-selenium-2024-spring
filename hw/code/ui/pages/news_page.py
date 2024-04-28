from ui.pages.base_page import BasePage
from ui.locators.news_page_locators import NewsPageLocators


class NewsPage(BasePage):
    locators = NewsPageLocators()
    url = 'https://ads.vk.com/news'

    def get_page_title(self):
        return self.find(self.locators.PAGE_TITLE).text

    def get_news_title(self):
        return self.find(self.locators.NEWS_TITLE).text

    def click_news_item(self):
        self.click(self.locators.NEWS_ITEM)

    def click_more_details_button(self):
        self.click(self.locators.NEWS_MORE_DETAILS_BUTTON)

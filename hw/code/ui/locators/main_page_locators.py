from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class MainPageLocators(BasePageLocators):
    VK_ADS_LOGO = (By.XPATH, "//*[contains(@class, 'HeaderLeft_home__')]")

    VK_BUSINESS_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Footer_controls__')]/a[contains(@href, 'https://vk.company/ru/company/business/')]"
    )

    NAV_CABINET_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'NavigationVKAds_right__')]/a[contains(@class, 'ButtonCabinet_primary__')]"
    )

    FOOTER_CABINET_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'Footer_leftContent__')]/a[contains(@class, 'ButtonCabinet_primary__')]"
    )

    @staticmethod
    def NAV_ITEM(item_name):
        return By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_') and text()='{item_name}']"

    @staticmethod
    def NAV_EDUCATION_DROPDOWN_ITEM(item_name):
        return By.XPATH, f"//*[contains(@class, 'SubNavigationItem_title__') and text()='{item_name}']"

    @staticmethod
    def FOOTER_ITEM(item_name):
        return By.XPATH, f"//*[contains(@class, 'Footer_item__')]/a[text()='{item_name}']"

    FOOTER_LANGUAGE_DROPDOWN = (By.XPATH, "//*[contains(@class, 'SelectLanguage_desktopSelect__')]")
    FOOTER_SELECTED_LANGUAGE = (By.XPATH, "//*[contains(@class, 'SelectLanguage_desktopSelect__')]/span")

    @staticmethod
    def FOOTER_LANGUAGE_DROPDOWN_ITEM(language):
        return By.XPATH, f"//*[contains(@class, 'SelectLanguage_selectElem__') and text()='{language}']"

    @staticmethod
    def FOOTER_SOCIAL_MEDIA_ITEM(url):
        return By.XPATH, f"//a[contains(@class, 'Footer_control__') and contains(@href, '{url}')]"

    FOOTER_ABOUT = (By.XPATH, "//*[contains(@class, 'Footer_about__')]")

    SLIDER_TITLE = (By.XPATH, "//*[contains(@class, 'MainSlider_active__')]//p")
    NONACTIVE_CIRCLE = (By.XPATH, "//*[contains(@class, 'Bullets_box__')]")

    @staticmethod
    def SLIDER_BUTTON(url):
        return By.XPATH, f"//a[contains(@class, 'MainSlider_button__') and contains(@href, '{url}')]"

    SEE_ALL_LINK = (By.XPATH, "//*[contains(@class, 'styles_all__')]")
    CASE_ITEM = (By.XPATH, "//*[contains(@class, 'Case_content__')]")
    CASE_ITEM_TITLE = (By.XPATH, "//*[contains(@class, 'Case_title__')]")

    WEBINAR_ITEM = (By.XPATH, "//*[contains(@class, 'GetStarted_wrapper__')]")
    WEBINAR_ITEM_BUTTON = (By.XPATH, "//*[contains(@class, 'GetStarted_button__')]")

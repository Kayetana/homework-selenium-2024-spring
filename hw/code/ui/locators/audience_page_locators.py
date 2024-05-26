from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class AudiencePageLocators(BasePageLocators):
    CREATE_AUDIENCE_BUTTON = (By.XPATH, "//button[@data-testid='create-audience']")

    AUDIENCE_NAME_INPUT = (By.XPATH, "//*[contains(@class, 'vkuiInput__el')]")
    ERROR = (By.XPATH, "//*[@role='alert']")

    ADD_SOURCE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить источник']")

    @staticmethod
    def SOURCE_ITEM(item_name):
        return By.XPATH, f"//*[contains(@class, 'SourceTypeSelector_button__')]//*[text()='{item_name}']"

    SOURCE_TITLE_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiInput') and preceding-sibling::h5[text()='Название']]/input"
    )

    KEY_PHRASES_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'KeyPhrases_') and preceding-sibling::h5//*[text()='Ключевые фразы']]//textarea"
    )

    NEGATIVE_PHRASES_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'KeyPhrases_') and preceding-sibling::h5//*[text()='Минус-фразы']]//textarea"
    )

    SEARCH_PERIOD_INPUT = (By.XPATH, "//*[contains(@class, 'ContextForm_daysInput__')]/input")

    SOURCE_TITLE_ON_CARD = (
        By.XPATH,
        "//*[contains(@class, 'SourceListItem_')]/*[contains(@class, 'Header_header__')]/h4"
    )

    SOURCE_CONTENT_ON_CARD = (
        By.XPATH,
        "//*[contains(@class, 'SourceListItem_')]//*[contains(@class, 'InfoRow_content__')]"
    )

    SUBMIT_SOURCE_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'ModalSidebarPage_container__')]//*[@data-testid='submit']"
    )

    SUBMIT_AUDIENCE_BUTTON = (
        By.XPATH,
        "//form[contains(@class, 'ModalSidebarPage_container__')]//*[@data-testid='submit']"
    )

    CREATED_AUDIENCE_TITLE = (By.XPATH, "//*[contains(@class, 'NameCell_wrapper__')]/h5")

    AUDIENCE_OPTIONS_BUTTON = (By.XPATH, "//*[contains(@class, 'NameCell_details__')]")

    AUDIENCE_DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiActionSheetItem__')]//*[text()='Удалить']")
    AUDIENCE_CONFIRM_DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'ModalConfirm_wrapper__')]//*[text()='Удалить']")

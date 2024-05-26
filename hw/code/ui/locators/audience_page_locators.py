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

    KEY_PHRASES_INPUT = (By.XPATH, "//*[contains(@class, 'KeyPhrases_textarea__')]/textarea")

    MODAL_PAGE_SUBMIT_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiTappable--hasActive') and @type='submit']")

    SOURCE_CARD_CONTENT = (
        By.XPATH,
        "//*[contains(@class, 'SourcesList_wrapper__')]//*[contains(@class, 'InfoRow_content__')]"
    )

    CREATED_AUDIENCE_TITLE = (By.XPATH, "//*[contains(@class, 'NameCell_wrapper__')]/h5")

    AUDIENCE_OPTIONS_BUTTON = (By.XPATH, "//*[contains(@class, 'NameCell_details__')]")

    AUDIENCE_DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiActionSheetItem__')]//*[text()='Удалить']")
    AUDIENCE_CONFIRM_DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'ModalConfirm_wrapper__')]//*[text()='Удалить']")

from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class CampaignsPageLocators(BasePageLocators):
    # general
    SKIP_HELP_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Попробовать позже']")
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Создать']")
    CONTINUE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Продолжить']")
    PUBLISH_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Опубликовать']")
    CONFIRM_PUBLISH_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Отправить']")
    ERROR = (By.XPATH, "//*[@role='alert']/div")

    @staticmethod
    def ACTIVE_STEP(step_name):
        return By.XPATH, f"//*[contains(@class, 'Steps_step_active__') and child::span[text()='{step_name}']]"

    # first step
    CAMPAIGN_TITLE = (By.XPATH, "//*[contains(@class, 'EditableTitle_container__')]")
    CAMPAIGN_TITLE_TEXTAREA = (By.XPATH, "//textarea[contains(@class, 'EditableTitle_input__')]")

    SITE_BUTTON = (By.XPATH, "//*[@data-id='site_conversions']")
    SITE_INPUT = (By.XPATH, "//*[@placeholder='Введите ссылку на сайт']")

    GOAL_DROPDOWN = (By.XPATH, "//*[@data-testid='priced-goal']")
    STRATEGY_DROPDOWN = (By.XPATH, "//*[@data-testid='autobidding-mode']")
    BUDGET_INPUT = (By.XPATH, "//*[contains(@class, 'Budget_input__')]/input")

    DATES = (By.XPATH, "//*[contains(@class, 'Dates_layout__')]")
    START_DATE = (By.XPATH, "//*[contains(@class, 'Dates_datepickerStart__')]/input")

    # second step
    REGION_QUICK_SELECTION = (By.XPATH, "//*[contains(@class, 'RegionsQuickSelection_item__')]")
    REGION_INPUT = (By.XPATH, "//*[@data-testid='search']")
    REGION_SEARCH_RESULTS = (By.XPATH, "//*[contains(@class, 'Branch_branch__')]")
    REGION_SELECTED_AND_DISPLAYED = (By.XPATH, "//*[contains(@class, 'RegionsList_wrapper__')]//h4")

    SECTION_DEMOGRAPHY = (By.XPATH, "//*[@data-testid='section-demography']")

    @staticmethod
    def GENDER_BUTTON(gender):
        return By.XPATH, f"//*[contains(@class, 'vkuiRadio') and child::input[@value='{gender}']]"

    SECTION_DEVICES = (By.XPATH, "//*[@data-testid='section-devices']")
    DESKTOP_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiCheckbox__') and child::span[text()='Десктопные']]")

    DO_NOT_ADD_UTM_TAGS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiRadio__title')]//*[text()='Не добавлять UTM-метки']"
    )

    # third step
    TITLE = (By.XPATH, "//*[contains(@class, 'TextRole_textFieldWrap__')]//input")
    DESCRIPTION = (By.XPATH, "//*[contains(@class, 'TextRole_textFieldWrap__')]//textarea")
    TEXT_ON_BUTTON_DROPDOWN = (
        By.XPATH,
        "//*[contains(@class, 'vkuiCustomSelect') and preceding-sibling::h2/span[text()='Надпись на кнопке']]"
    )

    @staticmethod
    def TEXT_ON_BUTTON_ITEM(text):
        return By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption') and @title='{text}']"

    LOAD_IMAGE_INPUT = (By.XPATH, "//input[@type='file']")

    IMAGES_GROUP = (By.XPATH, "//*[contains(@class, 'MediaContentGroupItem_image__')]")

    # third step. preview
    TITLE_ON_PREVIEW = (By.XPATH, "//*[contains(@class, 'preview_preview__')]//h3[contains(@class, 'Header_name__')]")
    DESCRIPTION_ON_PREVIEW = (
        By.XPATH,
        "//*[contains(@class, 'preview_preview__')]//*[contains(@class, 'Default_text__')]"
    )
    VIDEO_ON_PREVIEW = (By.XPATH, "//*[contains(@class, 'VideoContainer_video__')]")

    @staticmethod
    def BUTTON_ON_PREVIEW(text):
        return By.XPATH, f"//*[contains(@class, 'Footer_button__') and text()='{text}']"

    # campaigns page

    CAMPAIGN_ITEM = (By.XPATH, "//button[contains(@class, 'nameCellContent_link__')]")
    OPTIONS_ITEM = (By.XPATH, "//*[@data-testid='actions']")

    CAMPAIGN_ITEM_BUDGET = (By.XPATH, "//*[contains(@class, 'budget_editable__')]")

    DELETE_CAMPAIGN_BUTTON = (By.XPATH, "//*[@data-testid='archive']")

from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class LeadFormsPageLocators(BasePageLocators):
    # general
    CREATE_LEADFORM_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__') and text()='Создать лид-форму']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__') and text()='Удалить']")
    STEP_COUNTER = (By.XPATH, "//*[contains(@class, 'CreateLeadFormModal_activeStep__')]/div")

    # leadform creating. first step. images
    LOAD_IMAGE_BUTTON = (By.XPATH, "//*[@data-testid='set-global-image']")
    LOAD_IMAGE_INPUT = (By.XPATH, "//input[@type='file']")
    UPLOADED_IMAGE_ITEM = (By.XPATH, "//*[contains(@class, 'ImageItems_imageItem__')]")
    UPLOADED_IMAGE_NAME = (By.XPATH, "//*[contains(@class, 'ImageItems_name__')]")

    CHANGE_IMAGE_BUTTON = (By.XPATH, "//button[@data-testid='change-image']")
    EDIT_IMAGES_BUTTON = (By.XPATH, "//button[@aria-label='Edit']")
    SELECT_ALL_IMAGES_BUTTON = (By.XPATH, "//*[contains(@class, 'EditControl_selection__')]//*[text()='Выбрать все']")

    DELETE_IMAGES_BUTTON = (By.XPATH, "//button[@data-testid='delete']")

    @staticmethod
    def GRADIENT_SELECT_BUTTON(gradient_number):
        return By.XPATH, f"//*[contains(@class, 'GradientSelector_round__') and @data-id='{gradient_number}']"

    # leadform creating. first step. inputs
    LEADFORM_NAME_INPUT = (By.XPATH, "//input[@placeholder='Название лид-формы']")
    COMPANY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Название компании']")
    LEADFORM_TITLE_INPUT = (By.XPATH, "//input[@placeholder='Текст заголовка']")
    LEADFORM_DESCRIPTION_INPUT = (By.XPATH, "//input[@placeholder='Краткое описание опроса']")

    # leadform creating. first step. preview items
    COMPANY_NAME_ON_PREVIEW = (By.XPATH, "//*[contains(@class, 'TopPart-module_companyTitle__')]")
    LEADFORM_TITLE_ON_PREVIEW = (By.XPATH, "//*[contains(@class, 'TopPart-module_appTitle__')]")
    LEADFORM_DESCRIPTION_ON_PREVIEW = (By.XPATH, "//*[contains(@class, 'TopPart-module_appDescription__')]")

    # leadform creating. second step
    ADD_QUESTION_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__') and text()='Добавить вопрос']")
    ADD_ANSWER_BUTTON = (By.XPATH, "//*[contains(@class, 'Question_addAnswerLine__')]/button")

    QUESTION_INPUTS = (
        By.XPATH,
        "//*[contains(@class, 'Question_questionContent__')]//textarea[@placeholder='Напишите вопрос']"
    )
    ANSWER_INPUT = (By.XPATH, "//*[contains(@class, 'Answer_answer__')]//input")

    ADD_CONTACTS_BUTTON = (By.XPATH, "//*[contains(@class, 'Questions_addContactFieldsBtn__')]")

    @staticmethod
    def CONTACT_INFO_TYPE(info_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiCheckbox__titleBefore') and text()='{info_type}']"

    ADD_CONTACT_INFO_TYPES_BUTTON = (By.XPATH, "//*[contains(@class, 'ModalManagerPage_footer__')]/button")

    # leadform creating. second step. preview items
    @staticmethod
    def CONTACT_INPUT_ON_PREVIEW(placeholder_name):
        return By.XPATH, f"//*[contains(@class, 'FormPanel')]//input[@placeholder='{placeholder_name}']"

    BLOCK_TITLES_ON_PREVIEW = (By.XPATH, "//*[contains(@class, 'OnePageContentBlock-module_title__')]")
    ANSWERS_ON_PREVIEW = (By.XPATH, "//*[contains(@class, 'vkuiRadio__title')]/span")

    # leadform creating. third step
    RESULT_TITLE_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormField') and preceding-sibling::h5[text()='Заголовок']]//input"
    )
    RESULT_DESCRIPTION_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormField') and preceding-sibling::h5[text()='Описание']]//input"
    )

    ADD_COMPANY_SITE_BUTTON = (By.XPATH, "//*[@data-testid='add-site-btn']")
    COMPANY_SITE_INPUT = (By.XPATH, "//*[@placeholder='Введите ссылку на сайт']//input")

    ADD_COMPANY_PHONE_BUTTON = (By.XPATH, "//*[@data-testid='add-phone-btn']")
    COMPANY_PHONE_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormField') and preceding-sibling::h5[text()='Телефон для заказа']]//input"
    )

    # leadform creating. third step. preview items
    RESULT_TITLE_ON_PREVIEW = (
        By.XPATH,
        "//*[contains(@class, 'Success-module_placeholder__')]/*[contains(@class, 'vkuiPlaceholder__header')]"
    )

    RESULT_DESCRIPTION_ON_PREVIEW = (
        By.XPATH,
        "//*[contains(@class, 'Success-module_placeholder__')]/*[contains(@class, 'vkuiPlaceholder__text')]"
    )

    SITE_BUTTON_ON_PREVIEW = (By.XPATH, "//*[contains(@class, 'vkuiButton__') and text()='Перейти на сайт']")
    CALL_BUTTON_ON_PREVIEW = (By.XPATH, "//*[contains(@class, 'vkuiButton__') and text()='Позвонить']")

    # leadform creating. fourth step
    SETTINGS_NOTIFICATIONS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'Settings_notificationsWrap__')]//*[contains(@class, 'vkuiTappable')]"
    )

    SETTINGS_NOTIFICATIONS_EMAIL_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'Settings_notificationsWrap__')]//input[contains(@class, 'vkuiInput__el')]"
    )

    SETTINGS_FULL_NAME_INPUT = (
        By.XPATH,
        "//input[contains(@class, 'vkuiInput__el') and @placeholder='Введите фамилию, имя и отчество']"
    )

    SETTINGS_ADDRESS_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiInput__el') and @placeholder='Введите адрес']")
    SETTINGS_EMAIL_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiInput__el') and @placeholder='Введите email']")
    SETTINGS_INN_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiInput__el') and @placeholder='Введите ИНН']")

    # leadforms page
    LEADFORM_ITEM = (By.XPATH, "//*[contains(@class, 'NameCell_wrapper__')]/button")
    DELETE_LEADFORM_BUTTON = (By.XPATH, "//button[contains(@class, 'Nav_item__') and child::*[text()='Удалить']]")

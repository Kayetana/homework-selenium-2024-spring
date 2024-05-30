from ui.pages.base_page import BasePage
from ui.locators.leadforms_page_locators import LeadFormsPageLocators
from selenium.webdriver.support import expected_conditions as ec


class LeadFormsPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators = LeadFormsPageLocators()

    DEFAULT_ANSWERS_COUNT = 2
    CONTACT_INFO_TYPES_AND_PLACEHOLDERS = {
        'Фамилия': 'Введите фамилию',
        'Электронная почта': 'Введите email',
        'Возраст': 'Введите возраст'
    }

    def click_create_leadform_button(self):
        self.click(self.locators.CREATE_LEADFORM_BUTTON)

    def upload_image(self, filepath: str):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        load_image_input = self.find(self.locators.LOAD_IMAGE_INPUT)
        load_image_input.send_keys(filepath)

    def get_last_image_name_from_media_library(self) -> str:
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        return self.find(self.locators.UPLOADED_IMAGE_NAME).text

    def delete_all_from_media_library(self):
        self.click(self.locators.EDIT_IMAGES_BUTTON)
        self.click(self.locators.SELECT_ALL_IMAGES_BUTTON)
        self.click(self.locators.DELETE_IMAGES_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_BUTTON)

    def fill_first_step(self, leadform_name: str, filepath: str, company_name: str, leadform_title: str,
                        leadform_description: str, gradient_number: int):
        leadform_name_input = self.find(self.locators.LEADFORM_NAME_INPUT)
        leadform_name_input.clear()
        leadform_name_input.send_keys(leadform_name)

        self.upload_image(filepath)
        self.click(self.locators.UPLOADED_IMAGE_ITEM)

        company_name_input = self.find(self.locators.COMPANY_NAME_INPUT)
        company_name_input.clear()
        company_name_input.send_keys(company_name)

        leadform_title_input = self.find(self.locators.LEADFORM_TITLE_INPUT)
        leadform_title_input.clear()
        leadform_title_input.send_keys(leadform_title)

        leadform_description_input = self.find(self.locators.LEADFORM_DESCRIPTION_INPUT)
        leadform_description_input.clear()
        leadform_description_input.send_keys(leadform_description)

        self.click(self.locators.GRADIENT_SELECT_BUTTON(gradient_number))

    def get_company_name_on_preview(self) -> str:
        return self.find(self.locators.COMPANY_NAME_ON_PREVIEW).text

    def get_leadform_title_on_preview(self) -> str:
        return self.find(self.locators.LEADFORM_TITLE_ON_PREVIEW).text

    def get_leadform_description_on_preview(self) -> str:
        return self.find(self.locators.LEADFORM_DESCRIPTION_ON_PREVIEW).text

    def click_submit_button(self):
        self.click(self.locators.SUBMIT_BUTTON)

    def delete_uploaded_images(self):
        step_counter = int(self.find(self.locators.STEP_COUNTER).text)

        # return to first step
        for _ in range(step_counter - 1):
            self.click(self.locators.CANCEL_BUTTON)

        self.click(self.locators.CHANGE_IMAGE_BUTTON)
        self.delete_all_from_media_library()

    def add_questions_and_answers(self, questions_and_answers: dict):
        questions_counter = 0
        answers_counter = 0

        for question, answers in questions_and_answers.items():
            self.click(self.locators.ADD_QUESTION_BUTTON)
            question_input = self.find_multiple(self.locators.QUESTION_INPUTS)[questions_counter]
            question_input.clear()
            question_input.send_keys(question)
            questions_counter += 1

            if len(answers) > self.DEFAULT_ANSWERS_COUNT:
                additional_answer_input_count = len(answers)-self.DEFAULT_ANSWERS_COUNT

                for _ in range(additional_answer_input_count):
                    self.click(self.locators.ADD_ANSWER_BUTTON)

            for answer in answers:
                answer_input = self.find_multiple(self.locators.ANSWER_INPUT)[answers_counter]
                answer_input.clear()
                answer_input.send_keys(answer)
                answers_counter += 1

    def is_questions_and_answers_displayed_correct(self, questions_and_answers: dict) -> bool:
        questions_counter = 0
        answers_counter = 0
        questions_on_preview: list = self.find_multiple(self.locators.BLOCK_TITLES_ON_PREVIEW)[1:]
        answers_on_preview: list = self.find_multiple(self.locators.ANSWERS_ON_PREVIEW)

        for question, answers in questions_and_answers.items():
            if questions_on_preview[questions_counter].text != question:
                return False
            questions_counter += 1

            for answer in answers:
                if answers_on_preview[answers_counter].text != answer:
                    return False
                answers_counter += 1
        return True

    def add_contact_info_type(self, additional_contact_info_types: list):
        self.click(self.locators.ADD_CONTACTS_BUTTON)
        for info_type in additional_contact_info_types:
            self.click(self.locators.CONTACT_INFO_TYPE(info_type))
        self.click(self.locators.ADD_CONTACT_INFO_TYPES_BUTTON)

    def is_additional_contact_info_types_displayed(self, additional_contact_info_types: list) -> bool:
        for info_type in additional_contact_info_types:
            try:
                self.find(self.locators.CONTACT_INPUT_ON_PREVIEW(self.CONTACT_INFO_TYPES_AND_PLACEHOLDERS[info_type]))
            except TimeoutError:
                return False
        return True

    def fill_second_step(self, questions_and_answers: dict, additional_contact_info_types: list):
        self.add_questions_and_answers(questions_and_answers)
        self.add_contact_info_type(additional_contact_info_types)

    def fill_third_step(self, result_title: str, result_description: str, company_url: str, company_phone: str):
        result_title_input = self.find(self.locators.RESULT_TITLE_INPUT)
        result_title_input.clear()
        result_title_input.send_keys(result_title)

        result_description_input = self.find(self.locators.RESULT_DESCRIPTION_INPUT)
        result_description_input.clear()
        result_description_input.send_keys(result_description)

        self.click(self.locators.ADD_COMPANY_SITE_BUTTON)
        company_site_input = self.find(self.locators.COMPANY_SITE_INPUT)
        company_site_input.clear()
        company_site_input.send_keys(company_url)

        self.click(self.locators.ADD_COMPANY_PHONE_BUTTON)
        company_phone_input = self.find(self.locators.COMPANY_PHONE_INPUT)
        company_phone_input.clear()
        company_phone_input.send_keys(company_phone)

    def get_result_title_on_preview(self) -> str:
        return self.find(self.locators.RESULT_TITLE_ON_PREVIEW).text

    def get_result_description_on_preview(self) -> str:
        return self.find(self.locators.RESULT_DESCRIPTION_ON_PREVIEW).text

    def is_call_button_displayed_on_preview(self) -> bool:
        return self.became_visible(self.locators.CALL_BUTTON_ON_PREVIEW)

    def is_site_button_displayed_on_preview(self) -> bool:
        return self.became_visible(self.locators.SITE_BUTTON_ON_PREVIEW)

    def fill_fourth_step(self, notifications_email: str, full_name: str, address: str, email: str, inn: str):
        self.click(self.locators.SETTINGS_NOTIFICATIONS_BUTTON)
        notifications_email_input = self.find(self.locators.SETTINGS_NOTIFICATIONS_EMAIL_INPUT)
        notifications_email_input.clear()
        notifications_email_input.send_keys(notifications_email)

        full_name_input = self.find(self.locators.SETTINGS_FULL_NAME_INPUT)
        full_name_input.clear()
        full_name_input.send_keys(full_name)

        address_input = self.find(self.locators.SETTINGS_ADDRESS_INPUT)
        address_input.clear()
        address_input.send_keys(address)

        email_input = self.find(self.locators.SETTINGS_EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

        inn_input = self.find(self.locators.SETTINGS_INN_INPUT)
        inn_input.clear()
        inn_input.send_keys(inn)

    def get_created_leadform_name(self) -> str:
        return self.find(self.locators.LEADFORM_ITEM).text

    def delete_leadform(self):
        self.hover(self.locators.LEADFORM_ITEM)
        self.click(self.locators.DELETE_LEADFORM_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_BUTTON)

    def wait_until_leadform_deleted(self):
        self.wait().until(ec.invisibility_of_element(self.locators.LEADFORM_ITEM))

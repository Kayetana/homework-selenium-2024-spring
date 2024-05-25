import os
import pytest
from base_case import BaseCase

LEADFORM_NAME = 'Запись на тестовый урок'
FILEPATH = os.path.join(os.path.dirname(__file__), 'images/company_logo.jpg')
COMPANY_NAME = 'Easy English'
LEADFORM_TITLE = 'Проверь свой уровень английского'
LEADFORM_DESCRIPTION = 'Мы пришлем результат на почту'
GRADIENT_NUMBER = 5

QUESTIONS_AND_ANSWERS = {
    'Как переводится с английского слово Strawberry?': ['Клубника', 'Ежевика', 'Малина', 'Голубика'],
    'Как переводится с английского слово Bird?': ['птица', 'петь']
}

ADDITIONAL_CONTACT_INFO_TYPES = ['Электронная почта', 'Фамилия']

RESULT_TITLE = 'Тест пройден!'
RESULT_DESCRIPTION = 'В течение 15 минут вам на почту придет результат'
COMPANY_URL = 'https://easyenglish.best/'
COMPANY_PHONE = '+79999999999'

NOTIFICATIONS_EMAIL = 'notifications@easyenglish.ru'
FULL_NAME = 'Петров Петр'
ADDRESS = 'г.Москва, ул.Никитина, д.1, кв.600'
EMAIL = 'petrov@easyenglish.ru'
INN = '3663065397'


@pytest.fixture
def second_step(leadforms_page):
    leadforms_page.click_create_leadform_button()
    leadforms_page.fill_first_step(LEADFORM_NAME, FILEPATH, COMPANY_NAME, LEADFORM_TITLE,
                                   LEADFORM_DESCRIPTION, GRADIENT_NUMBER)
    leadforms_page.click_submit_button()


@pytest.fixture
def third_step(second_step, leadforms_page):
    leadforms_page.fill_second_step(QUESTIONS_AND_ANSWERS, ADDITIONAL_CONTACT_INFO_TYPES)
    leadforms_page.click_submit_button()


@pytest.fixture
def fourth_step(third_step, leadforms_page):
    leadforms_page.fill_third_step(RESULT_TITLE, RESULT_DESCRIPTION, COMPANY_URL, COMPANY_PHONE)
    leadforms_page.click_submit_button()


class TestLeadFormsPage(BaseCase):
    def test_upload_image(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.upload_image(FILEPATH)
        assert leadforms_page.get_last_image_name_from_media_library() == os.path.basename(FILEPATH)

        leadforms_page.delete_all_from_media_library()

    def test_fill_first_step(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.fill_first_step(LEADFORM_NAME, FILEPATH, COMPANY_NAME, LEADFORM_TITLE,
                                       LEADFORM_DESCRIPTION, GRADIENT_NUMBER)

        assert leadforms_page.get_company_name_on_preview() == COMPANY_NAME
        assert leadforms_page.get_leadform_title_on_preview() == LEADFORM_TITLE
        assert leadforms_page.get_leadform_description_on_preview() == LEADFORM_DESCRIPTION

        leadforms_page.delete_uploaded_images()

    def test_fill_second_step(self, second_step, leadforms_page):
        leadforms_page.fill_second_step(QUESTIONS_AND_ANSWERS, ADDITIONAL_CONTACT_INFO_TYPES)

        assert leadforms_page.is_questions_and_answers_displayed_correct(QUESTIONS_AND_ANSWERS)
        assert leadforms_page.is_additional_contact_info_types_displayed(ADDITIONAL_CONTACT_INFO_TYPES)

        leadforms_page.delete_uploaded_images()

    def test_fill_third_step(self, third_step, leadforms_page):
        leadforms_page.fill_third_step(RESULT_TITLE, RESULT_DESCRIPTION, COMPANY_URL, COMPANY_PHONE)

        assert leadforms_page.get_result_title_on_preview() == RESULT_TITLE
        assert leadforms_page.get_result_description_on_preview() == RESULT_DESCRIPTION
        assert leadforms_page.is_call_button_is_displayed_on_preview()
        assert leadforms_page.is_site_button_is_displayed_on_preview()

        leadforms_page.delete_uploaded_images()

    def test_create_leadform(self, fourth_step, leadforms_page):
        leadforms_page.fill_fourth_step(NOTIFICATIONS_EMAIL, FULL_NAME, ADDRESS, EMAIL, INN)
        leadforms_page.click_submit_button()
        assert leadforms_page.get_created_leadform_name() == LEADFORM_NAME

        leadforms_page.delete_leadform()

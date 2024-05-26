from datetime import datetime
import pytest
import os
from base_case import BaseCase

SITE_URL = 'go.dev'
TITLE = 'Go'
DESCRIPTION = 'Build simple, secure, scalable systems with Go'
TEXT_ON_BUTTON = 'Вступить'
BUDGET_AMOUNT = 10000
REGION = 'Владивосток'
AUDITORY_GENDER = 'female'
FILEPATH = os.path.join(os.path.dirname(__file__), 'images/gopher.png')


@pytest.fixture
def first_step(campaigns_page):
    campaigns_page.skip_help()
    campaigns_page.click_create_campaign_button()


@pytest.fixture
def second_step(first_step, campaigns_page):
    campaigns_page.select_site()
    campaigns_page.enter_site_url(SITE_URL)

    campaigns_page.enter_budget_amount(BUDGET_AMOUNT)
    campaigns_page.click_continue_button()


@pytest.fixture
def third_step(second_step, campaigns_page):
    campaigns_page.fill_second_step(REGION, AUDITORY_GENDER)
    campaigns_page.click_continue_button()


class TestCampaignsPage(BaseCase):

    def test_error_empty_budget(self, first_step, campaigns_page):
        campaigns_page.select_site()
        campaigns_page.enter_site_url(SITE_URL)

        campaigns_page.click_continue_button()
        assert campaigns_page.get_error() == campaigns_page.ERROR_EMPTY_FIELD

    def test_error_small_budget(self, first_step, campaigns_page):
        campaigns_page.select_site()
        campaigns_page.enter_site_url(SITE_URL)

        campaigns_page.enter_budget_amount(campaigns_page.MIN_BUDGET_AMOUNT - 1)
        campaigns_page.click_continue_button()
        assert campaigns_page.get_error() == campaigns_page.ERROR_TOO_SMALL_BUDGET_AMOUNT

    def test_fill_second_step(self, second_step, campaigns_page):
        campaigns_page.fill_second_step(REGION, AUDITORY_GENDER)
        assert campaigns_page.get_displayed_region() == REGION

    def test_fill_third_step(self, third_step, campaigns_page):
        campaigns_page.fill_third_step(TITLE, DESCRIPTION, TEXT_ON_BUTTON, FILEPATH)

        assert campaigns_page.get_preview_title() == TITLE
        assert campaigns_page.get_preview_description() == DESCRIPTION
        assert campaigns_page.is_button_displayed_on_preview(TEXT_ON_BUTTON)
        assert campaigns_page.is_images_group_displayed()
        assert campaigns_page.is_video_displayed_on_preview()

    def test_create_campaign(self, third_step, campaigns_page):
        campaigns_page.fill_third_step(TITLE, DESCRIPTION, TEXT_ON_BUTTON, FILEPATH)
        assert campaigns_page.is_video_displayed_on_preview()

        campaigns_page.click_publish_button()
        campaigns_page.confirm_publish()

        expected_campaign_name = 'Кампания ' + datetime.now().strftime('%Y-%m-%d')
        assert campaigns_page.get_created_campaign_name() == expected_campaign_name
        assert campaigns_page.get_created_campaign_budget() == BUDGET_AMOUNT

        campaigns_page.delete_campaign()

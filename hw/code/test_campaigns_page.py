from datetime import datetime
import pytest
from base_case import BaseCase

SITE_URL = 'go.dev'
BUDGET_AMOUNT = 1000
SMALL_BUDGET_AMOUNT = 99
TITLE = 'Go'
DESCRIPTION = 'Build simple, secure, scalable systems with Go'


@pytest.fixture
def new_campaign(campaigns_page):
    campaigns_page.skip_help()
    campaigns_page.click_create_campaign()


@pytest.fixture
def enter_site(new_campaign, campaigns_page):
    campaigns_page.select_site()
    campaigns_page.enter_site_url(SITE_URL)


@pytest.fixture
def first_step(enter_site, campaigns_page):
    campaigns_page.enter_budget_amount(BUDGET_AMOUNT)
    campaigns_page.click_continue_button()


@pytest.fixture
def second_step(first_step, campaigns_page):
    campaigns_page.select_regions()
    campaigns_page.click_continue_button()


class TestCampaignsPage(BaseCase):
    def test_go_to_new_campaign(self, new_campaign):
        assert self.is_opened('https://ads.vk.com/hq/new_create/ad_plan')

    def test_site_input_became_visible(self, new_campaign, campaigns_page):
        campaigns_page.select_site()
        assert campaigns_page.site_input_became_visible()

    def test_error_empty_site(self, new_campaign, campaigns_page):
        campaigns_page.select_site()
        campaigns_page.click_continue_button()
        assert campaigns_page.get_error() == 'Обязательное поле'

    def test_additional_options_became_visible(self, enter_site, campaigns_page):
        assert campaigns_page.options_became_visible()

    def test_start_date(self, enter_site, campaigns_page):
        assert campaigns_page.get_start_date() == datetime.now().strftime('%d.%m.%Y')

    def test_error_empty_budget(self, enter_site, campaigns_page):
        campaigns_page.click_continue_button()
        assert campaigns_page.get_error() == 'Обязательное поле'

    def test_error_small_budget(self, enter_site, campaigns_page):
        campaigns_page.enter_budget_amount(SMALL_BUDGET_AMOUNT)
        campaigns_page.click_continue_button()
        assert campaigns_page.get_error() == 'Бюджет кампании должен быть не меньше 100₽'

    def test_open_second_step(self, first_step, campaigns_page):
        assert campaigns_page.is_active_step('Группы объявлений')

    def test_open_third_step(self, second_step, campaigns_page):
        assert campaigns_page.is_active_step('Объявления')

    def test_open_media_panel(self, second_step, campaigns_page):
        campaigns_page.click_media_button()
        assert campaigns_page.get_panel_title() == 'Медиатека'

    def test_select_image(self, second_step, campaigns_page):
        campaigns_page.click_media_button()
        campaigns_page.select_image()
        assert campaigns_page.is_image_selected()

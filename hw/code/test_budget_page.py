import pytest
from base_case import BaseCase


@pytest.fixture
def replenishment_modal_page(budget_page):
    budget_page.click_replenish_budget_button()


class TestBudgetPage(BaseCase):
    def test_error_too_little_amount(self, replenishment_modal_page, budget_page):
        budget_page.enter_amount(budget_page.MIN_AMOUNT - 1)
        budget_page.click_submit_button()
        assert budget_page.get_error_message() == budget_page.ERROR_TOO_LITTLE_AMOUNT

    def test_error_too_little_amount_without_vat(self, replenishment_modal_page, budget_page):
        budget_page.enter_amount_without_vat(budget_page.MIN_AMOUNT_WITHOUT_VAT - 1)
        budget_page.click_submit_button()
        assert budget_page.get_error_message() == budget_page.ERROR_TOO_LITTLE_AMOUNT

    def test_error_too_large_amount(self, replenishment_modal_page, budget_page):
        budget_page.enter_amount(budget_page.MAX_AMOUNT + 1)
        budget_page.click_submit_button()
        assert budget_page.get_error_message() == budget_page.ERROR_TOO_LARGE_AMOUNT

    def test_error_too_large_amount_without_vat(self, replenishment_modal_page, budget_page):
        budget_page.enter_amount_without_vat(budget_page.MAX_AMOUNT_WITHOUT_VAT + 1)
        budget_page.click_submit_button()
        assert budget_page.get_error_message() == budget_page.ERROR_TOO_LARGE_AMOUNT

    def test_enter_non_numeric_amount(self, replenishment_modal_page, budget_page):
        budget_page.enter_amount('one two three !?#')
        assert budget_page.get_amount_value() == ''

    def test_enter_non_numeric_amount_without_vat(self, replenishment_modal_page, budget_page):
        budget_page.enter_amount_without_vat('hi :)')
        assert budget_page.get_amount_without_vat_value() == ''

    def test_vat_deduction(self, replenishment_modal_page, budget_page):
        budget_page.enter_amount(600)
        assert budget_page.get_amount_without_vat_value() == '500 ₽'

    def test_vat_addition(self, replenishment_modal_page, budget_page):
        budget_page.enter_amount_without_vat(800)
        assert budget_page.get_amount_value() == '960 ₽'

    def test_open_vkpay_iframe(self, replenishment_modal_page, budget_page):
        budget_page.enter_amount(budget_page.MIN_AMOUNT)
        budget_page.click_submit_button()
        assert budget_page.vkpay_iframe_became_visible()

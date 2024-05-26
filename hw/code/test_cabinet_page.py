from base_case import BaseCase


class TestCabinetPage(BaseCase):
    def test_replenishment_modal_page_became_visible(self, cabinet_page):
        cabinet_page.click_balance_button()
        assert cabinet_page.replenishment_modal_page_became_visible()

    def test_notifications_modal_page_became_visible(self, cabinet_page):
        cabinet_page.click_notifications_button()
        assert cabinet_page.notifications_modal_page_became_visible()

    def test_logout(self, cabinet_page):
        cabinet_page.logout()
        assert self.is_opened('https://ads.vk.com/')

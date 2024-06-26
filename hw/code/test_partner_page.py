from base_case import BaseCase


class TestPartnerPage(BaseCase):
    def test_go_to_auth(self, partner_page):
        partner_page.click_cabinet_button()
        partner_page.go_to_new_tab()
        assert self.is_opened('https://id.vk.com/auth')

    def test_go_to_help(self, partner_page):
        partner_page.click_help_button()
        partner_page.go_to_new_tab()
        assert self.is_opened('https://ads.vk.com/help')

    def test_formats(self, partner_page):
        partner_page.click_format_tab('Для приложений')
        assert partner_page.page_contain_formats(partner_page.APP_FORMATS)

        partner_page.click_format_tab('Для сайтов')
        assert partner_page.page_contain_formats(partner_page.WEBSITE_FORMATS)

    def test_submit_button_disabled_by_default(self, partner_page):
        assert partner_page.submit_button_is_disabled()

    def test_submit_button_enabled_after_filling_form(self, partner_page):
        partner_page.enter_name_and_email('test', 'test')
        assert not partner_page.submit_button_is_disabled()

    def test_submit_message_after_submitting_form(self, partner_page):
        partner_page.enter_name_and_email('test', 'test')
        partner_page.click_submit_button()
        assert partner_page.submit_message_became_visible()

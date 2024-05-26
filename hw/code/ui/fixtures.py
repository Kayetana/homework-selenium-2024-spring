import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.auth_page import AuthPage
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.news_page import NewsPage
from ui.pages.cases_page import CasesPage
from ui.pages.events_page import EventsPage
from ui.pages.upvote_page import UpvotePage
from ui.pages.partner_page import PartnerPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.cabinet_page import CabinetPage
from ui.pages.audience_page import AudiencePage
from ui.pages.campaigns_page import CampaignsPage
from ui.pages.budget_page import BudgetPage
from ui.pages.settings_page import SettingsPage
from ui.pages.leadforms_page import LeadFormsPage
import os
from dotenv import load_dotenv


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def news_page(driver):
    driver.get(NewsPage.url)
    return NewsPage(driver=driver)


@pytest.fixture
def cases_page(driver):
    driver.get(CasesPage.url)
    return CasesPage(driver=driver)


@pytest.fixture
def events_page(driver):
    driver.get(EventsPage.url)
    return EventsPage(driver=driver)


@pytest.fixture
def upvote_page(driver):
    driver.get(UpvotePage.url)
    return UpvotePage(driver=driver)


@pytest.fixture
def partner_page(driver):
    driver.get(PartnerPage.url)
    return PartnerPage(driver=driver)


@pytest.fixture(scope='session')
def credentials_without_cabinet():
    load_dotenv()
    return os.getenv('LOGIN_WITHOUT_CABINET'), os.getenv('PASSWORD_WITHOUT_CABINET')


@pytest.fixture(scope='session')
def credentials_with_cabinet():
    load_dotenv()
    return os.getenv('LOGIN'), os.getenv('PASSWORD')


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)


@pytest.fixture
def registration_page(driver, credentials_without_cabinet, auth_page):
    driver.get(RegistrationPage.url)
    auth_page.login(*credentials_without_cabinet)
    return RegistrationPage(driver=driver)


@pytest.fixture
def cabinet_page(driver, credentials_with_cabinet, auth_page):
    driver.get(RegistrationPage.url)
    auth_page.login(*credentials_with_cabinet)
    return CabinetPage(driver=driver)


@pytest.fixture
def campaigns_page(driver, cabinet_page):
    driver.get(CampaignsPage.url)
    return CampaignsPage(driver=driver)


@pytest.fixture
def audience_page(driver, cabinet_page):
    driver.get(AudiencePage.url)
    return AudiencePage(driver=driver)


@pytest.fixture
def budget_page(driver, cabinet_page):
    driver.get(BudgetPage.url)
    return BudgetPage(driver=driver)


@pytest.fixture
def settings_page(driver, cabinet_page):
    driver.get(SettingsPage.url)
    return SettingsPage(driver=driver)


@pytest.fixture
def leadforms_page(driver, cabinet_page):
    driver.get(LeadFormsPage.url)
    return LeadFormsPage(driver=driver)

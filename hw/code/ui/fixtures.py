import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.news_page import NewsPage
from ui.pages.cases_page import CasesPage
from ui.pages.events_page import EventsPage
from ui.pages.upvote_page import UpvotePage
from ui.pages.partner_page import PartnerPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.hq_page import HqPage
from ui.pages.audience_page import AudiencePage
from ui.pages.campaigns_page import CampaignsPage
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


@pytest.fixture
def registration_page(driver):
    driver.get(RegistrationPage.url)
    return RegistrationPage(driver=driver)


@pytest.fixture(scope='session')
def credentials():
    load_dotenv()
    return os.getenv('LOGIN'), os.getenv('PASSWORD')


@pytest.fixture
def registration_new_page(registration_page, credentials):
    registration_page.login(*credentials)
    registration_page.go_to_new_cabinet_registration()


@pytest.fixture
def hq_page(credentials, driver, registration_page):
    registration_page.login(*credentials)
    return HqPage(driver=driver)


@pytest.fixture
def campaigns_page(hq_page):
    hq_page.driver.get(CampaignsPage.url)
    return CampaignsPage(driver=hq_page.driver)


@pytest.fixture
def audience_page(hq_page):
    hq_page.driver.get(AudiencePage.url)
    return AudiencePage(driver=hq_page.driver)

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(slow_mo=100)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context(permissions=["geolocation"], geolocation={"latitude": 48.8, "longitude": 2.3})
    page = context.new_page()
    yield page
    page.close()
    context.close()
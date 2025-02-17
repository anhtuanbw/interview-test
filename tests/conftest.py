import pytest
from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # Set to True for headless mode
#         yield browser
#         browser.close()

# @pytest.fixture(scope="function")
# def page(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     page.close()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222") 
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def page(browser):
    default_context = browser.contexts[0]
    page = default_context.new_page()
    yield page
    page.close()

from playwright.sync_api import Page
from pages.base_page import BasePage

class MyAccountHomePage(BasePage):
    ACCOUNT_HEADING = "[data-automation='accountHeading']"
    ACCOUNT_SETTING_LINK_SELECTOR = "[data-automation='account-settings-link']"


    def __init__(self, page: Page):
        self.page = page
        self.account_heading = page.locator(self.ACCOUNT_HEADING)
        self.account_setting_link = page.locator(self.ACCOUNT_SETTING_LINK_SELECTOR)

    def navigate(self):
        self.page.goto(f"{self.BASE_URL}/account/home")

    def navigate_to_account_settings(self):
        self.account_setting_link.click()
        self.page.wait_for_load_state("networkidle")

    def is_my_account_page_showing(self):
        return self.account_heading.is_visible() and "account/home" in self.page.url
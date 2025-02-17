from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    ACCOUNT_BUTTON_SELECTOR = "button p >> text='Account'"
    MYACCOUNT_TEXT_SELECTOR = ".dropdown-top-holder a >> text='My Account'"
    SIGN_OUT_TEXT_SELECTOR = ".dropdown-top-holder a >> text='Sign Out'"


    def __init__(self, page: Page):
        self.page = page
        self.account_button = page.locator(self.ACCOUNT_BUTTON_SELECTOR)
        self.my_account_text = page.locator(self.MYACCOUNT_TEXT_SELECTOR)
        self.sign_out_text = page.locator(self.SIGN_OUT_TEXT_SELECTOR)

    def navigate(self, force_login=False):
        self.page.goto(f"{self.BASE_URL}")
        if force_login:
            # Check the account text on header and perform login actions
            pass # Placeholder for login actions
            
    def navigate_to_my_account(self):
        self.account_button.click()
        self.my_account_text.click()
        self.page.wait_for_load_state("networkidle")

    def sign_out_current_user(self):
        self.account_button.click()
        self.sign_out_text.click()
        self.page.wait_for_load_state("networkidle")

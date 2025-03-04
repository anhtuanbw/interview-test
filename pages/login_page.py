from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT_SELECTOR = ".login-container input#email"
    PASSWORD_INPUT_SELECTOR = ".login-container input#pass"
    SIGN_IN_BUTTON_SELECTOR = ".login-container button#send2"


    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator(self.USERNAME_INPUT_SELECTOR)
        self.password_input = page.locator(self.PASSWORD_INPUT_SELECTOR)
        self.sign_in_button = page.locator(self.SIGN_IN_BUTTON_SELECTOR)

    def enter_credentials(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_login(self):
        self.sign_in_button.click()

    def login(self, username, password):
        self.enter_credentials(username, password)
        self.click_login()
        self.page.wait_for_load_state("domcontentloaded")


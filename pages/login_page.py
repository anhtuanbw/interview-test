from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT_SELECTOR = "[id='username']"
    PASSWORD_INPUT_SELECTOR = "[id='password']"
    SIGN_IN_BUTTON_SELECTOR = "button >> text='Sign in'"


    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator(self.USERNAME_INPUT_SELECTOR)
        self.password_input = page.locator(self.PASSWORD_INPUT_SELECTOR)
        self.sign_in_button = page.locator(self.SIGN_IN_BUTTON_SELECTOR)

    def navigate(self):
        self.page.goto(f"{self.BASE_URL}/account/login?flow=home")

    def enter_credentials(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_login(self):
        self.sign_in_button.click()
        self.page.wait_for_load_state("networkidle")



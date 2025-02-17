from playwright.sync_api import Page
from pages.base_page import BasePage

class UpdatePasswordPage(BasePage):
    CURRENT_PASSWORD_INPUT_SELECTOR = "#accountSettingOldPasswordInput"
    NEW_PASSWORD_INPUT_SELECTOR = "#accountSettingNewPasswordInput"
    NOTIFICATION_MESSAGE_SELECTOR = "[data-automation='notification-strip-title']"
    UPDATE_BUTTON_SELECTOR = "span >> text='Save Changes'"


    def __init__(self, page: Page):
        self.page = page
        self.current_pwd_input = page.locator(self.CURRENT_PASSWORD_INPUT_SELECTOR)
        self.new_pwd_input = page.locator(self.NEW_PASSWORD_INPUT_SELECTOR)
        self.update_button = page.locator(self.UPDATE_BUTTON_SELECTOR)

    def navigate(self):
        self.page.goto(f"{self.BASE_URL}")
            
    def navigate_to_my_account(self):
        self.account_button.click()
        self.my_account_text.click()
        self.page.wait_for_load_state("networkidle")

    def input_current_password(self, current_password):
        self.current_pwd_input.fill(current_password)

    def input_new_password(self, new_password):
        self.new_pwd_input.fill(new_password)

    def click_save_changes(self):
        self.update_button.click()
        self.page.wait_for_load_state("networkidle")

    def get_notification_message(self):
        return self.notification_message.text_content()

from playwright.sync_api import Page
from pages.base_page import BasePage

class AccountSettingPage(BasePage):
    LAST_NAME_INPUT_SELECTOR = "#account-settings-last-name"
    MOBILE_INPUT_SELECTOR = "#mobile-phone"
    UPDATE_BUTTON_INPUT_SELECTOR = "#account-settings-update-btn"
    NOTIFICATION_MESSAGE_SELECTOR = "[data-automation='notification-strip-title']"
    UPDATE_PASSWORD_LINK = ".change-password"

    def __init__(self, page: Page):
        self.page = page
        self.last_name_input = page.locator(self.LAST_NAME_INPUT_SELECTOR)
        self.mobile_input = page.locator(self.MOBILE_INPUT_SELECTOR)
        self.update_button = page.locator(self.UPDATE_BUTTON_INPUT_SELECTOR)
        self.notification_message = page.locator(self.NOTIFICATION_MESSAGE_SELECTOR)
        self.update_password_link = page.locator(self.UPDATE_PASSWORD_LINK)


    def navigate(self):
        self.page.goto(f"{self.BASE_URL}/account/settings")

    def is_page_showing(self):
        return "account/settings" in self.page.url
    
    def input_last_name(self, last_name):
        # Clear text
        self.last_name_input.clear()
        self.last_name_input.fill(last_name)

    def input_mobile_number(self, mobile):
        self.mobile_input.clear()
        self.mobile_input.fill(mobile)

    def click_update(self):
        self.update_button.click()
        self.page.wait_for_load_state("networkidle")

    def get_notification_message(self):
        return self.notification_message.text_content()

    def get_current_mobile(self):
        return self.mobile_input.input_value()

    def get_current_last_name(self):
        return self.last_name_input.input_value()

    def click_update_password_link(self):
        self.update_password_link.click()
        self.page.wait_for_load_state("networkidle")

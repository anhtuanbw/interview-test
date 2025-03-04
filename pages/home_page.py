from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    SIGN_IN_TEXT_SELECTOR = ".page-header .authorization-link a >> text='Sign In'"
    CATEGORY_TEXT_SELECTOR = "a[role='menuitem'] span:visible >> text='%s'"
    CART_ICON_SELECTOR = ".page-header .showcart"
    CART_CHECKOUT_BUTTON_SELECTOR = "#top-cart-btn-checkout"

    def __init__(self, page: Page):
        self.page = page
        self.sign_in_text = page.locator(self.SIGN_IN_TEXT_SELECTOR)
        self.cart_icon = page.locator(self.CART_ICON_SELECTOR)
        self.cart_checkout_button = page.locator(self.CART_CHECKOUT_BUTTON_SELECTOR)

    def navigate(self, force_login=False):
        self.page.goto(f"{self.BASE_URL}")
        if force_login:
            # Check the account text on header and perform login actions
            pass # Placeholder for login actions
            
    def navigate_to_sign_in(self):
        self.sign_in_text.click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_product_category(self, category):
        categories = category.split("-")
        for cat in categories:
            cat = cat.strip()
            self.page.hover(self.CATEGORY_TEXT_SELECTOR % cat)
            self.page.wait_for_timeout(500)
        self.page.click(self.CATEGORY_TEXT_SELECTOR % categories[-1].strip(), force=True)
        self.page.wait_for_load_state("networkidle")

    def check_out_cart(self):
        self.cart_icon.click()
        self.cart_checkout_button.click()
        self.page.wait_for_load_state("networkidle")
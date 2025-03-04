from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductSearchPage(BasePage):
    PRODUCT_CONTAINER_SELECTOR = '.product-item-info'


    def __init__(self, page: Page):
        self.page = page
        self.products = self.page.locator(self.PRODUCT_CONTAINER_SELECTOR).all()

    def open_random_product(self):
        import random
        random.choice(self.products).click()
        self.page.wait_for_load_state("networkidle")
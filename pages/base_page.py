import os
from playwright.sync_api import Page

class BasePage:
    BASE_URL = os.getenv("BASE_URL", "https://magento.softwaretestingboard.com/")
    def __init__(self, page: Page):
        self.page = page

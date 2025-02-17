import os
from playwright.sync_api import Page

class BasePage:
    BASE_URL = os.getenv("BASE_URL", "https://www.myer.com.au")
    def __init__(self, page: Page):
        self.page = page

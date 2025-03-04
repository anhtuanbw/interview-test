from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductDetailPage(BasePage):
    SIZE_ICON_SELECTOR = '//div[span[text()="Size"]]//div[contains(@class, "swatch-option")]'
    COLOR_ICON_SELECTOR = '//div[span[text()="Color"]]//div[contains(@class, "swatch-option")]'
    OPTION_ICON_SELECTOR = '//div[span[text()="%s"]]//div[contains(@class, "swatch-option")]'
    QUALITY_TEXTBOX_SELECTOR = "#qty"
    FINAL_PRICE_TEXT_SELECTOR = '.product-info-price [data-price-type="finalPrice"]'
    ADD_TO_CART_BUTTON_SELECTOR = 'button[title="Add to Cart"]'
    PRODUCT_NAME_SELECTOR = '[data-ui-id="page-title-wrapper"]'


    def __init__(self, page: Page):
        self.page = page
    

    def select_option_value(self, option_type, option_value=None):
        all_options = None 

        if option_type.upper() == "SIZE":
            all_options = self.page.locator(f'xpath={self.SIZE_ICON_SELECTOR}')
        elif option_type.upper() == "COLOR":
            all_options = self.page.locator(f'xpath={self.COLOR_ICON_SELECTOR}')
        else:
            raise Exception("Invalid option type")

        if option_value:
            options = all_options.all()
            option = next((opt for opt in options if opt.text_content().strip() == option_value), None)
            if option:
                option.click()
            else:
                raise Exception(f"Option '{option_value}' not found")
        else:
            options = all_options.all()
            if options:
                import random
                random.choice(options).click()
            else:
                raise Exception("No options available to select")

    def get_current_product_info(self):
        product_name = self.page.locator(f'css={self.PRODUCT_NAME_SELECTOR}').inner_text()
        final_price = self.page.locator(f'css={self.FINAL_PRICE_TEXT_SELECTOR}').inner_text()
        return {"product_name": product_name, "final_price": final_price}
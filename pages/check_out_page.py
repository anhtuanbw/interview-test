from playwright.sync_api import Page
from pages.base_page import BasePage

class CheckOutPage(BasePage):
    ITEM_IN_CART_TEXT_SELECTOR = ".items-in-cart"
    PRODUCT_CONTAINER_SELECTOR = '.product-item-details'
    STREET_ADDRESS_SELECTOR = '[name="street[0]"]'
    CITY_SELECTOR = '[name="city"]'
    REGION_SELECTOR = '[name="region_id"]'
    POSTAL_CODE_SELECTOR = '[name="postcode"]'
    COUNTRY_SELECTOR = '[name="country_id"]'
    TELEPHONE_SELECTOR = '[name="telephone"]'
    FIRST_DELIVERY_METHOD_SELECTOR = '.table-checkout-shipping-method tr:first-child input'
    NEXT_BUTTON_SELECTOR = '.continue'
    SHIP_ADDRESS_LIST_SELECTOR = '.shipping-address-items'
    PLACE_ORDER_BUTTON_SELECTOR = '.checkout'
    ORDER_NUMBER_LINK_SELECTOR = '.order-number'


    def __init__(self, page: Page):
        self.page = page
        self.item_in_cart_text = page.locator(self.ITEM_IN_CART_TEXT_SELECTOR)
        self.ship_address_list = page.locator(self.SHIP_ADDRESS_LIST_SELECTOR)
        self.order_number_link = page.locator(self.ORDER_NUMBER_LINK_SELECTOR)
        self.next_button = page.locator(self.NEXT_BUTTON_SELECTOR)

    def show_all_items(self):
        self.item_in_cart_text.click()

    def is_existing_ship_address(self):
        return self.ship_address_list.is_visible()

    def get_all_item_in_cart(self):
        all_items = self.page.locator(self.PRODUCT_CONTAINER_SELECTOR).all()
        items = []
        for item in all_items:
            product_name = item.locator('.product-item-name').inner_text()
            quantity = item.locator('.details-qty .value').inner_text()
            sub_total = item.locator('.subtotal').inner_text()
            items.append({"product_name": product_name, "quantity": int(quantity) , "sub_total": sub_total})
    
        return items

    def enter_valid_address(self, address):
        street_address = self.page.locator(self.STREET_ADDRESS_SELECTOR)
        city = self.page.locator(self.CITY_SELECTOR)
        region = self.page.locator(self.REGION_SELECTOR)
        postal_code = self.page.locator(self.POSTAL_CODE_SELECTOR)
        country = self.page.locator(self.COUNTRY_SELECTOR)
        telephone = self.page.locator(self.TELEPHONE_SELECTOR)

        street_address.fill(address["street_address"])
        city.fill(address["city"])
        region.select_option(label=address["region"])
        postal_code.fill(address["postal_code"])
        country.select_option(label=address["country"])
        telephone.fill(address["telephone"])
    
    def select_first_delivery_method(self):
        self.page.click(self.FIRST_DELIVERY_METHOD_SELECTOR)

    def click_next(self):
        self.next_button.click()

    def click_place_order(self):
        self.page.click(self.PLACE_ORDER_BUTTON_SELECTOR)

    def get_order_number(self):
        return self.order_number_link.inner_text()
    
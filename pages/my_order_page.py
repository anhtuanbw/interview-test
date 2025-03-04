from playwright.sync_api import Page
from pages.base_page import BasePage

class MyOrdersPage(BasePage):
    EMPTY_MESSAGE_TEXT_SELECTOR = ".empty"
    ORDER_TABLE_SELECTOR = "#my-orders-table"

    def __init__(self, page: Page):
        self.page = page
        self.empty_message = page.locator(self.EMPTY_MESSAGE_TEXT_SELECTOR)
        self.order_table = page.locator(self.ORDER_TABLE_SELECTOR)

    def navigate(self):
        self.page.goto(f"{self.BASE_URL}sales/order/history/")
        self.page.wait_for_load_state("networkidle")

    def is_cart_empty(self):
        return self.empty_message.is_visible()

    def get_all_orders(self):
        orders = []
        for row in self.order_table.locator("tbody tr").all():
            order = {}
            order["order_id"] = row.locator(".id").inner_text()
            order["order_date"] = row.locator(".date").inner_text()
            order["order_status"] = row.locator(".status").inner_text()
            order["order_total"] = row.locator(".total").inner_text()
            orders.append(order)
        return orders
    
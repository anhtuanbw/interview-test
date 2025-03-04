import pytest
from decimal import Decimal
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from pages.product_search_page import ProductSearchPage
from pages.check_out_page import CheckOutPage
from pages.my_order_page import MyOrdersPage
from utils.list_utils import normalize_items

# Load the feature file
scenarios("../features/order_items.feature")


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def product_detail(page):
    return ProductDetailPage(page)

@pytest.fixture
def product_search_page(page):
    return ProductSearchPage(page)

@pytest.fixture
def check_out_page(page):
    return CheckOutPage(page)

@pytest.fixture
def my_orders_page(page):
    return MyOrdersPage(page)

@given("the user is logged in as a registered user")
def login_as_registered_user(home_page, login_page):
    home_page.navigate()
    home_page.navigate_to_sign_in()
    login_page.login("tuan101@yopmail.com", "At123456")

@when(parsers.parse('the user adds the following items to the cart:\n{items}'))
def add_items_to_cart(home_page, product_search_page, product_detail, items):
    global added_items
    added_items = []
    items = [item.strip().split('|') for item in items.strip().split('\n')[1:]]
    for item in items:
        _, category, item_name, quantity, _ = item
        home_page.navigate_to_product_category(category.strip())
        product_search_page.open_random_product()
        product_detail.select_option_value("Size")
        product_detail.select_option_value("Color")
        product_detail.page.fill("#qty", quantity.strip())
        product_detail.page.click('button[title="Add to Cart"]')
        product_detail.page.wait_for_load_state("networkidle")
        current_product = product_detail.get_current_product_info()
        added_items.append({
            "quantity": int(quantity.strip()),
            "sub_total": "${:.2f}".format(float(current_product['final_price'].replace('$', '')) * int(quantity.strip())),
            **current_product
        })

@when("the user proceeds to the Cart page")
def proceed_to_cart_page(home_page):
    home_page.check_out_cart()


def normalize_items(items):
    return sorted([
        {
            'product_name': item['product_name'],
            'quantity': item['quantity'],
            'sub_total': Decimal(item['sub_total'].replace('$', '')) 
        }
        for item in items
    ], key=lambda x: (x['product_name'], x['quantity'], x['sub_total']))

@when("the user reviews the Order Summary including products and prices")
def review_order_summary(check_out_page):
    check_out_page.show_all_items()
    all_items = check_out_page.get_all_item_in_cart()
    
    normalized_added_items = normalize_items(added_items)
    normalized_all_items = normalize_items(all_items)
    assert normalized_added_items == normalized_all_items
    
@when("the user enters a valid delivery address")
def enter_delivery_address(check_out_page):
    if check_out_page.is_existing_ship_address():
        return
    address = {
        "street_address": "123 Main St",
        "city": "City",
        "region": "Alaska",
        "postal_code": "12345",
        "country": "United States",
        "telephone": "1234567890"
    }
    check_out_page.enter_valid_address(address)

@when("the user selects a delivery method")
def select_delivery_method(check_out_page):
    check_out_page.select_first_delivery_method()

@when("the user places the order")
def place_order(check_out_page):
    check_out_page.click_next()
    check_out_page.click_place_order()

@then("the order should be successfully submitted")
def verify_order_submission(check_out_page):
    global order_number
    order_number = check_out_page.get_order_number()
    assert order_number

@then('the order should be visible under "My Orders"')
def verify_order_in_my_orders(my_orders_page):
    my_orders_page.navigate()
    orders = my_orders_page.get_all_orders()
    assert any(order['order_id'] == order_number for order in orders)

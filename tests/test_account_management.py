import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.my_account_page import MyAccountHomePage
from pages.account_setting_page import AccountSettingPage
from pages.update_password_page import UpdatePasswordPage

# Load the feature file
scenarios("../features/myer_account_management.feature")


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def my_account_page(page):
    return MyAccountHomePage(page)

@pytest.fixture
def account_settings_page(page):
    return AccountSettingPage(page)

@pytest.fixture
def password_change_page(page):
    return UpdatePasswordPage(page)

@given("the user is on the login page")
def navigate_to_login_page(login_page):
    login_page.navigate()


@when(parsers.re(r'the user enters username "(?P<username>.+)" and password "(?P<password>.+)"'))
def enter_credentials(login_page, username, password):
    login_page.enter_credentials(username, password)


@when("the user clicks the login button")
def click_login_button(login_page):
    login_page.click_login()


@then("the user should be redirected to the account dashboard")
def verify_post_login_redirect(page):
    assert "account/home" in page.url


@given("the user is logged into their Myer account")
def navigate_to_login_page(home_page):
    home_page.navigate(force_login=True)


@when("the user navigates to the account settings page")
def navigate_to_my_account(home_page):
    home_page.navigate_to_my_account()


@then("the account settings page should display")
def check_my_account_page_show_up(my_account_page):
    assert my_account_page.is_my_account_page_showing()


@given("the user is on the account settings page")
@when("the user navigate to the account settings page")
def navigate_to_account_settings_page(home_page, my_account_page):
    home_page.navigate(force_login=True)
    home_page.navigate_to_my_account()
    my_account_page.navigate_to_account_settings()


@when(parsers.re(r'the user updates their last name to "(?P<last_name>.+)", and mobile number to "(?P<mobile_phone>.+)"'))
def update_user_data(account_settings_page, last_name, mobile_phone):
    account_settings_page.input_last_name(last_name)
    account_settings_page.input_mobile_number(mobile_phone)


@when('clicks the Update button')
def click_save_changes(account_settings_page):
    account_settings_page.click_update()


@then("the Success message should be displayed")
def verify_confirmation_message(account_settings_page):
    assert account_settings_page.get_notification_message().strip() == "Your account has been successfully updated"


@then("the password update success message should be displayed")
def verify_confirmation_message(account_settings_page):
    assert account_settings_page.get_notification_message().strip() == "Your password has successfully updated"



@when('clicks the "Save Changes" button')
def click_save_changes(password_change_page):
    password_change_page.click_save_changes()


@when("the user click on Update password link")
def click_update_password_link(account_settings_page):
    account_settings_page.click_update_password_link()


@when(parsers.re(r'enter the old password is "(?P<old_password>.+)" and new password is "(?P<new_password>.+)"'))
def enter_old_and_new_password(password_change_page, old_password, new_password):
    password_change_page.input_current_password(old_password)
    password_change_page.input_new_password(new_password)


@given('the user is logged out')
def log_out_current_user(home_page):
    home_page.sign_out_current_user()


@when(parsers.re(r'logs in with username "(?P<username>.+)" and password "(?P<password>.+)"'))
def login_with_credential(login_page, username, password):
    login_page.navigate()
    login_page.enter_credentials(username, password)
    login_page.click_login()


@then(parsers.re(r'it should show lastname is "(?P<last_name>.+)" and mobile number is "(?P<mobile_phone>.+)"'))
def verify_curent_last_name_and_mobile_number(account_settings_page, last_name, mobile_phone):
    assert account_settings_page.get_current_last_name() == last_name
    assert account_settings_page.get_current_mobile() == mobile_phone

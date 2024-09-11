import pytest
from pytest_bdd import given, when, then, scenarios
from pages.login_page import LoginPage

scenarios("login.feature")


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@given('I am on the login page')
def open_login_page(login_page):
    login_page.open()


@when('I enter valid credentials')
def enter_valid_credentials(login_page):
    login_page.enter_credentials('testhannapeshko@gmail.com', '123456')


@when('I click login button')
def click_login(login_page):
    login_page.click_login()


@then('I should be redirected to my account page')
def check_redirection_to_my_account_page(login_page):
    expected_url = 'http://www.automationpractice.pl/index.php?controller=my-account'
    current_url = login_page.wait_for_redirect(expected_url)
    assert current_url == expected_url, (
        f"Expected URL: '{expected_url}' but got: '{current_url}'"
    )


@when('I enter invalid credentials')
def enter_invalid_credentials(login_page):
    login_page.enter_credentials('invalid@example.com', 'wrongpassword')


@then('I should see an error message')
def check_error_message(login_page):
    expected_error_message = 'Authentication failed'
    actual_error_message = login_page.get_error_message()
    assert expected_error_message in actual_error_message, (
        f"Expected error message: '{expected_error_message}' but got: '{actual_error_message}'"
    )

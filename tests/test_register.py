import uuid
import pytest
from pytest_bdd import given, when, then, scenarios
from pages.register_page import RegisterPage

scenarios("register.feature")


@pytest.fixture
def register_page(driver):
    return RegisterPage(driver)


@given('I am on the registration page')
def open_register_page(register_page):
    register_page.open()


@when('I enter a valid email')
def enter_valid_email(register_page):
    # we don't have access to db, so that can't use fixtures there.
    # just random email generation to send unique values each execution
    random_email = f"testhannapeshko+{uuid.uuid4().hex[:8]}@gmail.com"
    register_page.enter_email(random_email)


@when('I click create an account button')
def click_create_account_button(register_page):
    register_page.click_create_account()


@then('I should be redirected to the account creation page')
def check_redirection_to_account_creation_page(register_page):
    expected_url = 'http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation'
    current_url = register_page.wait_for_redirect(expected_url)
    assert current_url == expected_url, (
        f"Expected URL: '{expected_url}' but got: '{current_url}'"
    )


@when('I enter valid details for account creation')
def enter_valid_user_details(register_page):
    register_page.enter_user_details('Hanna', 'Peshko', 'password123')


@when('I submit the registration form')
def submit_registration_form(register_page):
    register_page.click_register()


@then('I should be redirected to my account page')
def check_redirection_to_my_account_page(register_page):
    expected_url = 'http://www.automationpractice.pl/index.php?controller=my-account'
    current_url = register_page.wait_for_redirect(expected_url)
    assert current_url == expected_url, (
        f"Expected URL: '{expected_url}' but got: '{current_url}'"
    )


@when('I enter an already registered email')
def enter_already_registered_email(register_page):
    register_page.enter_email('testhannapeshko@gmail.com')


@then('I should see an error message email has already been registered')
def check_email_already_registered_error(register_page):
    expected_error_message = (
        'An account using this email address has already been registered. Please enter a valid password or request '
        'a new one.'
    )
    actual_error_message = register_page.get_create_account_error_message()
    assert expected_error_message in actual_error_message, (
        f"Expected error message: '{expected_error_message}' but got: '{actual_error_message}'"
    )


@when('I enter invalid details for account creation')
def enter_invalid_user_details(register_page):
    register_page.enter_user_details('Hanna72832', 'Peshko2834581', '')


@then('I should see error messages for invalid details')
def check_invalid_details_error_message(register_page):
    expected_errors = [
        'lastname is invalid.',
        'firstname is invalid.',
        'passwd is required.'
    ]
    actual_error_message = register_page.get_register_error_message()

    for expected_error in expected_errors:
        assert expected_error in actual_error_message, (
            f"Expected '{expected_error}' but got '{actual_error_message}'"
        )

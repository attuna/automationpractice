import time
import pytest
from pytest_bdd import given, when, then, scenarios
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage


scenarios('shopping_flow.feature')


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def product_detail_page(driver):
    return ProductDetailPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@given('I am on the homepage')
def go_to_homepage(home_page):
    home_page.open()


@when('I select a product category')
def select_category(home_page):
    home_page.select_category('Dresses')


@when('I choose a product')
def choose_product(home_page):
    home_page.select_product('Printed Summer Dress')


@then('I am redirected to the product detail page')
def check_redirection_to_product_detail_page(driver):
    expected_url_part = 'id_product='
    current_url = driver.current_url
    assert expected_url_part in current_url, f"Expected URL to contain '{expected_url_part}', but got '{current_url}'"


@when('I select available size')
def select_size(product_detail_page):
    time.sleep(3)
    product_detail_page.select_size('L')


@when('I add the product to the cart')
def add_to_cart(product_detail_page):
    product_detail_page.add_to_cart()


@when('I proceed to checkout')
def proceed_to_checkout(product_detail_page):
    product_detail_page.proceed_to_checkout()


@then('I should be redirected to the checkout page')
def check_redirection_to_checkout_page(cart_page):
    expected_url = 'http://www.automationpractice.pl/index.php?controller=order'
    current_url = cart_page.wait_for_redirect(expected_url)
    assert current_url == expected_url, (
        f"Expected URL: '{expected_url}' but got: '{current_url}'"
    )


@then('the product should be in the cart')
def verify_product_in_cart(cart_page):
    cart_page.open()
    assert cart_page.is_product_in_cart('Printed Summer Dress'), "Product not found in cart"

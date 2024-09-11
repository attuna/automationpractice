import pytest
from pytest_bdd import scenarios, given, when, then
from pages.sorting_filtering_page import SortingFilteringPage

scenarios('sorting_filtering.feature')


@pytest.fixture
def sorting_filtering_page(driver):
    return SortingFilteringPage(driver)


@given('I am on the product listing page')
def open_product_listing_page(sorting_filtering_page):
    sorting_filtering_page.open()


@when('I filter items by category')
def filter_items_by_category(sorting_filtering_page):
    sorting_filtering_page.filter_products('Summer Dresses')


@when('I sort items by price asc')
def sort_items_asc(sorting_filtering_page):
    sorting_filtering_page.sort_products('Price: Lowest first')


@then('I should see items sorted by price in ascending order')
def verify_items_sorted_asc(sorting_filtering_page):
    assert sorting_filtering_page.is_sorted_by_price(order='asc')


@when('I sort items by price desc')
def sort_items_desc(sorting_filtering_page):
    sorting_filtering_page.sort_products('Price: Highest first')


@then('I should see items sorted by price in descending order')
def verify_items_sorted_desc(sorting_filtering_page):
    assert sorting_filtering_page.is_sorted_by_price(order='desc')

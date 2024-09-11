from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class SortingFilteringPage(BasePage):
    URL = 'http://www.automationpractice.pl/index.php?id_category=8&controller=category'

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super().open(self.URL)

    def filter_products(self, filter_option):
        filter_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, filter_option))
        )
        filter_link.click()

    def sort_products(self, sort_option):
        sort_select = self.wait.until(
            EC.presence_of_element_located((By.ID, 'selectProductSort'))
        )
        select = Select(sort_select)
        select.select_by_visible_text(sort_option)

    def is_sorted_by_price(self, order='asc'):
        if order not in ['asc', 'desc']:
            raise ValueError(f"Invalid order: {order}. Use 'asc' for ascending or 'desc' for descending order.")

        prices = []
        price_elements = self.driver.find_elements(By.CSS_SELECTOR, '.price.product-price')

        for item in price_elements:
            price_text = item.text.strip().replace('$', '').replace(',', '')
            if price_text:
                try:
                    price = float(price_text)
                    prices.append(price)
                except ValueError:
                    print(f"Invalid price encountered: {price_text}")
                    continue

        sorted_prices = sorted(prices)
        if order == 'asc':
            return prices == sorted_prices
        elif order == 'desc':
            return prices == sorted_prices[::-1]

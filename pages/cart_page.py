from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    URL = 'http://www.automationpractice.pl/index.php?controller=order'

    def open(self):
        super().open(self.URL)

    def is_product_in_cart(self, product_name):
        try:
            self.driver.find_element(By.LINK_TEXT, product_name)
            return True
        except:
            return False

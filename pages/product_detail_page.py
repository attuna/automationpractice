from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class ProductDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_size(self, size):

        size_dropdown = self.driver.find_element(By.ID, 'group_1')

        select = Select(size_dropdown)
        select.select_by_visible_text(size)

    def add_to_cart(self):
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.NAME, 'Submit'))
        )
        add_to_cart_button.click()

    def proceed_to_checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Proceed to checkout']"))
        )
        checkout_button.click()

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    URL = 'http://www.automationpractice.pl/index.php?id_category=3&controller=category'

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.URL)

    def select_category(self, category_name):
        css_selector = f"a[title='{category_name}']"
        category_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        category_link.click()

    def select_product(self, product_name):
        product_element = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, product_name))
        )
        product_element.click()

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage(BasePage):
    URL = 'http://automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation'

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super().open(self.URL)

    def enter_first_name(self, first_name):
        first_name_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'customer_firstname'))
        )
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'customer_lastname'))
        )
        last_name_field.send_keys(last_name)

    def enter_email(self, email):
        email_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'email_create'))
        )
        email_field.send_keys(email)

    def click_create_account(self):
        create_account_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'SubmitCreate'))
        )
        create_account_button.click()

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'passwd'))
        )
        password_field.send_keys(password)

    def click_register(self):
        register_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'submitAccount'))
        )
        register_button.click()

    def enter_user_details(self, first_name, last_name, password):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_password(password)

    def get_create_account_error_message(self):
        error_element = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'create_account_error'))
        )
        return error_element.text

    def get_register_error_message(self):
        error_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert.alert-danger'))
        )
        return error_element.text

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    URL = 'http://www.automationpractice.pl/index.php?controller=authentication&back=my-account'

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super().open(self.URL)

    def enter_email(self, email):
        email_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'email'))
        )
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'passwd'))
        )
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'SubmitLogin'))
        )
        login_button.click()

    def enter_credentials(self, email, password):
        self.enter_email(email)
        self.enter_password(password)

    def get_error_message(self):
        error_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert.alert-danger'))
        )
        return error_element.text

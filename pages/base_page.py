from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def wait_for_redirect(self, expected_url):
        self.wait.until(EC.url_to_be(expected_url))
        return self.driver.current_url

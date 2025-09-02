from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    error_message = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    required_field_error = (By.CSS_SELECTOR, "span.oxd-input-field-error-message")

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self):
        """Error message for invalid credentials"""
        return self.get_text(self.error_message)

    def get_required_error(self):
        """Return all 'Required' field error messages"""
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(self.required_field_error)
        )
        return [elem.text for elem in elements]

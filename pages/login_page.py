from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)

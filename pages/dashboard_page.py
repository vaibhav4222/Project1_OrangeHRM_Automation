from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    dashboard_header = (By.TAG_NAME, "h6")

    def get_header_text(self):
        return self.get_text(self.dashboard_header)

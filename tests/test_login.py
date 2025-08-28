import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.title("Test OrangeHRM Login")
def test_valid_login(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open("https://opensource-demo.orangehrmlive.com/")

    login_page.login("Admin", "admin123")

    header = dashboard_page.get_header_text()

    assert "Dashboard" in header

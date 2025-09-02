import json
import pytest
from pathlib import Path
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# Load credentials
BASE_DIR = Path(__file__).resolve().parent.parent
CREDENTIALS_FILE = BASE_DIR / "testdata" / "credentials.json"

with open(CREDENTIALS_FILE) as f:
    credentials = json.load(f)


@pytest.mark.smoke
def test_valid_login(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login(credentials["valid"]["username"], credentials["valid"]["password"])

    assert "Dashboard" in dashboard_page.get_header_text(), "Valid login failed!"


@pytest.mark.negative
def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login(credentials["invalid"]["username"], credentials["invalid"]["password"])

    error = login_page.get_error_message()
    assert "Invalid credentials" in error, "Error message not shown for invalid login!"


@pytest.mark.negative
def test_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("", "admin123")

    errors = login_page.get_required_error()
    assert "Required" in errors[0], "Validation error not shown for empty username!"


@pytest.mark.negative
def test_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login(credentials["empty_password"]["username"], credentials["empty_password"]["password"])

    errors = login_page.get_required_error()
    assert any("Required" in e for e in errors), "Validation error not shown for empty password!"


@pytest.mark.negative
def test_empty_both_fields(driver):
    login_page = LoginPage(driver)
    login_page.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login(credentials["empty_both"]["username"], credentials["empty_both"]["password"])

    errors = login_page.get_required_error()
    assert len(errors) >= 2, "Both fields should show 'Required' validation errors!"
    assert all("Required" in msg for msg in errors), "Validation errors missing for empty fields!"


import pytest
from pages.login_page import LoginPage
from pages.add_employee_page import AddEmployeePage


@pytest.mark.ui
@pytest.mark.ui_login
def test_logowanie_ui(driver, logger):
    login_page = LoginPage(driver, logger)
    add_employee_page = AddEmployeePage(driver)

    login_page.open()
    login_page.fill_username_input("admin")
    login_page.fill_password_input("admin")
    login_page.click_sign_in_button()

    assert add_employee_page.anchor_element().is_displayed()



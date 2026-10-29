import pytest
from pages.add_employee_page import AddEmployeePage


@pytest.mark.ui
@pytest.mark.ui_create_employee
def test_dodanie_pracownika_ui(zalogowany_driver, employee_data):
    ### Arrange
    driver = zalogowany_driver
    add_employee_page = AddEmployeePage(driver)
    employee_data = employee_data

    ### Act
    add_employee_page.fill_form(employee_data)

    ### Assert
    add_employee_page.assert_employee_data(employee_data)

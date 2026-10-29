import pytest
from pages.add_employee_page import AddEmployeePage


@pytest.mark.ui
@pytest.mark.ui_create_employee
def test_dodanie_pracownika_uifull(zalogowany_driver, employee_data):
    ### Arrange
    add_employee_page = AddEmployeePage(zalogowany_driver)

    ### Act
    add_employee_page.fill_name_input(employee_data.get("name"))
    add_employee_page.fill_salary_input(employee_data.get("salary"))
    add_employee_page.fill_age_input(employee_data.get("age"))
    add_employee_page.select_position(employee_data.get("position"))
    add_employee_page.check_on_vacation(employee_data.get("on_leave"))
    add_employee_page.click_add_button()

    ### Assert
    table_cells = add_employee_page.return_last_employee_row()
    assert table_cells[1].text == employee_data["name"]
    assert table_cells[2].text == str(employee_data["salary"])
    assert table_cells[3].text == str(employee_data["age"])
    assert table_cells[4].text == employee_data["position"]
    if employee_data["on_leave"]:
        assert table_cells[5].text == "✅"
    else:
        assert table_cells[5].text == "❌"
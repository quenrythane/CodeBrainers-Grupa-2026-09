import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.add_employee_page import AddEmployeePage


@pytest.mark.ui
@pytest.mark.ui_create_employee
def test_dodanie_pracownika_ui(zalogowany_driver):
    ### Arrange
    driver = zalogowany_driver
    add_employee_page = AddEmployeePage(driver)


    employee_data = {
        "name"  : "Bartek Tester",
        "salary":  7000,
        "age"   : 25,
        "position": "Junior QA",
        "on_leave": True
    }


    ### Act
    # add_employee_page.fill_name_input(employee_data["name"])
    # add_employee_page.fill_salary_input(employee_data["salary"])
    # add_employee_page.fill_age_input(employee_data["age"])
    # add_employee_page.select_position(employee_data["position"])
    # add_employee_page.check_on_vacation(employee_data["on_leave"])
    # add_employee_page.click_add_button()

    add_employee_page.fill_name_input("xdxd")
    input("Press Enter to continue...")  # Dodaj to, aby zatrzymać test i sprawdzić, czy formularz jest wypełniony poprawnie
    add_employee_page.fill_form(employee_data)
    input("Press Enter to continue...")  # Dodaj to, aby zatrzymać test i sprawdzić, czy formularz jest wypełniony poprawnie



    ### Assert
    sleep(1)  # czekamy na odświeżenie tabeli
    # pre_table = EC.presence_of_element_located((By.ID, "employees"))
    # table = WebDriverWait(driver, 10).until(pre_table)
    table = driver.find_element(By.ID, "employees")
    table_rows = table.find_elements(By.TAG_NAME, "tr")  # [tr0, tr1, tr2, ...]
    last_table_row = table_rows[-1]  # tr-1
    table_cells = last_table_row.find_elements(By.TAG_NAME, "td")  # [td0, td1, td2, ...]

    assert table_cells[1].text == employee_data["name"]
    assert table_cells[2].text == str(employee_data["salary"])
    assert table_cells[3].text == str(employee_data["age"])
    assert table_cells[4].text == employee_data["position"]
    if employee_data["on_leave"]:
        assert table_cells[5].text == "✅"
    else:
        assert table_cells[5].text == "❌"


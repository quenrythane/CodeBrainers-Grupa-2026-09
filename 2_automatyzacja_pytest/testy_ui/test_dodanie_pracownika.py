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
    driver = zalogowany_driver
    add_employee_page = AddEmployeePage(driver)

    add_employee_page.fill_employee_name(employee_data["name"])

    ### Arrange
    name_input = driver.find_element(By.ID, "name")
    salary_input = driver.find_element(By.ID, "salary")
    age_input = driver.find_element(By.ID, "age")
    position_select = Select(   driver.find_element(By.ID, "position")  )
    on_vacation_checkbox = driver.find_element(By.ID, "on_leave")
    add_button = driver.find_element(By.ID, "submitBtn")

    employee_data = {
        "name"  : "Janek Tester",
        "salary":  7000,
        "age"   : 25,
        "position": "Junior QA",
        "on_leave": True
    }


    ### Act
    name_input.send_keys(employee_data["name"])
    salary_input.send_keys(employee_data["salary"])
    age_input.send_keys(employee_data["age"])
    position_select.select_by_visible_text("Junior QA")
    if employee_data["on_leave"]:
        on_vacation_checkbox.click()
    add_button.click()


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


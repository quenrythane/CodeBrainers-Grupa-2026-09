from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep


class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.ID, "full_name")
        self.salary_input = (By.ID, "salary")
        self.age_input = (By.ID, "age")
        self.position_select = (By.ID, "position")
        self.on_vacation_checkbox = (By.ID, "on_leave")
        self.add_button = (By.ID, "submitBtn")



    def fill_input(self, locator, value):
        input_element = self.driver.find_element(*locator)
        input_element.clear()
        input_element.send_keys(value)


    def fill_name_input(self, name):
        self.fill_input(self, self.name_input, name)


    def fill_salary_input(self, salary):
        self.fill_input(self, self.salary_input, salary)



    def fill_age_input(self, age):
        self.fill_input(self, self.age_input, age)



    def select_position(self, position):
        position_select = Select(self.driver.find_element(*self.position_select))
        position_select.select_by_visible_text(position)


    def check_on_vacation(self, on_leave):
        on_vacation_checkbox = self.driver.find_element(*self.on_vacation_checkbox)
        on_vacation_checkbox.click() if on_leave else None


    def click_add_button(self):
        add_button = self.driver.find_element(*self.add_button)
        add_button.click()


    def fill_form(self, employee):
        self.fill_name_input(employee.get("name"))
        self.fill_salary_input(employee.get("salary"))
        self.fill_age_input(employee.get("age"))
        self.select_position(employee.get("position"))
        self.check_on_vacation(employee.get("on_leave"))
        self.click_add_button()


    def return_last_employee_row(self):
        sleep(1)
        # pre_table = EC.presence_of_element_located((By.ID, "employees"))
        # table = WebDriverWait(driver, 10).until(pre_table)

        table = self.driver.find_element(By.ID, "employees")
        table_rows = table.find_elements(By.TAG_NAME, "tr")
        last_table_row = table_rows[-1]
        table_cells = last_table_row.find_elements(By.TAG_NAME, "td")  # [td0, td1, td2, ...]
        return table_cells


    def assert_employee_data(self, employee_data):
        table_cells = self.return_last_employee_row()
        assert table_cells[1].text == employee_data["name"]
        assert table_cells[2].text == str(employee_data["salary"])
        assert table_cells[3].text == str(employee_data["age"])
        assert table_cells[4].text == employee_data["position"]
        if employee_data["on_leave"]:
            assert table_cells[5].text == "✅"
        else:
            assert table_cells[5].text == "❌"

    # Keys.ENTER



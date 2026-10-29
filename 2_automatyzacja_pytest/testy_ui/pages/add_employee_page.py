from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver

        self.name_input = (By.ID, "name")
        self.salary_input = (By.ID, "salary")
        self.age_input = (By.ID, "age")
        self.position_select = (By.ID, "position")
        # self.position_select = Select(   driver.find_element(By.ID, "position")  )
        self.on_vacation_checkbox = (By.ID, "on_leave")
        self.add_button = (By.ID, "submitBtn")



    def fill_employee_name(self, name):
        name_input = self.driver.find_element(*self.name_input)
        name_input.send_keys(name)





    # def add_employee(self, employee_data):
    #     self.driver.find_element(By.ID, "name").send_keys(employee_data["name"])
    #     self.driver.find_element(By.ID, "salary").send_keys(employee_data["salary"])
    #     self.driver.find_element(By.ID, "age").send_keys(employee_data["age"])
    #     Select(self.driver.find_element(By.ID, "position")).select_by_visible_text(employee_data["position"])
    #     if employee_data["on_leave"]:
    #         self.driver.find_element(By.ID, "on_leave").click()
    #     self.driver.find_element(By.ID, "submitBtn").click()



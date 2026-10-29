from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.url = "http://127.0.0.1:8000/login"
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.sign_in_button = (By.XPATH, "/html/body/div/form/button")


    def open(self):
        self.logger.info(f"Opening login page: {self.url}")
        self.driver.get(self.url)

    def fill_input(self, locator, value):
        self.logger.info(f"fill input: {locator} with value: {value}")
        input_element = self.driver.find_element(*locator)
        input_element.clear()
        input_element.send_keys(value)

    def fill_username_input(self, username):
        self.fill_input(self.username_input, username)

    def fill_password_input(self, password):
        self.fill_input(self.password_input, password)

    def click_sign_in_button(self):
        self.logger.info("Clicking sign in button")
        button_element = self.driver.find_element(*self.sign_in_button)
        button_element.click()
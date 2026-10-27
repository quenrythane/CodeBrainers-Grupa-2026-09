import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.ui
@pytest.mark.ui_login
def test_logowanie_ui():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.get("http://127.0.0.1:8000/login")

    # locator strategy
    # 1. id
    # 2. name
    # 3. class
    # 4. xpath  # /html/body/div/form/input[1]
    # 5. css selector
    # 6. link text
    # 7. partial link text
    # 8. tag name
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "/html/body/div/form/button")

    username_input.send_keys("admin")
    password_input.send_keys("admin")
    login_button.click()

    name_input = driver.find_element(By.ID, "name")
    assert name_input.is_displayed()



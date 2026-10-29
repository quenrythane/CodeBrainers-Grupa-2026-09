import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)

    return driver


@pytest.fixture
def zalogowany_driver(driver):
    driver.get("http://127.0.0.1:8000/login")
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "/html/body/div/form/button")

    username_input.send_keys("admin")
    password_input.send_keys("admin")
    login_button.click()

    name_input = driver.find_element(By.ID, "name")
    assert name_input.is_displayed()

    return driver
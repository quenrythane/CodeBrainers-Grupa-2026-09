from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/login")
input("1 Naciśnij enter by kontynuować: ")

site_title = driver.title
print(site_title)
input("2 Naciśnij enter by kontynuować: ")

assert site_title == "Login - Employee Manager"
input("3 Naciśnij enter by kontynuować: ")
driver.quit()


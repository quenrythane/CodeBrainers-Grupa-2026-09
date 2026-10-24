

class LoginPage:
    def __init__(self, argument_url):
        self.url = argument_url
        self.username_input = ("id", "username")
        self.password_input = ("id", "password")
        self.login_button = ("id", "submit")

    def fill_username_input(self, username):
        print("Typuje w pole: ", self.username_input)

    def fill_password_input(self, password):
        print("Typuje w pole: ", self.password_input)

    def click_login_button(self):
        print("Klikam w przycisk: ", self.login_button)



page_1 = LoginPage("xd xd xd")
page_1.fill_username_input("admin")
page_1.fill_password_input("admin")
page_1.click_login_button()



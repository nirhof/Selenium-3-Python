from selenium.webdriver.common.by import By

txt_username = (By.NAME, "username")
txt_password = (By.NAME, "password")
button_login = (By.CSS_SELECTOR, "input[type='submit']")
error_login_txt = (By.CSS_SELECTOR, "p[class='error']")


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_txt_username(self):
        return self.driver.find_element(txt_username[0], txt_username[1])

    def get_txt_password(self):
        return self.driver.find_element(txt_password[0], txt_password[1])

    def get_button_login(self):
        return self.driver.find_element(button_login[0], button_login[1])

    def get_txt_error(self):
        return self.driver.find_element(error_login_txt[0], error_login_txt[1])


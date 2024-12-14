from selenium.webdriver.common.by import By

login_register_btn = (By.XPATH, "//*[@content-desc='להתחבר // להירשם']")
continue_without_login_btn = (By.XPATH, "//*[@contentDescription='להמשיך ללא התחברות']")
enter_phone_txt = (By.XPATH, "//*[@class='android.widget.EditText']")
confirm_btn = (By.XPATH, "//*[@contentDescription='אישור']")
invalid_phone_number_error_txt = (By.XPATH, "//*[@content-desc='זה לא נראה כמו מספר בכלל...']")


class PapaJohnsLogin:
    def __init__(self, driver):
        self.driver = driver

    def get_login_register_btn(self):
        return self.driver.find_element(login_register_btn[0], login_register_btn[1])

    def get_continue_without_login_btn(self):
        return self.driver.find_element(continue_without_login_btn[0], continue_without_login_btn[1])

    def get_enter_phone_txt(self):
        return self.driver.find_element(enter_phone_txt[0], enter_phone_txt[1])

    def get_invalid_phone_number_error_txt(self):
        return self.driver.find_element(invalid_phone_number_error_txt[0], invalid_phone_number_error_txt[1])
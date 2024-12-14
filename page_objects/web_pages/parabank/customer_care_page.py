from selenium.webdriver.common.by import By

txt_name = (By.ID, "name")
txt_email = (By.ID, "email")
txt_phone = (By.ID, "phone")
txt_message = (By.ID, "message")
btn_send = (By.CSS_SELECTOR, "input[value='Send to Customer Care']")
# txt_send_success = (By.CSS_SELECTOR, "h1[class='title']+p+p")
txt_send_success = (By.ID, "rightPanel")


class CustomerCarePage:
    def __init__(self, driver):
        self.driver = driver

    def get_txt_name(self):
        return self.driver.find_element(txt_name[0], txt_name[1])

    def get_txt_email(self):
        return self.driver.find_element(txt_email[0], txt_email[1])

    def get_txt_phone(self):
        return self.driver.find_element(txt_phone[0], txt_phone[1])

    def get_txt_message(self):
        return self.driver.find_element(txt_message[0], txt_message[1])

    def get_btn_send(self):
        return self.driver.find_element(btn_send[0], btn_send[1])

    def get_btn_send(self):
        return self.driver.find_element(btn_send[0], btn_send[1])

    def get_txt_send_success(self):
        return self.driver.find_element(txt_send_success[0], txt_send_success[1])


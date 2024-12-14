from selenium.webdriver.common.by import By

start_order_btn = (By.XPATH, "//*[@class='android.widget.ImageView'][@index='2' and @clickable='true']")
order_with_coupon_btn = (By.XPATH, "//*[@contentDescription='הזמנה עם קופון']")
branches_btn = (By.XPATH, "//*[@contentDescription='סניפים']")
login_btn = (By.XPATH, "//*[@contentDescription='התחבר']")
burger_btn = (By.XPATH, "//*[@class='android.widget.Button']")
logged_user_txt = (By.XPATH, "//*[contains(@contentDescription, 'היי') and @index='2']")


class PapaJohnsHomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_start_order_btn(self):
        return self.driver.find_element(start_order_btn[0], start_order_btn[1])

    def get_order_with_coupon_btn(self):
        return self.driver.find_element(order_with_coupon_btn[0], order_with_coupon_btn[1])

    def get_branches_btn(self):
        return self.driver.find_element(branches_btn[0], branches_btn[1])

    def get_login_btn(self):
        return self.driver.find_element(login_btn[0], login_btn[1])

    def get_burger_btn(self):
        return self.driver.find_element(burger_btn[0], burger_btn[1])

    def get_logged_user_txt(self):
        return self.driver.find_element(logged_user_txt[0], logged_user_txt[1])
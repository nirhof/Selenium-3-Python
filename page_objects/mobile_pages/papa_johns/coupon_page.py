from selenium.webdriver.common.by import By

enter_coupon_txt = (By.ID, "coupon_flow_field")
use_coupon_btn = (By.XPATH, "//*[@text='ממש קופון']")
view_benefits_btn = (By.XPATH, "//*[@text='לחץ כאן לצפייה בהטבות שלך']")
alert_popup_msg = (By.ID, "alert-popup_msg")


class PapaJohnsCouponPage:
    def __init__(self, driver):
        self.driver = driver

    def get_enter_coupon_txt(self):
        return self.driver.find_element(enter_coupon_txt[0], enter_coupon_txt[1])

    def get_use_coupon_btn(self):
        return self.driver.find_element(use_coupon_btn[0], use_coupon_btn[1])

    def get_view_benefits_btn(self):
        return self.driver.find_element(view_benefits_btn[0], view_benefits_btn[1])

    def get_alert_popup_msg(self):
        return self.driver.find_element(alert_popup_msg[0], alert_popup_msg[1])

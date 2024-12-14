import allure

from page_objects.mobile_pages.papa_johns import home_page, coupon_page, login
from extensions.mobile_actions import MobileActions
import utilities.manage_pages as page
from extensions.verification import Verifications
import tests_cases.conftest as conf
from utilities.common_ops import get_data, wait, WaitCondition
from utilities.manage_pages import mobile_home

class MobileFlows:
    @staticmethod
    @allure.step('use coupon in Papa Johns application')
    def use_coupon(coupon_code):
        wait(WaitCondition.ELEMENT_CLICKABLE, home_page.order_with_coupon_btn)
        MobileActions.tap(page.mobile_home.get_order_with_coupon_btn())
        MobileActions.click_center_of_screen()
        wait(WaitCondition.ELEMENT_CLICKABLE, coupon_page.enter_coupon_txt)
        MobileActions.update_element_text(page.mobile_coupon_page.get_enter_coupon_txt(), coupon_code)
        MobileActions.tap(page.mobile_coupon_page.get_use_coupon_btn())

    @staticmethod
    @allure.step('Login to Papa Johns app - Enter phone number and send OTP')
    def enter_phone_and_request_otp(phone_number):
        wait(WaitCondition.ELEMENT_CLICKABLE, home_page.login_btn)
        MobileActions.tap(page.mobile_home.get_login_btn())
        MobileActions.tap(page.mobile_papa_login.get_login_register_btn())
        MobileActions.click_center_of_screen()
        wait(WaitCondition.ELEMENT_CLICKABLE, login.enter_phone_txt)
        MobileActions.update_element_text(page.mobile_papa_login.get_enter_phone_txt(), phone_number)

    @staticmethod
    @allure.step('verify invalid coupon error message')
    def verify_invalid_coupon_error_message(expected_message):
        MobileActions.click_center_of_screen()
        actual = page.mobile_coupon_page.get_alert_popup_msg().text
        Verifications.verify_equals(actual, expected_message)

    @staticmethod
    @allure.step('verify invalid phone error message')
    def verify_invalid_phone_message(expected):
        MobileActions.click_center_of_screen()
        wait(WaitCondition.ELEMENT_DISPLAYED, page.mobile_papa_login.get_invalid_phone_number_error_txt())
        actual = page.mobile_papa_login.get_invalid_phone_number_error_txt().get_attribute("contentDescription")
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step('swipe screen flow')
    def swipe_screen(direction):
        width = conf.mobile_size['width']
        height = conf.mobile_size['height']

        start_x = None
        start_y = None
        end_x = None
        end_y = None

        if direction == 'left':
            start_x = width * 0.9
            end_x = width * 0.1
            start_y = end_y = height * 0.5
        if direction == 'right':
            start_x = width * 0.1
            end_x = width * 0.9
            start_y = end_y = height * 0.5
        if direction == 'up':
            start_y = height * 0.9
            end_y = height * 0.1
            start_x = end_x = width * 0.5
        if direction == 'down':
            start_y = height * 0.1
            end_y = height * 0.9
            start_x = end_x = width * 0.5
        MobileActions.swipe(start_x, start_y, end_x, end_y, int(get_data('Swipe_Duration')))

    @staticmethod
    @allure.step('reset application')
    def reset_app():
        MobileActions.reset_app()
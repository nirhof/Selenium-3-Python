import allure
import pytest
from utilities.common_ops import get_data
from workflows.mobile_flows import MobileFlows
import tests_cases.conftest as conf

@pytest.mark.usefixtures('init_mobile_driver')
class TestMobile:

    def setup_method(self):
        MobileFlows.reset_app()

    @allure.title('Test01: use invalid coupon code for ordering pizza')
    @allure.description(
        'This test verifies that attempting to order pizza from Papa Johns with an invalid coupon code results in an error message.')
    def test_verify_invalid_pizza_coupon_error_message_papa_johns(self):
        # Attempt to use an invalid coupon code while ordering pizza
        coupon_code = '1234s'
        MobileFlows.use_coupon(coupon_code)
        # Define the expected error message for an invalid coupon code
        expected = "הקופון אינו תקין : ( כדאי לנסות שוב, אולי התפספס משהו."
        # Verify that the correct error message is displayed for the invalid coupon
        MobileFlows.verify_invalid_coupon_error_message(expected)

    @allure.title('Test02: login papa johns - using invalid phone number')
    @allure.description(
        'This test verifies login process to papa johns with invalid phone number results in an error')
    def test_verify_login_with_invalid_phone_error_message_papa_johns(self):
        # Retrieve test data for phone number (using a method or test data source)
        phone_number = get_data("Phone_Number")
        # Attempt to log in by entering the invalid phone number and requesting OTP
        MobileFlows.enter_phone_and_request_otp(phone_number)
        # Define the expected error message
        expected = "זה לא נראה כמו מספר בכלל..."
        # Verify that the correct error message is shown for an invalid phone number
        MobileFlows.verify_invalid_phone_message(expected)




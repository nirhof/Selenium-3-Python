import allure
import pytest
from utilities.common_ops import get_data
from workflows import web_flows
from workflows.web_flows import WebFlows
import tests_cases.conftest as conf


@pytest.mark.usefixtures('init_web_driver')
class TestWeb:
    @allure.title('Test01: Verify Invalid Login to Parabank')
    @allure.description(
        'This test verifies that attempting to log in with invalid credentials results in error message.')
    @pytest.mark.parametrize('user, password', web_flows.testdata)  # get testdata from csv file
    def test_verify_login_error_parabank(self, user, password):
        # Attempt to log in with invalid credentials
        WebFlows.login_parabank(user, password)
        # Expected error message when login fails
        expected_error_text = "The username and password could not be verified."
        # Verify the login error message is displayed correctly
        WebFlows.verify_login_parabank(expected_error_text)

    @allure.title('Test02: Verify Header Buttons Displayed on Parabank')
    @allure.description('This test verifies that all header buttons are correctly displayed on the Parabank page.')
    def test_verify_header_buttons_displayed(self):
        # Verify that the header buttons are displayed on the Parabank page
        WebFlows.verify_header_button_displayed()

    @allure.title('Test03: Verify Sending Email to Parabank Support')
    @allure.description('This test verifies that an email successfully sent to Parabank customer support.')
    def test_verify_sending_email_to_support(self):
        # Define the contact details for sending an email
        name = "Nir"
        email = "nirtest@gmail.com"
        phone = "0546900242"
        message = "Hello there"
        # Navigate to the contact page on Parabank
        WebFlows.navigate_contact_page_parabank()
        # Send an email to customer care with the provided details
        WebFlows.send_email_to_customer_care_parabank(name, email, phone, message)
        # Expected confirmation message after sending the email
        expected_text = f"Customer Care\nThank you {name}\nA Customer Care Representative will be contacting you."
        # Verify that the email confirmation message is displayed correctly
        WebFlows.verify_email_sent_parabank(expected_text)

    @allure.title('Test04: Verify Number of Products on Parabank')
    @allure.description('This test verifies that the number of products displayed on the Parabank products page.')
    def test_verify_number_of_products(self):
        # Navigate to the products page on the Parabank application.
        WebFlows.navigate_products_page_parabank()
        # Verify that the number of products on the page is equal to expected.
        WebFlows.verify_number_of_products(10)

    # @allure.title('Test05: Verify Parabank Home Screen visually')
    # @allure.description('This test verifies Parabank Home Screen visually.')
    # @pytest.mark.skipif(get_data('Execute_Applitools').lower() == 'no',
    #                     reason='run this test only if Execute_Applitools = yes')
    # def test_verify_visual_parabank_home(self):
    #     conf.eyes.open(self.driver, 'Parabank', 'Parabank Home')
    #     conf.driver.get(get_data('Url'))
    #     conf.eyes.check_window('Parabank Home')

    def teardown_method(self):
        # Navigate back to the home page on the Parabank application.
        WebFlows.go_parabank_home(self)

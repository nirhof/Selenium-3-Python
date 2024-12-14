import allure
import pytest

from extensions.db_actions import DBActions
from extensions.verification import Verifications
from workflows.db_flows import DBFlows
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
@pytest.mark.usefixtures('init_db_connection')
class Test_Web_DB:
    @allure.title('Test01: Verify Sending Email to Parabank Support with DB Customer information')
    @allure.description('This test verifies that an email successfully sent to Parabank customer support.')
    def test_verify_sending_email_to_support(self):
        # Call a function that sends an email to Parabank support using customer data
        DBFlows.send_email_to_customer_care_parabank_with_db_information()
        expected_name = "nir"
        expected_text = f"Customer Care\nThank you {expected_name}\nA Customer Care Representative will be contacting you."
        # Verify that the email confirmation message is displayed correctly
        WebFlows.verify_email_sent_parabank(expected_text)


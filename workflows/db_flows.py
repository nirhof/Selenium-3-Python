import allure

from extensions.db_actions import DBActions
from workflows.web_flows import WebFlows


class DBFlows:
    @staticmethod
    @allure.step('Send email to Parabank Customer Care via Database information')
    def send_email_to_customer_care_parabank_with_db_information():
        columns = ['name', 'email', 'phone', 'message']
        result = DBActions.get_query_result(columns,"customers","name","nir")
        WebFlows.send_email_to_customer_care_parabank(result[0][0],result[0][1],result[0][2],result[0][3])


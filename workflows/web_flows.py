import allure

import page_objects
from extensions.ui_actions import UIActions
import utilities.manage_pages as page
from extensions.verification import Verifications
from utilities.common_ops import wait, WaitCondition, get_data, read_csv
from page_objects.web_pages.parabank import home_page, header_panel, customer_care_page


class WebFlows:
    @staticmethod
    @allure.step('login to Parabank')
    def login_parabank(username: str, password: str):
        UIActions.update_element_text(page.home_page.get_txt_username(), username)
        UIActions.update_element_text(page.home_page.get_txt_password(), password)
        UIActions.click(page.home_page.get_button_login())

    @staticmethod
    @allure.step('Verify login error message on Parabank')
    def verify_login_parabank(expected: str):
        wait(WaitCondition.ELEMENT_EXISTS, home_page.error_login_txt)
        actual = page.home_page.get_txt_error().text
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step('Verify header buttons are displayed on Parabank')
    def verify_header_button_displayed():
        buttons_header_element = [page.header_panel.get_btn_home(),
                                  page.header_panel.get_btn_about_us(),
                                  page.header_panel.get_btn_contact()]
        Verifications.verify_elements_displayed_soft_assert(buttons_header_element)

    @staticmethod
    @allure.step('Navigate to the Contact page on Parabank')
    def navigate_contact_page_parabank():
        wait(WaitCondition.ELEMENT_DISPLAYED, page.header_panel.get_btn_contact())
        UIActions.click(page.header_panel.get_btn_contact())

    @staticmethod
    @allure.step('Send email to Parabank Customer Care')
    def send_email_to_customer_care_parabank(name: str, email: str, phone: str, message: str):
        UIActions.update_element_text(page.customer_care_page.get_txt_name(), name)
        UIActions.update_element_text(page.customer_care_page.get_txt_email(), email)
        UIActions.update_element_text(page.customer_care_page.get_txt_phone(), phone)
        UIActions.update_element_text(page.customer_care_page.get_txt_message(), message)
        UIActions.click(page.customer_care_page.get_btn_send())

    @staticmethod
    @allure.step('Verify email sent confirmation message on Parabank')
    def verify_email_sent_parabank(expected: str):
        wait(WaitCondition.ELEMENT_EXISTS, customer_care_page.txt_send_success)
        actual = page.customer_care_page.get_txt_send_success().text
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step('Navigate to the Products page on Parabank')
    def navigate_products_page_parabank():
        wait(WaitCondition.ELEMENT_DISPLAYED, page.header_panel.get_menu_products())
        UIActions.click(page.header_panel.get_menu_products())

    @staticmethod
    @allure.step('Verify number of products on the products page of Parabank')
    def verify_number_of_products(expected: int):
        Verifications.verify_number_of_elements(page.products_page.get_list_of_products(), expected)

    @staticmethod
    @allure.step('Navigate to the Parabank home page')
    def go_parabank_home(self):
        self.driver.get(get_data("Url"))


# Read the CSV file from the location provided by get_data('DDT_File_Location')
data = read_csv(get_data('DDT_File_users_Location'))
# Create a list of tuples (testdata), where each tuple contains the first two elements (columns)
# of each row in the data read from the CSV file.
testdata = [(row[0], row[1]) for row in data]

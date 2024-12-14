import tests_cases.conftest
from page_objects.desktop_pages.windows_calculator.calculator_page import CalculatorPage
from page_objects.mobile_pages.papa_johns.coupon_page import PapaJohnsCouponPage
from page_objects.mobile_pages.papa_johns.home_page import PapaJohnsHomePage
from page_objects.mobile_pages.papa_johns.login import PapaJohnsLogin
from page_objects.web_pages.parabank.customer_care_page import CustomerCarePage
from page_objects.web_pages.parabank.header_panel import HeaderPanel
from page_objects.web_pages.parabank.home_page import HomePage
from page_objects.web_pages.parabank.products_page import ProductsPage

# Web Objects
home_page = None
header_panel = None
customer_care_page = None
products_page = None

# Mobile Objects
mobile_home = None
mobile_coupon_page = None
mobile_papa_login = None

# Desktop Objects
calculator_page = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['home_page'] = HomePage(tests_cases.conftest.driver)
        globals()['header_panel'] = HeaderPanel(tests_cases.conftest.driver)
        globals()['customer_care_page'] = CustomerCarePage(tests_cases.conftest.driver)
        globals()['products_page'] = ProductsPage(tests_cases.conftest.driver)


    @staticmethod
    def init_mobile_pages():
        globals()['mobile_home'] = PapaJohnsHomePage(tests_cases.conftest.driver)
        globals()['mobile_coupon_page'] = PapaJohnsCouponPage(tests_cases.conftest.driver)
        globals()['mobile_papa_login'] = PapaJohnsLogin(tests_cases.conftest.driver)

    @staticmethod
    def init_desktop_pages():
        globals()['calculator_page'] = CalculatorPage(tests_cases.conftest.driver)


import allure
import pytest

from extensions.verification import Verifications
from utilities.common_ops import get_data
from workflows.desktop_flows import DesktopFlows
import tests_cases.conftest as conf

@pytest.mark.usefixtures('init_desktop_driver')
class TestDesktop:
    def setup_method(self):
        DesktopFlows.calculator_clear()

    @allure.title('Test01: Calculator Addition')
    @allure.description(
        'This test verifies that the calculator performs addition correctly.')
    def test_calculator_addition(self):
        # Perform the addition operation
        DesktopFlows.calculator_calculate("1+2+3")
        # Get the result of the calculation
        result = DesktopFlows.calculator_get_result()
        # Verify that the result is as expected
        Verifications.verify_equals(result, "6")

    @allure.title('Test02: Calculator Subtraction')
    @allure.description(
        'This test verifies that the calculator performs subtraction correctly.')
    def test_calculator_subtraction(self):
        # Perform the subtraction operation
        DesktopFlows.calculator_calculate("10-5-2")
        # Get the result of the calculation
        result = DesktopFlows.calculator_get_result()
        # Verify that the result is as expected
        Verifications.verify_equals(result, "3")

    @allure.title('Test03: Calculator Multiplication')
    @allure.description(
        'This test verifies that the calculator performs multiplication correctly.')
    def test_calculator_multiplication(self):
        # Perform the multiplication operation
        DesktopFlows.calculator_calculate("2*3*4")
        # Get the result of the calculation
        result = DesktopFlows.calculator_get_result()
        # Verify that the result is as expected
        Verifications.verify_equals(result, "24")

    @allure.title('Test04: Calculator Division')
    @allure.description(
        'This test verifies that the calculator performs division correctly.')
    def test_calculator_division(self):
        # Perform the division operation
        DesktopFlows.calculator_calculate("12/4/3")
        # Get the result of the calculation
        result = DesktopFlows.calculator_get_result()
        # Verify that the result is as expected
        Verifications.verify_equals(result, "1")




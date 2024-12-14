import allure

from extensions.ui_actions import UIActions
import utilities.manage_pages as page


class DesktopFlows:
    @staticmethod
    @allure.step('calculator - equation')
    def calculator_calculate(equation):
        for i in equation:
            DesktopFlows.calculator_click(i)
        UIActions.click(page.calculator_page.get_btn_equals())

    @staticmethod
    @allure.step('calculator - get calculator result')
    def calculator_get_result():
        result = page.calculator_page.get_txt_result().text.replace("Display is","").strip()
        return result

    @staticmethod
    @allure.step('calculator - clear')
    def calculator_clear():
        UIActions.click(page.calculator_page.get_btn_clear())

    @staticmethod
    def calculator_click(value):
        if value == '0':
            UIActions.click(page.calculator_page.get_btn_zero())
        elif value == '1':
            UIActions.click(page.calculator_page.get_btn_one())
        elif value == '2':
            UIActions.click(page.calculator_page.get_btn_two())
        elif value == '3':
            UIActions.click(page.calculator_page.get_btn_three())
        elif value == '4':
            UIActions.click(page.calculator_page.get_btn_four())
        elif value == '5':
            UIActions.click(page.calculator_page.get_btn_five())
        elif value == '6':
            UIActions.click(page.calculator_page.get_btn_six())
        elif value == '7':
            UIActions.click(page.calculator_page.get_btn_seven())
        elif value == '8':
            UIActions.click(page.calculator_page.get_btn_eight())
        elif value == '9':
            UIActions.click(page.calculator_page.get_btn_nine())
        elif value == '+':
            UIActions.click(page.calculator_page.get_btn_plus())
        elif value == '-':
            UIActions.click(page.calculator_page.get_btn_minus())
        elif value == '*':
            UIActions.click(page.calculator_page.get_btn_multiply())
        elif value == '/':
            UIActions.click(page.calculator_page.get_btn_divide())
        else:
            raise ValueError(f"Invalid  value '{value}' not found.")


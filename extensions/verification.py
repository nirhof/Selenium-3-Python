import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations
from typing import List


class Verifications:
    @staticmethod
    @allure.step('Verify that actual value "{actual}" equals expected value "{expected}"')
    def verify_equals(actual, expected):
        print(f'actual is {actual}')
        print(f'expected is {expected}')
        assert actual == expected, f'Verify equals failed, actual result:{actual} is not equal to expected:{expected}'

    @staticmethod
    @allure.step('Verify that element "{elem.text}" is displayed')
    def verify_is_displayed(elem: WebElement):
        assert elem.is_displayed(), f'Verify is displayed failed, element:{elem.text} is not displayed'

    @staticmethod
    @allure.step('Soft assert that all elements are displayed')
    def verify_elements_displayed_soft_assert(elements: WebElement):  # using soft assertions
        for i in range(len(elements)):
            print(f"element {i + 1} is {elements[i].text}")
            soft_assert(elements[i].is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step('Verify that all elements are displayed using costume smart assertion')
    def verify_elements_displayed(elements: WebElement):  # using costume smart assertion
        failed_elements = []
        for i in range(len(elements)):
            if not elements[i].is_displayed():
                failed_elements.insert(len(failed_elements), elements[i].text)
        if len(failed_elements) > 0:
            for failed_element in failed_elements:
                print('not all elements are displayed. assertion failed. elements which is not displayed is: ' + str(
                    failed_element))
            raise AssertionError('not all elements are displayed. assertion failed')

    @staticmethod
    @allure.step('Verify number of elements is "{expected}"')
    def verify_number_of_elements(elems: List[WebElement], expected: int):
        print(f"number of elements is {len(elems)}")
        assert len(elems) == expected, f'Number of elements: {str(len(elems))} does not match expected {str(expected)}'

    @staticmethod
    @allure.step('Verify that actual value contains expected value "{expected}"')
    def verify_contains(actual, expected):
        print(f'Actual is: {actual}')
        print(f'Expected: {expected}')
        assert expected in actual, f"Verify contains failed: actual:{actual} does not contain expected:{expected}"

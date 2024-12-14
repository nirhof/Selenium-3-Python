import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from tests_cases.conftest import action


class UIActions:
    @staticmethod
    @allure.step('Click on element')
    def click(element: WebElement):
        element.click()

    @staticmethod
    @allure.step('Update text of element with value "{text}"')
    def update_element_text(element: WebElement, text: str):
        element.clear()
        element.send_keys(text)

    @staticmethod
    @allure.step('Select option by value "{value}" from dropdown')
    def select_drop_down_by_value(element: WebElement, value: str):
        dropdown = Select(element)
        dropdown.select_by_value(value)

    @staticmethod
    @allure.step('Select option by index "{index}" from dropdown')
    def select_drop_down_by_value(element: WebElement, index: int):
        dropdown = Select(element)
        dropdown.select_by_index(index)

    @staticmethod
    @allure.step('Select option by visible text "{visible_text}" from dropdown')
    def select_drop_down_by_value(element: WebElement, visible_text: str):
        dropdown = Select(element)
        dropdown.select_by_visible_text(visible_text)

    @staticmethod
    @allure.step('Mouse hover over element')
    def mouse_hover(element1: WebElement):
        action.move_to_element(element1).click().perform()

    @staticmethod
    @allure.step('Mouse hover over element1 and then element2')
    def mouse_hover_2_elements(element1: WebElement, element2: WebElement):
        action.move_to_element(element1).move_to_element(element2).click().perform()

    @staticmethod
    @allure.step('Right click on element')
    def right_click(element: WebElement, key):
        action.context_click(element).send_keys(key).perform()

    @staticmethod
    @allure.step('Drag element and drop on another element')
    def drag_and_drop(drag: WebElement, drop: WebElement):
        action.drag_and_drop(drag, drop).perform()





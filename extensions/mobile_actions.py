import allure
from appium.webdriver.common.touch_action import TouchAction

import tests_cases.conftest as conf
from extensions.ui_actions import UIActions


class MobileActions(UIActions):
    @staticmethod
    @allure.step('tap on element')
    def tap(element):
        TouchAction(conf.driver).tap(element).perform()

    @staticmethod
    @allure.step('swipe screen')
    def swipe(start_x, start_y, end_x, end_y, duration):
        conf.driver.swipe(start_x, start_y, end_x, end_y, duration)

    @staticmethod
    @allure.step('zoom on element')
    def zoom_in(element,pixels =200):
        action1 = conf.action
        action2 = conf.action2
        x_loc = element.rect['x'] + element.rect['width'] // 2  # Center x-coordinate
        y_loc = element.rect['y'] + element.rect['height'] // 2  # Center y-coordinate

        action1.press(x=x_loc, y=y_loc).move_to(x=x_loc, y=y_loc + pixels).wait(500).release()
        action2.press(x=x_loc, y=y_loc).move_to(x=x_loc, y=y_loc - pixels).wait(500).release()

        # Perform the actions
        action1.perform()
        action2.perform()

    @staticmethod
    @allure.step('pinch on element')
    def pinch(element,pixels =200):
        action1 = conf.action
        action2 = conf.action2
        x_loc = element.rect['x'] + element.rect['width'] // 2  # Center x-coordinate
        y_loc = element.rect['y'] + element.rect['height'] // 2  # Center y-coordinate

        action1.press(x=x_loc, y=y_loc + pixels).move_to(x=x_loc, y=y_loc).wait(500).release()
        action2.press(x=x_loc, y=y_loc - pixels).move_to(x=x_loc, y=y_loc).wait(500).release()

        # Perform the actions
        action1.perform()
        action2.perform()

    @staticmethod
    @allure.step('click the center of the screen')
    def click_center_of_screen(duration: int = 5000):
        # Get screen dimensions
        screen_size = conf.driver.get_window_size()
        screen_width = screen_size['width']
        screen_height = screen_size['height']
        # Calculate the center of the screen
        center_x = screen_width // 2
        center_y = screen_height // 2
        TouchAction(conf.driver).long_press(x=center_x, y=center_y, duration=duration).release().perform()


    @staticmethod
    @allure.step('reset app')
    def reset_app():
        conf.driver.reset()
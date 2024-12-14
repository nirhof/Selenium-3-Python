import csv
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tests_cases.conftest as conf
import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse('C:/Automation/Projects/selenium3-python/configuration/data.xml').getroot()
    return root.find('.//' + node_name).text


def wait(for_element, elem, expected_text=None):
    if for_element == 'element_exists':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.visibility_of(elem))
    elif for_element == 'element_clickable':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.element_to_be_clickable((elem[0], elem[1])))
    elif for_element == 'element_text_present':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.text_to_be_present_in_element((elem[0], elem[1]), expected_text))


def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(tuple(row))  # Convert each row to a tuple
    return data


def get_time_stamp():
    return time.time()


# Enum for specifying conditions to wait for

class WaitCondition:
    ELEMENT_EXISTS = 'element_exists'
    ELEMENT_DISPLAYED = 'element_displayed'
    ELEMENT_CLICKABLE = 'element_clickable'
    ELEMENT_TEXT_PRESENT = 'element_text_present'



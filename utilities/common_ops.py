import csv
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tests_cases.conftest as conf  # Assuming `conf` is where the global driver is defined
import xml.etree.ElementTree as ET  # Used for parsing XML files


# Function to retrieve data from an XML configuration file
def get_data(node_name):
    """
    Fetches the text value of a specified node from the XML configuration.
    Assumes the XML is structured with a root node that contains other nodes.

    Args:
        node_name (str): The name of the XML node to find.

    Returns:
        str: The text content of the specified XML node.
    """
    # Parse the XML configuration file and get the root element
    root = ET.parse('C:/Automation/Projects/selenium3-python/configuration/data.xml').getroot()

    # Find the node by name and return its text value
    return root.find('.//' + node_name).text


# Function to wait for a specific condition on a web element
def wait(for_element, elem, expected_text=None):
    """
    Wait for an element to meet a certain condition using WebDriverWait.

    Args:
        for_element (str): The type of condition to wait for. Options are defined in `WaitCondition`.
        elem (tuple or WebElement): The locator or WebElement to apply the condition to.
        expected_text (str, optional): The text to be checked in case of 'element_text_present'.

    Returns:
        None
    """
    # Use WebDriverWait to wait for the specified condition
    wait_time = int(get_data('WaitTime'))  # Fetch the configured wait time from the XML

    # Depending on the `for_element` condition, wait for the appropriate condition
    if for_element == 'element_exists':
        WebDriverWait(conf.driver, wait_time).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, wait_time).until(EC.visibility_of(elem))
    elif for_element == 'element_clickable':
        WebDriverWait(conf.driver, wait_time).until(EC.element_to_be_clickable((elem[0], elem[1])))
    elif for_element == 'element_text_present':
        WebDriverWait(conf.driver, wait_time).until(EC.text_to_be_present_in_element((elem[0], elem[1]), expected_text))


# Function to read data from a CSV file and return it as a list of tuples
def read_csv(file_name):
    """
    Reads a CSV file and returns its content as a list of tuples.

    Args:
        file_name (str): The path to the CSV file to read.

    Returns:
        list of tuples: Each row in the CSV is returned as a tuple.
    """
    data = []  # List to store the rows from the CSV
    with open(file_name, newline='') as file:
        reader = csv.reader(file)  # Create a CSV reader object
        for row in reader:
            data.append(tuple(row))  # Convert each row to a tuple and append it to the list
    return data


# Function to get the current time in seconds since the epoch
def get_time_stamp():
    """
    Retrieves the current timestamp (in seconds) as a floating-point number.

    Returns:
        float: The current timestamp.
    """
    return time.time()


# Enum-like class to specify different waiting conditions for Selenium
class WaitCondition:
    """
    Enum-like class to specify different wait conditions.
    These are used as arguments in the `wait` function to specify the condition to wait for.
    """
    ELEMENT_EXISTS = 'element_exists'  # Wait for the element to exist in the DOM
    ELEMENT_DISPLAYED = 'element_displayed'  # Wait for the element to be visible on the page
    ELEMENT_CLICKABLE = 'element_clickable'  # Wait for the element to be clickable
    ELEMENT_TEXT_PRESENT = 'element_text_present'  # Wait for specific text to be present
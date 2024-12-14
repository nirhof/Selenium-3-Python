import allure
import requests
from docutils.utils import extract_name_value
from requests import request

header = {'Content-Type': 'application/json'}

class APIActions:
    @staticmethod
    @allure.step('Get Request')
    def get(path):
        response = requests.get(path)
        return response

    @staticmethod
    @allure.step('Extract value from response')
    def extract_value_from_response(response, nodes):
        extract_value = None
        response_json = response.json()
        if len(nodes) == 1:
            extract_value = response_json[nodes[0]]
        elif len(nodes) == 2:
            extract_value = response_json[(nodes[0])][(nodes[1])]
        elif len(nodes) == 3:
            extract_value = response_json[(nodes[0])][(nodes[1])][(nodes[2])]
        return extract_value


    @staticmethod
    @allure.step('POST Request')
    def post(path, payload):
        response = requests.post(path, json=payload)
        return response.status_code


    @staticmethod
    @allure.step('PUT Request')
    def put(path, payload):
        response = requests.put(path, json=payload)
        return response.status_code

    @staticmethod
    @allure.step('DELETE Request')
    def delete(path):
        response = requests.delete(path)
        return response.status_code

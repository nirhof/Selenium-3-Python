import allure

from extensions.api_actions import APIActions
from utilities.common_ops import get_data

url = get_data('API_Base_Url')

class APIFlows:
    @staticmethod
    @allure.step('Get value')
    def get_value_from_api(resources, nodes):
        resources = resources
        response = APIActions.get(url + resources)
        return APIActions.extract_value_from_response(response, nodes)

    @staticmethod
    @allure.step('create new album for user')
    def create_album(user_id, title):
        payload = {'user_id':user_id, 'title': title}
        resources = 'albums/'
        status_code = APIActions.post(url + resources, payload)
        return status_code

    @staticmethod
    @allure.step('update album title for user')
    def update_album(user_id, title, id):
        payload = {'user_id':user_id, 'title': title}
        resources = 'albums/'
        status_code = APIActions.put(url + resources + str(id), payload)
        return status_code

    @staticmethod
    @allure.step('delete album by id')
    def delete_album(id):
        resources = 'albums/'
        status_code = APIActions.delete(url + resources + str(id))
        return status_code

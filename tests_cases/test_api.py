import allure

from extensions.verification import Verifications
from workflows.api_flows import APIFlows

title = 'enim repellat iste'
user_id = '11'

class Test_API:
    @allure.title('Test01: Verify user name from http://localhost:3000/users')
    @allure.description(
        'This test verifies that the user with ID 0 has the name "Leanne Graham" in the API response '
        'from JSONPlaceholder. It checks that the API retrieves the correct user details successfully.'
    )
    def test_verify_user_name_json_place_holder(self):
        # Define the resource endpoint for users
        resources = 'users/'
        # Define the parameters to retrieve the user data
        nodes = [0, 'name']  # 0 is the user ID, and 'name' specifies the field to retrieve
        # Fetch user data from the API using the specified resource and nodes
        actual = APIFlows.get_value_from_api(resources, nodes)
        # Verify that the retrieved user name matches the expected value
        Verifications.verify_equals(actual, "Leanne Graham")

    @allure.title('Test02: create album in http://localhost:3000/albums')
    @allure.description(
        'This test verifies the successful creation of an album for a specific user '
        'using the JSONPlaceholder API. It checks that the API returns a status code '
        'of 201, indicating that the album was created successfully.'
    )
    def test_create_album_json_place_holder(self):
        # Call the API method to create an album with the specified user ID and title
        actual = APIFlows.create_album(user_id, title)
        # Verify that the response status code is 201 (Created)
        Verifications.verify_equals(actual, 201)

    @allure.title('Test03: Update album in http://localhost:3000/albums')
    @allure.description(
        'This test verifies that an album for a specific user can be updated using the JSONPlaceholder API. '
        'It checks that the API returns a status code of 200, indicating that the update was successful.'
    )
    def test_update_album_json_place_holder(self):
        # Define the title and ID of the album to be updated
        title = 'Veni, vidi, vici'
        resources = 'albums/'
        nodes = [-1, 'id']
        id = APIFlows.get_value_from_api(resources, nodes)
        # Call the API method to update the album with the specified user ID, title, and album ID
        actual = APIFlows.update_album(user_id, title, id)
        # Verify that the response status code is 200 (OK), indicating a successful update
        Verifications.verify_equals(actual, 200)

    @allure.title('Test04: Delete album in http://localhost:3000/albums')
    @allure.description(
        'This test verifies that an album can be deleted using the JSONPlaceholder API. '
        'It checks that the API returns a status code of 200, indicating that the deletion was successful.'
    )
    def test_delete_album_json_place_holder(self):
        # Define the resource endpoint for albums
        resources = 'albums/'
        # Get the ID of the last album to delete
        nodes = [-1, 'id']  # Assuming -1 refers to the last album and 'id' specifies the field to retrieve
        id = APIFlows.get_value_from_api(resources, nodes)
        # Call the API method to delete the album with the specified ID
        actual = APIFlows.delete_album(id)
        # Verify that the response status code is 200 (OK), indicating a successful deletion
        Verifications.verify_equals(actual, 200)
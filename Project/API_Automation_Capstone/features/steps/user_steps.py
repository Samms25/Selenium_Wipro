from behave import given, then
from api.user_api import UserAPI
from utilities.response_validator import ResponseValidator
from utilities.failure_analyzer import FailureAnalyzer
from utilities.test_data_reader import TestDataReader


@given("I send a GET request to the users endpoint")
def step_get_users(context):
    user_api = UserAPI()
    context.response = user_api.get_all_users()


@then("the response status code should be 200")
def step_status_code(context):
    assert context.response.status_code == 200


@then("the response should contain users")
def step_users_present(context):
    response_data = context.response.json()

    ResponseValidator.validate_status(
        context.response,
        200
    )

    assert "users" in response_data
    assert len(response_data["users"]) > 0

    first_user = response_data["users"][0]

    ResponseValidator.validate_required_fields(
        first_user,
        ["id", "firstName", "lastName", "age"]
    )

    ResponseValidator.validate_field_types(
        first_user,
        {
            "id": int,
            "firstName": str,
            "lastName": str,
            "age": int
        }
    )


@given("I send a GET request for user ID 1")
def step_get_user_by_id(context):
    user_api = UserAPI()
    context.response = user_api.get_user_by_id(1)


@then("the response should contain user ID 1")
def step_user_id_present(context):
    ResponseValidator.validate_response(
        context.response,
        expected_status=200,
        required_fields=[
            "id",
            "firstName",
            "lastName",
            "age"
        ],
        expected_types={
            "id": int,
            "firstName": str,
            "lastName": str,
            "age": int
        }
    )

    response_data = context.response.json()

    assert response_data["id"] == 1

@given("I have valid new user data")
def step_new_user_data(context):
    reader = TestDataReader()
    data = reader.read_data()

    context.user_data = data["valid_user"]


@when("I send a POST request to create the user")
def step_create_user(context):
    user_api = UserAPI()
    context.response = user_api.create_user(context.user_data)


@then("the create user response status code should be 201")
def step_create_user_status(context):
    assert context.response.status_code == 201


@then("the response should contain the created user")
def step_created_user_present(context):
    response_data = context.response.json()

    assert response_data["firstName"] == "Test"
    assert response_data["lastName"] == "User"

@given("I have updated data for user ID 1")
def step_updated_user_data(context):
    reader = TestDataReader()
    data = reader.read_data()

    context.user_id = 1
    context.updated_data = data["updated_user"]


@when("I send a PUT request to update the user")
def step_update_user(context):
    user_api = UserAPI()

    context.response = user_api.update_user(
        context.user_id,
        context.updated_data
    )


@then("the update user response status code should be 200")
def step_update_user_status(context):
    assert context.response.status_code == 200


@then("the response should contain the updated user")
def step_updated_user_present(context):
    response_data = context.response.json()

    assert response_data["firstName"] == "Updated"
    assert response_data["lastName"] == "User"    

@given("I want to delete user ID 1")
def step_delete_user_setup(context):
    context.user_id = 1


@when("I send a DELETE request for the user")
def step_delete_user(context):
    user_api = UserAPI()

    context.response = user_api.delete_user(
        context.user_id
    )


@then("the delete user response status code should be 200")
def step_delete_user_status(context):
    assert context.response.status_code == 200


@then("the response should confirm the user was deleted")
def step_delete_confirmation(context):
    response_data = context.response.json()

    assert response_data["isDeleted"] is True    

@given("I send a GET request for a non-existent user ID")
def step_get_nonexistent_user(context):
    user_api = UserAPI()
    context.response = user_api.get_user_by_id(9999)


@then("the user response status code should be 404")
def step_nonexistent_user_status(context):

    analysis = FailureAnalyzer.analyze_response(
        context.response
    )

    print("\n===== API FAILURE ANALYSIS =====")
    print(f"Status Code: {analysis['status_code']}")
    print(f"Failure Category: {analysis['category']}")

    assert context.response.status_code == 404


@then("the response should contain a not found message")
def step_not_found_message(context):
    response_data = context.response.json()

    assert "message" in response_data    
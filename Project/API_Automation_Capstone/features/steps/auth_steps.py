from behave import given, when, then
from api.auth_api import AuthAPI


@given("the user has valid login credentials")
def step_valid_credentials(context):
    context.username = "emilys"
    context.password = "emilyspass"


@when("the user sends a login request")
def step_login_request(context):
    auth_api = AuthAPI()

    context.response = auth_api.login(
        context.username,
        context.password
    )


@then("the login response status code should be 200")
def step_status_code(context):
    assert context.response.status_code == 200


@then("the response should contain an access token")
def step_access_token(context):
    response_data = context.response.json()

    assert "accessToken" in response_data
    assert response_data["accessToken"]

@given("the user has invalid login credentials")
def step_invalid_credentials(context):
    context.username = "invalid_user"
    context.password = "wrong_password"


@then("the login response status code should be 400")
def step_invalid_login_status(context):
    assert context.response.status_code == 400


@then("the response should contain a login error")
def step_login_error(context):
    response_data = context.response.json()

    assert "message" in response_data    
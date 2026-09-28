Feature: User Authentication

  Scenario: Successful user login
    Given the user has valid login credentials
    When the user sends a login request
    Then the login response status code should be 200
    And the response should contain an access token

  Scenario: Login with invalid credentials
    Given the user has invalid login credentials
    When the user sends a login request
    Then the login response status code should be 400
    And the response should contain a login error
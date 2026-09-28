Feature: User Management

  Scenario: Get all users successfully
    Given I send a GET request to the users endpoint
    Then the response status code should be 200
    And the response should contain users

  Scenario: Get a user by ID successfully
    Given I send a GET request for user ID 1
    Then the response status code should be 200
    And the response should contain user ID 1

  Scenario: Create a new user successfully
    Given I have valid new user data
    When I send a POST request to create the user
    Then the create user response status code should be 201
    And the response should contain the created user 

  Scenario: Update an existing user successfully
    Given I have updated data for user ID 1
    When I send a PUT request to update the user
    Then the update user response status code should be 200
    And the response should contain the updated user    

  Scenario: Delete an existing user successfully
    Given I want to delete user ID 1
    When I send a DELETE request for the user
    Then the delete user response status code should be 200
    And the response should confirm the user was deleted   

  Scenario: Get a non-existent user
    Given I send a GET request for a non-existent user ID
    Then the user response status code should be 404
    And the response should contain a not found message     
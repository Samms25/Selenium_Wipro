# API Automation Capstone

## 1. Project Overview

This project implements an automated API testing framework for User
Management and Authentication APIs.

The framework is developed using Python and the Requests library, with
Behave used for Behavior-Driven Development (BDD). It includes reusable
API classes, configuration management, test data handling, response
validation, logging, failure analysis, and Allure reporting.

The project is designed to provide reliable, maintainable, and reusable
API automation with clear test execution results.

## 2. Project Objective

The main objectives of this project are:

- Automate REST API testing using Python.
- Automate User Management API operations.
- Automate authentication scenarios.
- Implement Behavior-Driven Development (BDD) using Behave.
- Validate API response status codes, required fields, and data types.
- Implement reusable API and utility components.
- Implement logging and API failure analysis.
- Generate test execution reports using Allure.
- Maintain the project using Git and GitHub.

## 3. Project Scenario

The project focuses on automating a sample REST API for User Management
and Authentication.

The User Management API automation covers the following operations:

- Retrieve all users using GET.
- Retrieve a specific user by ID using GET.
- Create a new user using POST.
- Update an existing user using PUT.
- Delete a user using DELETE.
- Validate the response for a non-existent user.

Authentication scenarios are also automated to validate successful
authentication and invalid login handling.

The framework uses reusable API classes and BDD feature files to
organize and execute these scenarios.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Requests | REST API communication |
| Behave | BDD-based API test automation |
| Allure | Test execution reporting |
| Pytest | Supporting test validation |
| JSON | Test data and API response handling |
| Git | Version control |
| GitHub | Source code repository |
| VS Code | Development environment |


## 5. Framework Architecture

The framework follows a modular architecture to keep the API automation
code reusable, maintainable, and easy to understand.

```text
Feature Files
      ↓
Step Definitions
      ↓
API Classes
      ↓
Requests Library
      ↓
REST API
      ↓
API Response
      ↓
Response Validation
      ↓
Logging & Failure Analysis
      ↓
Allure Reporting
 ```

## 6. Project Structure

```text
API_Automation_Capstone/
│
├── api/
│   ├── auth_api.py
│   └── user_api.py
│
├── config/
│   └── config.ini
│
├── features/
│   ├── authentication.feature
│   ├── user_management.feature
│   ├── environment.py
│   └── steps/
│       ├── auth_steps.py
│       └── user_steps.py
│
├── test_data/
│   └── user.json
│
├── utilities/
│   ├── api_health.py
│   ├── common_utils.py
│   ├── config_reader.py
│   ├── failure_analyzer.py
│   ├── logger.py
│   ├── response_validator.py
│   └── test_data_reader.py
│
├── smoke_test.py
├── test_api_health.py
├── test_auth.py
├── test_data_reader_test.py
├── test_failure_analyzer.py
├── test_validator.py
├── requirements.txt
└── README.md
 ```

## 7. Authentication Testing

The authentication module validates both successful and unsuccessful
login scenarios.

### Scenarios Covered

1. Successful login and access-token validation.
2. Invalid login and login-error validation.

The API response is validated to ensure that the expected authentication
information or error message is returned.

## 8. User Management Testing

The User Management feature contains BDD scenarios for the following
operations:

- Retrieve all users.
- Retrieve a user by ID.
- Create a new user.
- Update an existing user.
- Delete a user.
- Handle a non-existent user.

Each scenario validates the API response status and the relevant
response data.

## 9. Response Validation

A reusable `ResponseValidator` utility is implemented to validate API
responses.

The framework validates:

- HTTP status codes.
- Required response fields.
- Response field data types.
- Expected response structure.

This reduces duplicate validation logic and improves the maintainability
and reliability of the automation framework.

## 10. Failure Analysis

The framework includes a reusable `FailureAnalyzer` utility to classify
API responses based on their HTTP status codes.

| Status Code | Category | Severity |
|---|---|---|
| 200 | SUCCESS | NONE |
| 400 | CLIENT_ERROR - BAD_REQUEST | MEDIUM |
| 401 | AUTHENTICATION_ERROR - UNAUTHORIZED | HIGH |
| 403 | AUTHORIZATION_ERROR - FORBIDDEN | HIGH |
| 404 | RESOURCE_ERROR - NOT_FOUND | MEDIUM |
| 500 | SERVER_ERROR | CRITICAL |

The analyzer also provides a recommendation for investigating the
identified failure.

## 11. Logging

The framework uses Python's `logging` module to record API execution
details.

The logs capture:

- HTTP method.
- API endpoint.
- HTTP status code.
- API execution information.

Example:

```text
GET https://dummyjson.com/users -> Status: 200
GET https://dummyjson.com/users/1 -> Status: 200
POST https://dummyjson.com/users/add -> Status: 201
PUT https://dummyjson.com/users/1 -> Status: 200
DELETE https://dummyjson.com/users/1 -> Status: 200
GET https://dummyjson.com/users/9999 -> Status: 404

## 12. BDD Implementation

Behave is used to implement Behavior-Driven Development (BDD) for the
API automation framework.

The test scenarios are written in Gherkin syntax inside `.feature`
files and are connected to Python step definitions.

Example:

```gherkin
Feature: User Management

Scenario: Get all users successfully
    Given I send a GET request to the users endpoint
    And the response should contain users

## 13. Allure Reporting

Allure is integrated with the Behave test automation framework to
generate detailed and interactive test execution reports.

The Allure report provides information about:

- Test scenarios executed.
- Passed and failed scenarios.
- Execution status.
- Test duration.
- Feature and scenario details.

The Allure report was generated successfully after executing the
automated test suite.

## 14. Test Execution

The complete Behave test suite was executed successfully.

The final execution produced the following results:

```text
2 features passed, 0 failed, 0 skipped
8 scenarios passed, 0 failed, 0 skipped
29 steps passed, 0 failed, 0 skipped

## 15. Test Execution Evidence

### 15.1 Behave Test Execution

The complete Behave test suite was executed successfully with all
implemented scenarios passing.


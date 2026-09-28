# Module 3: Python BDD RESTful Automations

## Module Overview

This module introduces Python-based REST API automation and Behaviour Driven
Development (BDD) using the Behave framework.

The module covers REST and SOAP concepts, Python HTTP libraries, API requests
and responses, authentication, sessions, cookies, database integration,
BDD concepts, Gherkin syntax, step definitions, hooks, parameterization,
tagging and test reporting.

The objective of this module is to develop automated API test scenarios using
Python and the Behave BDD framework.

---

# Part 1: Python Basics for REST Automation

## Experiment 1: REST vs SOAP

### Experiment Name

Understanding REST and SOAP Web Services

### Objective

To understand the basic concepts of REST and SOAP web services and identify
their differences.

### Purpose

The purpose of this experiment is to understand the two commonly used
approaches for communication between applications and web services.

### Concept / Theory

REST stands for Representational State Transfer.

REST is an architectural style commonly used for building web services.
REST APIs generally communicate using HTTP methods and commonly exchange data
in formats such as JSON.

SOAP stands for Simple Object Access Protocol.

SOAP is a protocol used for exchanging structured information between
applications and commonly uses XML-based messages.

### REST

Important characteristics of REST include:

- Uses HTTP methods
- Commonly uses JSON
- Stateless communication
- Lightweight communication
- Resource-based architecture

### SOAP

Important characteristics of SOAP include:

- Uses XML-based messages
- Formal messaging structure
- Supports various communication standards
- Uses a defined service contract

### Procedure

1. Study the basic architecture of REST.
2. Study the basic architecture of SOAP.
3. Identify the communication methods used by both.
4. Compare their message formats.
5. Identify their common use cases.

### Result

The basic concepts and differences between REST and SOAP web services were
successfully understood.

<img width="1920" height="842" alt="module3_exp1_output" src="https://github.com/user-attachments/assets/3ee32f30-f842-4c23-b406-0f5b3a62cbb4" />


---

# Experiment 2: Python Requests Library

## Experiment Name

Introduction to Python Requests Library

### Objective

To understand and use the Python Requests library for communicating with
REST APIs.

### Purpose

The purpose of this experiment is to send HTTP requests from Python and
process the responses returned by an API.

### Concept / Theory

The Python Requests library provides a simple interface for sending HTTP
requests.

It supports common HTTP methods such as:

- GET
- POST
- PUT
- PATCH
- DELETE

A response object returned by the Requests library contains information such
as:

- Status code
- Response headers
- Response content
- JSON data

### Procedure

1. Install the Requests library.
2. Import the Requests module.
3. Specify the API endpoint.
4. Send the required HTTP request.
5. Receive the response.
6. Read the response information.
7. Verify the result.

### Result

The Python Requests library was successfully used to communicate with a
REST API.

---

# Part 2: Python HTTP Libraries

## Experiment 3: GET Request and JSON Response

### Experiment Name

Sending GET Requests and Reading JSON Responses

### Objective

To send a GET request to a REST API and retrieve data in JSON format.

### Purpose

The purpose of this experiment is to understand how data can be retrieved
from an API using a GET request.

### Concept / Theory

The HTTP GET method is used to retrieve information from a server.

A REST API may return the response in JSON format.

The JSON response can be converted into Python data structures and processed
using Python code.

### Procedure

1. Identify the API endpoint.
2. Send a GET request using the Requests library.
3. Receive the response.
4. Verify the HTTP status code.
5. Convert the response into JSON.
6. Extract the required information.
7. Display or validate the retrieved data.

### Output

The API response obtained after successful execution is shown below.

### Result

A GET request was successfully sent and the JSON response was retrieved and
processed using Python.

<img width="1920" height="842" alt="module3_exp3_output" src="https://github.com/user-attachments/assets/8b16b28d-28e9-438d-b2b5-960ca614376a" />


---

## Experiment 4: Basic Features of Requests

### Experiment Name

Working with Request and Response Objects

### Objective

To understand the basic properties and methods of the Requests library.

### Purpose

The purpose of this experiment is to access and process information returned
by an HTTP response.

### Concept / Theory

A response object provides access to information returned by the server.

Important response attributes include:

- `status_code`
- `headers`
- `text`
- `content`
- `json()`

These properties can be used to validate and process API responses.

### Procedure

1. Send an HTTP request.
2. Store the response object.
3. Read the status code.
4. Read the response headers.
5. Read the response body.
6. Convert JSON response data when required.
7. Validate the obtained information.

### Result

The important properties and methods of the Requests response object were
successfully explored.

---

## Experiment 5: Installation and Quick Start

### Experiment Name

Requests Library Installation and API Quick Start

### Objective

To configure the Python environment for API automation and execute a basic
API request.

### Purpose

The purpose of this experiment is to prepare the environment required for
Python REST API automation.

### Procedure

1. Verify Python installation.
2. Install the Requests package.
3. Import the Requests library.
4. Create a basic API request.
5. Execute the Python script.
6. Verify the returned response.

### Result

The Python environment was successfully configured for REST API automation.

---

## Experiment 6: Validating Status Codes and Headers

### Experiment Name

Validation of HTTP Status Codes and Response Headers

### Objective

To validate HTTP response status codes and headers using the Python
Requests response object.

### Purpose

The purpose of this experiment is to verify whether an API request was
processed successfully and whether the returned response contains the
expected information.

### Concept / Theory

HTTP status codes indicate the result of an HTTP request.

Common categories include:

- 2xx - Successful requests
- 3xx - Redirection
- 4xx - Client errors
- 5xx - Server errors

Response headers provide additional information about the response.

### Procedure

1. Send the API request.
2. Store the response.
3. Retrieve the status code.
4. Retrieve the required response headers.
5. Compare the actual values with expected values.
6. Report the validation result.

### Result

The API status code and response headers were successfully validated.

---

## Experiment 7: POST Request with Payload and Headers

### Experiment Name

Automating POST Requests with Payload and Headers

### Objective

To send POST requests containing request payloads and headers.

### Purpose

The purpose of this experiment is to understand how new data can be submitted
to a REST API.

### Concept / Theory

The HTTP POST method is commonly used to submit data to a server.

A POST request may contain:

- Request URL
- Headers
- Payload/body

JSON is commonly used as the payload format in REST APIs.

### Procedure

1. Identify the POST API endpoint.
2. Prepare the request payload.
3. Define the required headers.
4. Send the POST request.
5. Receive the response.
6. Validate the response status.
7. Validate the returned response data.

### Output

The POST request execution output is shown below.



### Result

A POST request was successfully automated using Python and the Requests
library.

---

## Experiment 8: End-to-End API Automation Flow

### Experiment Name

End-to-End API Automation Using Python

### Objective

To automate a complete API workflow using Python.

### Purpose

The purpose of this experiment is to combine multiple API operations into a
single automation flow.

### Concept / Theory

An end-to-end API automation flow may involve:

1. Sending a request.
2. Validating the response.
3. Extracting required data.
4. Passing extracted data to another request.
5. Validating the final response.

### Procedure

1. Configure the API endpoint.
2. Send the first API request.
3. Validate the response.
4. Extract required information.
5. Use the extracted information in the next request.
6. Continue the API workflow.
7. Validate the final response.

### Result

An end-to-end API automation flow was successfully implemented using Python.

---

# Part 3: API Automation

## Experiment 9: Global Configuration Using Python

### Experiment Name

Managing Global API Configuration

### Objective

To manage reusable API configuration information using Python.

### Purpose

The purpose of this experiment is to avoid repeatedly defining common
configuration values in different parts of the automation framework.

### Concept / Theory

Global configuration can contain reusable information such as:

- Base URL
- API endpoints
- Authentication information
- Environment settings
- Request configuration

Centralizing configuration improves maintainability and reusability.

### Procedure

1. Identify common configuration values.
2. Create a configuration object or module.
3. Store reusable configuration information.
4. Import the configuration where required.
5. Use the configuration values in API requests.
6. Execute and validate the automation.

### Result

Reusable API configuration was successfully implemented using Python.

---

## Experiment 10: External Test Data

### Experiment Name

Using External Data in API Automation

### Objective

To use external data as input for API automation.

### Purpose

The purpose of this experiment is to separate test data from automation
logic and improve test reusability.

### Concept / Theory

Test data can be maintained externally in formats such as:

- JSON
- CSV
- Properties files
- Excel

External data can then be read by the Python automation script and used as
request parameters or payload values.

### Procedure

1. Create the external data file.
2. Store the required API test data.
3. Read the data using Python.
4. Pass the retrieved values to the API request.
5. Execute the request.
6. Validate the response.

### Result

External test data was successfully integrated with Python API automation.

---

## Experiment 11: API Authentication

### Experiment Name

Authenticating APIs Using Python

### Objective

To understand and implement API authentication using Python automation.

### Purpose

The purpose of this experiment is to securely access APIs that require
authentication.

### Concept / Theory

APIs may require authentication before allowing access to protected
resources.

Authentication information may be provided through:

- Headers
- Tokens
- API keys
- Authentication parameters

The authentication mechanism depends on the API being tested.

### Procedure

1. Identify the authentication mechanism required by the API.
2. Prepare the authentication information.
3. Add the required authentication information to the request.
4. Send the request.
5. Validate the authentication response.
6. Access the protected API resource.

### Result

API authentication was successfully implemented and validated using Python.

---

## Experiment 12: Session Management

### Experiment Name

Managing API Sessions Using Python

### Objective

To understand and manage sessions during API automation.

### Purpose

The purpose of this experiment is to maintain session-related information
across multiple API requests.

### Concept / Theory

A session can be used to persist certain parameters across multiple requests.

Session management can help maintain:

- Cookies
- Headers
- Connection information
- Authentication state

### Procedure

1. Create a session.
2. Configure the required session information.
3. Send the required API request.
4. Maintain the session for subsequent requests.
5. Validate the response.
6. Close or terminate the session when required.

### Result

API session management was successfully implemented using Python.

---

## Experiment 13: Cookies in API Requests

### Experiment Name

Sending and Managing Cookies

### Objective

To understand how cookies are handled during API automation.

### Purpose

The purpose of this experiment is to send, receive and manage cookies
associated with API requests.

### Concept / Theory

Cookies are pieces of information stored and exchanged between a client and
server.

They may be used for:

- Session management
- Authentication
- User preferences
- Tracking session state

### Procedure

1. Send an API request.
2. Inspect the returned cookies.
3. Store or retrieve the required cookie.
4. Send the cookie with another request when required.
5. Validate the response.

### Result

Cookies were successfully handled during API automation.

---

## Experiment 14: Database Integration with Python

### Experiment Name

Connecting Python Automation with MySQL

### Objective

To connect Python automation with a MySQL database and retrieve test data.

### Purpose

The purpose of this experiment is to use database information as a source
for API automation.

### Concept / Theory

Database integration allows automated tests to retrieve or validate data
directly from a database.

A typical database automation flow includes:

1. Establishing a connection.
2. Selecting the database.
3. Executing a query.
4. Retrieving the result.
5. Using the result in automation.
6. Closing the connection.

### Procedure

1. Configure the MySQL database.
2. Create the required table and test data.
3. Establish a database connection from Python.
4. Execute the required query.
5. Retrieve the result.
6. Use the retrieved data in automation.
7. Close the database connection.

### Result

Python was successfully connected to the MySQL database and database data
was used for automation.

---

## Experiment 15: PUT and PATCH Requests

### Experiment Name

Updating API Data Using PUT and PATCH

### Objective

To understand and automate PUT and PATCH HTTP requests.

### Purpose

The purpose of this experiment is to update existing resources through REST
API automation.

### Concept / Theory

The PUT method is generally used to update or replace a resource.

The PATCH method is generally used to perform a partial update of a resource.

### Procedure

1. Identify the resource to be updated.
2. Prepare the required request payload.
3. Send the PUT or PATCH request.
4. Validate the response status code.
5. Verify the updated information.

### Result

API resources were successfully updated using PUT and PATCH requests.

---

## Experiment 16: DELETE Request

### Experiment Name

Deleting Data Using REST API

### Objective

To automate DELETE requests and verify the deletion response.

### Purpose

The purpose of this experiment is to understand how resources can be removed
through REST APIs.

### Procedure

1. Identify the resource to be deleted.
2. Construct the DELETE endpoint.
3. Send the DELETE request.
4. Validate the response status.
5. Verify that the resource has been deleted.

### Result

The DELETE operation was successfully automated and validated.

---

# Part 4: Handling HTTP Responses

## Experiment 17: Understanding Response Objects

### Experiment Name

Working with HTTP Response Objects

### Objective

To understand and process HTTP response objects returned by APIs.

### Purpose

The purpose of this experiment is to extract useful information from API
responses.

### Concept / Theory

An HTTP response contains information returned by the server after processing
a request.

Important response information includes:

- Status code
- Headers
- Body
- JSON content
- Cookies

### Procedure

1. Send an HTTP request.
2. Store the response object.
3. Read the status code.
4. Read the response headers.
5. Read the response body.
6. Process JSON data when required.
7. Validate the response.

### Result

HTTP response objects were successfully processed using Python.

---

## Experiment 18: Reading Response Content

### Experiment Name

Reading API Response Content

### Objective

To retrieve and process text and JSON content returned by an API.

### Purpose

The purpose of this experiment is to extract required information from
API responses for validation.

### Procedure

1. Send the API request.
2. Receive the response.
3. Read the response content.
4. Convert JSON data when required.
5. Extract the required fields.
6. Validate the extracted information.

### Result

API response content was successfully read and processed.

---

## Experiment 19: Handling Binary and Text Data

### Experiment Name

Handling Binary and Text HTTP Responses

### Objective

To understand how Python handles text and binary response data.

### Purpose

The purpose of this experiment is to correctly process different types of
data returned by an HTTP service.

### Concept / Theory

HTTP responses may contain:

- Text data
- JSON data
- Binary data

Text data can be processed as strings, while binary content can be accessed
as bytes.

### Procedure

1. Send the required request.
2. Identify the response content type.
3. Read text data using the appropriate response property.
4. Read binary data using the appropriate response property.
5. Process or save the content as required.

### Result

Text and binary HTTP response data were successfully handled using Python.

---

## Experiment 20: Status Codes and Error Handling

### Experiment Name

HTTP Status Code Validation and Error Handling

### Objective

To validate successful and unsuccessful API responses and handle errors.

### Purpose

The purpose of this experiment is to make API automation reliable by
identifying and handling unexpected responses.

### Procedure

1. Send the API request.
2. Read the response status code.
3. Determine whether the request was successful.
4. Handle error responses appropriately.
5. Record or report the result.
6. Continue or terminate execution according to the test requirement.

### Result

HTTP status codes and API errors were successfully handled during automation.

---

## Experiment 21: Exception Handling in API Automation

### Experiment Name

Exception Handling Using Python Requests

### Objective

To handle runtime exceptions occurring during API automation.

### Purpose

The purpose of this experiment is to prevent unexpected runtime errors from
terminating automation without useful information.

### Concept / Theory

Python exception handling can be implemented using:

- `try`
- `except`
- `finally`

Exception handling can be used for network errors, invalid requests,
connection errors and other runtime conditions.

### Procedure

1. Identify operations that may generate exceptions.
2. Place the operation inside a `try` block.
3. Handle expected exceptions using `except`.
4. Perform cleanup using `finally` where required.
5. Execute the automation.
6. Verify the handled result.

### Result

Exceptions were successfully handled during Python API automation.

---

# Part 5: Behaviour Driven Development (BDD)

## Experiment 22: Introduction to BDD

### Experiment Name

Introduction to Behaviour Driven Development

### Objective

To understand the concept of Behaviour Driven Development and its use in
test automation.

### Purpose

The purpose of this experiment is to understand how application behaviour
can be described using scenarios that are understandable by both technical
and non-technical stakeholders.

### Concept / Theory

Behaviour Driven Development is an approach in which software behaviour is
described using examples and scenarios.

BDD commonly uses the Gherkin language with keywords such as:

- Feature
- Scenario
- Given
- When
- Then
- And
- But

The Behave framework can execute these scenarios in Python.

### Result

The basic concepts of BDD and its role in Python automation were successfully
understood.

---

## Experiment 23: Setting Up Python Behave

### Experiment Name

Python and Behave BDD Framework Setup

### Objective

To configure the Python environment for BDD automation using Behave.

### Purpose

The purpose of this experiment is to prepare the environment required for
executing BDD scenarios using Python.

### Procedure

1. Verify Python installation.
2. Install Behave.
3. Create the project structure.
4. Create the `features` directory.
5. Create a feature file.
6. Create the required step definition file.
7. Execute the Behave test.
8. Verify the result.

### Typical Project Structure

```text
project/
│
├── features/
│   ├── example.feature
│   │
│   └── steps/
│       └── example_steps.py
│
└── environment.py

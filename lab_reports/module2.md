# Module 2: Unit Test Frameworks

## Module Overview

This module focuses on Python unit testing and test automation frameworks used
to organize, execute and report automated tests.

The module covers Python's built-in `unittest` framework, the `PyTest`
framework and the Page Object Model (POM) design pattern.

The objective of this module is to develop structured, maintainable and
reusable automated test cases using appropriate testing frameworks and design
patterns.

---

# Part 1: Unittest Framework

## Experiment 1: Introduction to Unittest

### Experiment Name

Introduction to Python Unittest Framework

### Objective

To understand the Python `unittest` framework and its role in creating and
executing automated test cases.

### Purpose

The purpose of this experiment is to learn the basic structure of a unit test
using Python's built-in `unittest` framework.

### Concept / Theory

`unittest` is a built-in Python testing framework inspired by the xUnit family
of testing frameworks.

It provides features for:

- Creating test cases
- Running test methods
- Performing assertions
- Setting up test environments
- Cleaning up test environments
- Grouping multiple tests into test suites

A test case is generally created by inheriting from `unittest.TestCase`.

### Procedure

1. Import the `unittest` module.
2. Create a test class by inheriting from `unittest.TestCase`.
3. Define a test method.
4. Write the required test logic.
5. Use assertion methods to verify the expected result.
6. Execute the test case.
7. Observe the test result.

### Implementation

The test case was implemented using Python's `unittest` framework.

### Output

The output obtained after successful execution is shown below.

<img width="1920" height="842" alt="module2_exp2_user1_output" src="https://github.com/user-attachments/assets/b57fb9ad-5a5d-4699-95dd-0ba05308f9a9" />


### Result

The basic structure and execution of a Python `unittest` test case were
successfully understood.

---

# Experiment 2: Creating the First Test Case

## Experiment Name

Creating and Executing the First Unittest Test Case

### Objective

To create and execute a basic test case using Python's `unittest`
framework.

### Purpose

The purpose of this experiment is to understand the structure of a test class,
test method and test execution process.

### Concept / Theory

A test case represents an individual unit of testing.

In the `unittest` framework, test methods generally begin with the word
`test`. The framework automatically identifies these methods as test cases
during test execution.

A typical unittest structure contains:

- Test class
- Test methods
- Test assertions
- Test execution

### Procedure

1. Import the `unittest` module.
2. Create a class derived from `unittest.TestCase`.
3. Define a test method beginning with `test`.
4. Write the required test logic.
5. Add an appropriate assertion.
6. Execute the test.
7. Verify whether the test passes or fails.

### Result

The first automated test case was successfully created and executed using the
`unittest` framework.

---

# Experiment 3: Class-Level Setup and Teardown

## Experiment Name

Implementing Setup and Teardown Methods

### Objective

To understand and implement setup and teardown operations in a unittest
test class.

### Purpose

The purpose of setup and teardown methods is to prepare the testing
environment before test execution and perform cleanup operations after test
execution.

### Concept / Theory

The `unittest` framework provides lifecycle methods that can be used for
pre-test and post-test operations.

The commonly used methods include:

- `setUp()`
- `tearDown()`

`setUp()` is executed before each test method, while `tearDown()` is executed
after each test method.

These methods are useful for operations such as:

- Opening a browser
- Creating test data
- Initializing objects
- Closing the browser
- Cleaning test data

### Procedure

1. Create a unittest test class.
2. Implement the `setUp()` method.
3. Add the required initialization logic.
4. Implement the test method.
5. Implement the `tearDown()` method.
6. Add cleanup operations.
7. Execute the test case.
8. Verify the execution sequence.

### Result

Setup and teardown operations were successfully implemented for the unittest
test case.

---

# Experiment 4: Assertions in Unittest

## Experiment Name

Implementing Assertions in Test Cases

### Objective

To verify expected and actual results using unittest assertion methods.

### Purpose

The purpose of assertions is to determine whether the actual result of a test
matches the expected result.

### Concept / Theory

Assertions are used to validate conditions during test execution.

Common unittest assertion methods include:

- `assertEqual()`
- `assertNotEqual()`
- `assertTrue()`
- `assertFalse()`
- `assertIsNone()`
- `assertIsNotNone()`
- `assertIn()`
- `assertNotIn()`

When an assertion succeeds, the corresponding test continues successfully.
When an assertion fails, the test is reported as failed.

### Procedure

1. Create a test case.
2. Define the expected result.
3. Obtain the actual result.
4. Apply the appropriate assertion.
5. Execute the test.
6. Verify the test result.

### Result

Assertions were successfully implemented to validate test results.

<img width="1920" height="842" alt="module2_exp4_csvuser1" src="https://github.com/user-attachments/assets/71abfc39-45b2-45a5-8ea2-b611ec29fd63" />


---

# Experiment 5: Creating a Test Suite

## Experiment Name

Creating and Executing a Test Suite

### Objective

To group multiple test cases into a test suite and execute them together.

### Purpose

The purpose of a test suite is to organize multiple related test cases and
execute them as a single group.

### Concept / Theory

A test suite is a collection of test cases that can be executed together.

Test suites are useful when a project contains multiple related tests and the
tester wants to control their execution as a group.

### Procedure

1. Create multiple test cases.
2. Create a test suite.
3. Add the required test cases to the suite.
4. Execute the suite.
5. Observe the execution results.
6. Verify the status of each test.

### Result

Multiple test cases were successfully grouped and executed using a unittest
test suite.

---

# Part 2: PyTest Framework

## Experiment 6: Introduction to PyTest

### Experiment Name

Introduction to PyTest Framework

### Objective

To understand the PyTest framework and its role in Python test automation.

### Purpose

The purpose of this experiment is to understand the basic features and
advantages of PyTest for writing and executing automated tests.

### Concept / Theory

PyTest is a Python testing framework that supports simple unit tests as well
as complex functional testing.

It provides features such as:

- Simple test syntax
- Test discovery
- Assertions
- Fixtures
- Parameterization
- Test selection
- Plugins
- Reporting
- Parallel test execution

### Procedure

1. Install PyTest.
2. Create a Python test file.
3. Create a test function or test class.
4. Write the test logic.
5. Execute the test using PyTest.
6. Observe the test result.

### Result

The basic concepts and execution process of the PyTest framework were
successfully understood.

---

# Experiment 7: Installing PyTest and Naming Conventions

## Experiment Name

PyTest Installation and Test Discovery

### Objective

To install PyTest and understand its test discovery and naming conventions.

### Purpose

The purpose of this experiment is to understand how PyTest identifies test
files and test functions automatically.

### Concept / Theory

PyTest follows naming conventions for discovering test cases.

Common conventions include:

- Test files beginning with `test_`
- Test files ending with `_test.py`
- Test functions beginning with `test_`
- Test classes beginning with `Test`

Following these conventions allows PyTest to automatically discover test cases.

### Procedure

1. Install PyTest.
2. Create a test file following the PyTest naming convention.
3. Create a test function.
4. Execute PyTest from the terminal.
5. Observe the discovered test cases.
6. Verify the execution result.

### Result

PyTest was successfully installed and its test discovery mechanism was
understood.

---

# Experiment 8: Test Methods and Assertions in PyTest

## Experiment Name

Creating Test Methods and Assertions Using PyTest

### Objective

To create PyTest test methods and verify results using assertions.

### Purpose

The purpose of this experiment is to understand how test cases and assertions
are implemented using PyTest.

### Concept / Theory

PyTest allows assertions to be written directly using Python's `assert`
statement.

For example, an expected condition can be compared with the actual result
using a simple assertion.

This makes PyTest test cases concise and readable.

### Procedure

1. Create a PyTest test file.
2. Define a test function.
3. Implement the required test logic.
4. Use the Python `assert` statement.
5. Execute the test using PyTest.
6. Verify the test result.

### Result

Test methods and assertions were successfully implemented using PyTest.

---

# Experiment 9: Test Suites and Subsets

## Experiment Name

Running Test Suites and Selected Test Cases

### Objective

To execute multiple test cases together and selectively execute required
tests using PyTest.

### Purpose

The purpose of this experiment is to understand how test execution can be
controlled when a project contains multiple test cases.

### Concept / Theory

PyTest allows testers to execute:

- Individual test files
- Individual test functions
- Multiple test files
- Groups or subsets of tests

This provides flexibility when executing large automation suites.

### Procedure

1. Create multiple test cases.
2. Organize the tests into appropriate files.
3. Execute the complete test suite.
4. Execute selected test cases when required.
5. Observe the execution results.

### Result

Multiple test cases and selected subsets were successfully executed using
PyTest.

---

# Experiment 10: Fixtures and conftest.py

## Experiment Name

Using PyTest Fixtures and conftest.py

### Objective

To understand and implement PyTest fixtures and shared configuration using
`conftest.py`.

### Purpose

The purpose of fixtures is to provide reusable setup and teardown operations
for test cases.

### Concept / Theory

A PyTest fixture provides a fixed baseline or preparation required by one or
more tests.

Fixtures can be used for:

- Browser initialization
- Test data setup
- Database connections
- Authentication
- Cleanup operations

The `conftest.py` file is used to define fixtures and configuration that can
be shared across multiple test files.

### Procedure

1. Create a PyTest test file.
2. Create a fixture.
3. Place reusable fixture configuration in `conftest.py` when required.
4. Use the fixture in the test case.
5. Execute the test.
6. Verify that the setup and cleanup operations are performed correctly.

### Result

PyTest fixtures and shared configuration using `conftest.py` were successfully
implemented.

---

# Experiment 11: PyTest Features and Multiple Test Cases

## Experiment Name

Executing Multiple Test Cases Using PyTest

### Objective

To organize and execute multiple test cases using PyTest.

### Purpose

The purpose of this experiment is to understand how PyTest can be used to
manage multiple automated test cases efficiently.

### Concept / Theory

PyTest provides several features that simplify test automation, including
automatic test discovery, fixtures, assertions, test selection and plugin
support.

Multiple test cases can be maintained in separate files and executed together
as part of a test suite.

### Procedure

1. Create multiple test cases.
2. Organize the test files.
3. Configure any required fixtures.
4. Execute the tests using PyTest.
5. Observe the execution summary.
6. Verify the result of each test case.

### Result

Multiple automated test cases were successfully organized and executed using
PyTest.

---

# Experiment 12: Moving Selenium Tests to PyTest

## Experiment Name

Integrating Selenium Automation with PyTest

### Objective

To convert an existing Selenium automation test into a PyTest-based test.

### Purpose

The purpose of this experiment is to combine Selenium WebDriver automation
with the PyTest testing framework.

### Concept / Theory

Selenium provides browser automation capabilities, while PyTest provides
test organization, execution and reporting capabilities.

Combining both allows browser automation scripts to be managed as structured
automated test cases.

PyTest fixtures can be used to initialize and close the Selenium WebDriver.

### Procedure

1. Select an existing Selenium automation test.
2. Create a PyTest test file.
3. Move the Selenium test logic into a PyTest test function or class.
4. Configure the WebDriver using a fixture where required.
5. Execute the test using PyTest.
6. Verify the browser automation result.
7. Verify the PyTest execution result.

### Result

The Selenium automation test was successfully integrated with PyTest.

---

# Experiment 13: Generating HTML Reports Using PyTest

## Experiment Name

PyTest HTML Reporting

### Objective

To generate an HTML test execution report using PyTest.

### Purpose

The purpose of HTML reporting is to provide a readable summary of automated
test execution, including test status and execution details.

### Concept / Theory

PyTest supports plugins that can generate HTML reports from test execution.

An HTML report can provide information such as:

- Test cases executed
- Passed tests
- Failed tests
- Execution status
- Test duration
- Test details

### Procedure

1. Install the required PyTest HTML reporting plugin.
2. Execute the test suite.
3. Configure the HTML report output.
4. Generate the report.
5. Open the generated HTML report.
6. Verify the execution details.

### Result

An HTML test execution report was successfully generated using PyTest.

---

# Part 3: Page Object Model

## Experiment 14: Introduction to Page Object Model

### Experiment Name

Understanding the Page Object Model Design Pattern

### Objective

To understand the Page Object Model design pattern and its importance in
test automation.

### Purpose

The purpose of the Page Object Model is to improve the maintainability,
reusability and readability of Selenium automation frameworks.

### Concept / Theory

Page Object Model (POM) is a design pattern commonly used in Selenium test
automation.

In POM, each webpage or major component of an application is represented by a
separate class.

A page class generally contains:

- Web element locators
- Page-specific methods
- Actions that can be performed on the page

The test class contains the actual test flow and assertions.

This separation reduces duplication and makes automation scripts easier to
maintain.

### Typical Architecture

```text
Project
│
├── pages/
│   ├── LoginPage
│   └── DashboardPage
│
├── tests/
│   └── test_login
│
├── utilities/
│
├── configuration/
│
└── test data/


# Python Selenium Automation - Lab Reports

# Module 1: Automation with Selenium

## Module Overview

This module introduces web automation using Selenium with Python. It covers
Selenium WebDriver, browser automation, element identification, web controls,
advanced browser interactions, dynamic web elements, synchronization, exception
handling, screenshots, external test data and advanced Selenium interactions.

The objective of this module is to develop practical skills required to design,
execute and maintain automated web test scripts using Python and Selenium WebDriver.

---

# Experiment 1: Introduction to Selenium and Selenium WebDriver

## Experiment Name

Introduction to Selenium and Selenium WebDriver

## Objective

To understand Selenium and its different components and to learn how Selenium
WebDriver can be used to automate web browsers using Python.

## Purpose

The purpose of this experiment is to understand the fundamentals of web
automation and the role of Selenium WebDriver in automating browser-based
applications.

## Concept / Theory

Selenium is an open-source framework used for automating web applications.

The major components of Selenium include:

- Selenium IDE
- Selenium WebDriver
- Selenium Grid

Selenium WebDriver provides an interface for communicating with web browsers
and performing automated actions such as opening a website, clicking buttons,
entering text and retrieving information from web pages.

Python can be used with Selenium WebDriver to create automated test scripts.

## Tools and Technologies

- Python
- Selenium
- Selenium WebDriver
- Web Browser
- VS Code / PyCharm

## Procedure

1. Install Python.
2. Install the Selenium package.
3. Configure the required web browser.
4. Import Selenium WebDriver in the Python program.
5. Create a WebDriver instance.
6. Launch the required browser.
7. Navigate to the required web page.
8. Perform the required browser actions.
9. Close the browser after execution.

## Implementation

The experiment was implemented using Python and Selenium WebDriver to automate
basic browser operations.

## Code

The Python implementation used for this experiment is maintained with the
corresponding practical work.

<img width="1149" height="564" alt="Screenshot (35)" src="https://github.com/user-attachments/assets/5352e0b0-8928-4f6e-af15-2bf11a47ca85" />


## Output

The output obtained after successful execution is shown in the corresponding
output screenshot.
<img width="1920" height="1080" alt="Screenshot (34)" src="https://github.com/user-attachments/assets/609d7ade-4428-4106-ab70-b7446e9f6d91" />



## Result

The basic concepts of Selenium and Selenium WebDriver were successfully
understood and browser automation was performed using Python.

---

# Experiment 2: Selenium WebDriver Installation and Browser Configuration

## Experiment Name

Installation and Configuration of Selenium WebDriver with Python

## Objective

To install Selenium WebDriver with Python and configure the environment for
browser automation.

## Purpose

The purpose of this experiment is to prepare the Python environment required
for executing Selenium automation scripts.

## Concept / Theory

Selenium WebDriver requires a programming language binding and a compatible
browser driver or browser-driver management mechanism to communicate with the
browser.

The Python Selenium package provides the required WebDriver APIs for creating
and controlling browser instances.

## Procedure

1. Verify that Python is installed.
2. Install Selenium using the Python package manager.
3. Configure the required browser.
4. Configure the browser driver if required.
5. Import the Selenium WebDriver module.
6. Create a browser driver object.
7. Execute a basic browser automation script.
8. Verify that the browser launches successfully.

## Implementation

The Selenium environment was configured using Python and the required browser
automation components.

## Output

The successful browser launch and execution of the Selenium script were
verified through the generated output.

## Result

The Selenium WebDriver environment was successfully configured and verified.

---

# Experiment 3: Working with Selenium Locators

## Experiment Name

Identification of Web Elements Using Selenium Locators

## Objective

To identify web elements using different Selenium locator strategies.

## Purpose

The purpose of this experiment is to understand how Selenium identifies elements
on a web page so that automated actions can be performed on them.

## Concept / Theory

A locator is a mechanism used by Selenium to identify a particular web element
on a webpage.

Common Selenium locator strategies include:

- ID
- Name
- Class Name
- Tag Name
- Link Text
- Partial Link Text
- CSS Selector
- XPath

Choosing an appropriate locator is important because reliable element
identification is essential for stable automation scripts.

## Procedure

1. Open the required webpage.
2. Inspect the HTML structure of the webpage.
3. Identify the required web element.
4. Select an appropriate locator strategy.
5. Locate the element using Selenium.
6. Perform the required action.
7. Verify the result.

## Implementation

Different locator strategies were used to identify and interact with web
elements.

<img width="1234" height="645" alt="Screenshot 2026-09-24 151944" src="https://github.com/user-attachments/assets/1faf6cab-8f8d-4a27-b7ca-411bddf4a260" />


## Result

The required web elements were successfully identified and interacted with
using Selenium locator strategies.

<img width="1920" height="842" alt="module1_exp3_output" src="https://github.com/user-attachments/assets/77e7bf2b-75e0-456c-b8e5-165fc48d7dd7" />
---

# Experiment 4: Working with XPath and CSS Selectors

## Experiment Name

Element Identification Using XPath and CSS Selectors

## Objective

To locate web elements using XPath and CSS Selector expressions.

## Purpose

The purpose of this experiment is to learn how to identify elements when simple
locators such as ID or Name are not sufficient.

## Concept / Theory

XPath is a query language used to navigate through elements in an HTML/XML
document.

Two commonly used XPath approaches are:

### Absolute XPath

Absolute XPath specifies the complete path from the root element to the
required element.

### Relative XPath

Relative XPath identifies an element based on its attributes or relationship
with other elements.

Common XPath functions and relationships include:

- `contains()`
- `starts-with()`
- Parent
- Child
- Following sibling
- Preceding sibling

CSS Selectors can also be used to identify elements based on:

- ID
- Class
- Attributes
- Child elements
- Descendant relationships
- Wildcards

## Procedure

1. Open the required webpage.
2. Inspect the HTML structure.
3. Identify the target element.
4. Create an XPath or CSS Selector.
5. Use the locator with Selenium.
6. Perform the required action.
7. Verify the output.

## Result

Web elements were successfully located using XPath and CSS Selector strategies.

---

# Experiment 5: Handling Basic Web Controls

## Experiment Name

Handling Buttons, Input Boxes, Checkboxes, Radio Buttons and Select Boxes

## Objective

To automate different types of web controls using Selenium WebDriver.

## Purpose

The purpose of this experiment is to understand how Selenium interacts with
common HTML controls found in web applications.

## Web Controls Covered

- Buttons
- Input/Text boxes
- Checkboxes
- Radio buttons
- Select boxes

## Concept / Theory

Selenium WebDriver provides methods that allow automated interaction with web
elements.

For example:

- Input fields can be populated with text.
- Buttons can be clicked.
- Checkboxes can be selected or deselected.
- Radio buttons can be selected.
- Select boxes can be handled using Selenium's Select functionality.

## Procedure

1. Launch the browser.
2. Navigate to the required webpage.
3. Locate the required control.
4. Perform the required action.
5. Verify the state or output of the control.
6. Close the browser.

## Result

Different web controls were successfully identified and automated using
Selenium WebDriver.

---

# Experiment 6: Handling Advanced Web Controls

## Experiment Name

Handling Alerts, Date Pickers, File Uploads, Multiple Windows and Iframes

## Objective

To automate advanced web controls and browser interactions using Selenium.

## Purpose

The purpose of this experiment is to learn how Selenium handles browser
features and web components that require switching between different contexts.

## Controls Covered

- JavaScript Alerts
- Confirmation dialogs
- Prompt dialogs
- Date Pickers
- File Upload
- Multiple Windows/Tabs
- Iframes

## Concept / Theory

Some web interactions require Selenium to change its current context.

For example:

- Alerts require switching to the alert.
- Iframes require switching into the frame before interacting with elements.
- Multiple windows require identifying the appropriate window handle.
- File upload controls can be handled by providing the required file path.

## Procedure

1. Launch the browser.
2. Navigate to the required webpage.
3. Identify the advanced control.
4. Switch to the required context when necessary.
5. Perform the required action.
6. Verify the result.
7. Return to the original browser context when required.
8. Close the browser.

## Result

Advanced web controls and browser contexts were successfully handled using
Selenium WebDriver.

---

# Experiment 7: Working with Web Tables

## Experiment Name

Handling and Traversing Dynamic Web Tables

## Objective

To identify, traverse and extract data from HTML web tables using Selenium.

## Purpose

The purpose of this experiment is to understand how structured tabular data
can be located and processed using Selenium WebDriver.

## Concept / Theory

Web tables contain information arranged into rows and columns.

Selenium can be used to:

- Locate a table.
- Identify rows.
- Identify columns/cells.
- Traverse through rows and columns.
- Search for specific data.
- Extract values from table cells.

## Procedure

1. Open the webpage containing the table.
2. Locate the table element.
3. Identify the rows and columns.
4. Traverse through the table.
5. Compare cell values with the required data.
6. Extract the required information.
7. Display or verify the result.

## Result

The web table was successfully located and its data was traversed and extracted
using Selenium.

---

# Experiment 8: Synchronization and Waits

## Experiment Name

Synchronization Using Implicit and Explicit Waits

## Objective

To understand synchronization problems in Selenium and implement appropriate
wait mechanisms.

## Purpose

The purpose of this experiment is to synchronize the automation script with
the loading and availability of web elements.

## Concept / Theory

Web applications may load elements dynamically. If Selenium tries to interact
with an element before it becomes available, the test may fail.

Synchronization mechanisms help Selenium wait for the required condition.

### Implicit Wait

An implicit wait tells WebDriver to wait for a specified amount of time when
searching for elements.

### Explicit Wait

An explicit wait waits for a specific condition to become true before
continuing execution.

Examples of expected conditions include:

- Element visibility
- Element presence
- Element to be clickable
- Element selection

## Procedure

1. Open the required webpage.
2. Identify the dynamically loaded element.
3. Observe the synchronization requirement.
4. Implement the appropriate wait mechanism.
5. Wait for the required condition.
6. Perform the required action.
7. Verify the output.

## Result

Synchronization techniques were successfully implemented to handle dynamically
loaded web elements.

---

# Experiment 9: Taking Screenshots in Selenium

## Experiment Name

Capturing Screenshots Using Selenium WebDriver

## Objective

To capture screenshots during Selenium test execution.

## Purpose

The purpose of this experiment is to capture the browser state during test
execution for debugging, verification and reporting purposes.

## Concept / Theory

Screenshots provide a visual record of the browser state at a particular point
during automation execution.

They are especially useful when:

- A test fails.
- A particular state needs to be verified.
- Evidence of test execution is required.
- Test reports require visual evidence.

## Procedure

1. Launch the browser.
2. Navigate to the required webpage.
3. Perform the required automation steps.
4. Invoke the Selenium screenshot functionality.
5. Save the screenshot.
6. Verify the generated image.

## Result

Screenshots were successfully captured during Selenium automation execution.

---

# Experiment 10: Exception Handling in Selenium

## Experiment Name

Exception Handling Using Try, Except and Finally

## Objective

To handle exceptions occurring during Selenium automation without terminating
the complete execution unexpectedly.

## Purpose

The purpose of this experiment is to make automation scripts more reliable
by handling possible runtime errors.

## Concept / Theory

Exceptions can occur during automation due to reasons such as:

- Element not being found
- Element not being clickable
- Timeout
- Invalid selector
- Browser or driver issues

Python provides exception-handling mechanisms using:

- `try`
- `except`
- `finally`

The `try` block contains the code that may produce an exception. The `except`
block handles the exception, while the `finally` block contains code that should
execute regardless of whether an exception occurs.

## Procedure

1. Identify a Selenium operation that may generate an exception.
2. Place the operation inside a `try` block.
3. Handle the expected exception using `except`.
4. Perform cleanup operations inside `finally`.
5. Execute the script.
6. Verify the result.

## Result

Exceptions were successfully handled using Python exception-handling
mechanisms.

---

# Experiment 11: Reading and Writing External Test Data

## Experiment Name

Data Handling Using Excel, JSON, CSV and XML

## Objective

To read and write test data using external data files.

## Purpose

The purpose of this experiment is to separate test data from automation logic
and make the test scripts reusable for multiple data sets.

## Data Sources

- Excel
- JSON
- CSV
- XML
- Properties/Configuration files

## Concept / Theory

Data-driven automation stores test data externally rather than hard-coding
values directly inside the test script.

External data sources make it possible to execute the same automation logic with
different sets of input data.

## Procedure

1. Create or use the required external data file.
2. Read the data using the appropriate Python library.
3. Store the retrieved data in a suitable Python data structure.
4. Pass the data to the Selenium automation script.
5. Execute the test with different data values.
6. Write updated data or results when required.
7. Verify the generated output.

## Result

External test data was successfully read and processed for Selenium automation.

---

# Experiment 12: Advanced Selenium Interactions

## Experiment Name

Mouse Hover, Keyboard Actions and JavaScript Execution

## Objective

To perform advanced browser interactions using Selenium WebDriver.

## Purpose

The purpose of this experiment is to automate user interactions that cannot
always be performed using basic Selenium commands.

## Interactions Covered

- Mouse Hover
- Keyboard Events
- Scrolling
- Drag and Drop
- JavaScript execution

## Concept / Theory

Selenium provides advanced interaction APIs for simulating user actions such
as mouse movement, keyboard input, drag-and-drop operations and scrolling.

JavaScript can also be executed through WebDriver when direct Selenium
interaction is not suitable for a particular operation.

## Procedure

1. Open the required webpage.
2. Locate the required interactive element.
3. Create the required Selenium action.
4. Perform the mouse or keyboard interaction.
5. Execute JavaScript where required.
6. Verify the resulting webpage state.

## Result

Advanced user interactions were successfully automated using Selenium WebDriver.

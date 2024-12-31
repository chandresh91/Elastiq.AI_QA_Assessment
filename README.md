# Selenium Automation Test - Table Search Demo

This project contains an automated test to validate the search functionality on the Selenium Playground Table to perform Search . The test is written in Python using Selenium WebDriver and the pytest framework.


## Objective

The objective of this project is to validate the search functionality on the Selenium Playground Table Sort & Search Demo. Specifically, the test:

- Searches for the term "New York."
- Verifies that 5 rows are returned in the search results.
- Ensures that each of the 5 rows contains the text "New York."

## Test Case Details

**Test Method:** `test_search_new_york`

### Steps:
1. Navigate to the Table Search Demo page.
2. Enter "New York" in the search box.
3. Verify that exactly 5 rows are displayed.
4. Ensure each of the 5 rows contains "New York."

### Assertions:
- The number of visible rows is exactly 5.
- Each visible row contains the string "New York."

## Dependencies

This project uses the following dependencies:

- **Python 3.x**
- **Selenium**
- **pytest**
- **WebDriver Manager** (for managing the browser drivers)

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```
## Environment Setup
**1. Install Python:**

Ensure that Python 3.x is installed on your system. You can check the version using:
`python --version`

**2. Install Dependencies:**

Use pip to install the required dependencies from requirements.txt:

`pip install -r requirements.txt`

**3. WebDriver Setup:**

Download latest version of `chromedriver.exe` and add it's path. See `DriverSetup.py`


## Running the Test
To run the tests using pytest, execute the following command:


`pytest Tests/qa_selenium_test.py`
This will automatically detect the test methods suffixed with _test and execute them.

## Test Output:

After running the test, you should see the test results in the console, indicating whether the assertions passed or failed.

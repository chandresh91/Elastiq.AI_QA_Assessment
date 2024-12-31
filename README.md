Selenium Automation Test - Table Search Demo
This project contains an automated test to validate the search functionality on the Selenium Playground Table Sort & Search Demo. The test is written in Python using Selenium WebDriver and pytest framework.

Project Structure
graphql
Copy code
TestProject/
│
├── Pages/
│   └── TableSearchPage.py        # Page Object Model class for the TableSearch page
│
├── Tests/
│   └── TestSearch.py             # Test case for validating search functionality
│
├── Utility/
│   └── DriverSetup.py            # Helper function to set up the WebDriver
│
├── .venv/                        # Virtual environment directory
│
├── requirements.txt              # List of required Python dependencies
│
└── README.md                     # Project documentation
Objective
The objective of this project is to validate the search functionality on the Selenium Playground Table Sort & Search Demo. Specifically, the test:

Searches for the term "New York."
Verifies that 5 rows are returned in the search results.
Ensures that each of the 5 rows contains the text "New York."
Test Case Details
Test Method: test_search_new_york
Steps:
Navigate to the Table Search Demo page.
Enter "New York" in the search box.
Verify that exactly 5 rows are displayed.
Ensure each of the 5 rows contains "New York."
Assertions:
The number of visible rows is exactly 5.
Each visible row contains the string "New York."
Dependencies
This project uses the following dependencies:

Python 3.x
Selenium
pytest
WebDriver Manager (for managing the browser drivers)
To install the required dependencies, run the following command:

bash
Copy code
pip install -r requirements.txt
Environment Setup
Install Python: Ensure that Python 3.x is installed on your system. You can check the version using:

bash
Copy code
python --version
Create a Virtual Environment (Optional but Recommended): You can create a virtual environment to isolate your project dependencies:

bash
Copy code
python -m venv .venv
Activate the virtual environment:

Windows:
bash
Copy code
.venv\Scripts\activate
Mac/Linux:
bash
Copy code
source .venv/bin/activate
Install Dependencies: Use pip to install the required dependencies from requirements.txt:

bash
Copy code
pip install -r requirements.txt
WebDriver Setup: The webdriver_manager library will automatically download and manage the Chrome WebDriver for you, so no manual download is required.

Running the Test
To run the tests using pytest, execute the following command:

bash
Copy code
pytest Tests/TestSearch.py
This will automatically detect the test methods prefixed with test_ and execute them.

Test Output: After running the test, you should see the test results in the console, indicating whether the assertions passed or failed.
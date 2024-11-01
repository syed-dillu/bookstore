**Bookstore Test Automation**
=============================

This repository contains test automation for a FastAPI-based bookstore application. The tests are written using pytest and utilize httpx for making asynchronous HTTP requests to the API. The testing framework integrates Allure for reporting and coverage for measuring test coverage.

**Tools and Technologies**
--------------------------

**· Python**: The programming language used for the test scripts.

**· pytest**: The testing framework used for writing and running the tests.

**· httpx**: An asynchronous HTTP client for making requests to the FastAPI application.

**· Allure**: A reporting tool that provides detailed test reports.

**· Coverage**: Provides an HTML report for test code coverage.

**· Logging**: Stores logs for each test run.

**· MagicMock**: Part of the unittest.mock library used to create mock objects for testing.

**Test Automation Structure**
-----------------------------

The test automation suite consists of several test cases covering user signup, login, book creation, update, retrieval, and deletion functionalities. The tests ensure that the API behaves as expected under various conditions.

### **Key Test Cases**

## Unit Tests

*   **User Signup**: Tests the functionality of user registration.
    
*   **User Login**: Tests the login process and the generation of access tokens.
    
*   **Token Creation**: Tests the creation of access tokens.
    
*   **Token Expiration**: Tests the expiration of access tokens after a specified duration.
    

## Integration Tests

*   **User Signup Integration**: Tests the complete flow of user registration from API request to database insertion.
    
*   **User Login Integration**: Tests the complete flow of user login, including authentication and token generation.
    
*   **Book Management Integration**: Tests the functionality of creating, updating, retrieving, and deleting books in the inventory through the API.

**Setup Instructions**
----------------------

### **Prerequisites**

· Python 3.7+

· Allure installed on the system (Refer to the Allure installation guide).

· pytest and coverage.py installed via requirements.txt.

### **Installation Steps**

**Clone the Repository**:

git clone https://github.com/syed-dillu/bookstore.git

**Navigate to the Project Directory**:

**Install the Required Packages**:

pip install -r requirements.txt

### **Pytest.ini File**

The pytest.ini file contains execution configurations, logging levels, and pytest execution commands.

**Running the Application**
---------------------------

### **Running Tests and Generating Reports**

**Execute the Batch Script**:

./run_script.bat

The run_script.bat file contains the following commands, it will automatically runs the script and generate the report

@echo off

REM Run pytest

pytest

REM Open coverage HTML report

start .\reports\coverage_report\index.html

REM Serve Allure report

start cmd /k "allure serve .\reports\allure-results"

o pytest: Executes all test cases in the tests/ folder.

o allure serve: Generates and serves the Allure report.

o Coverage report: Opens the HTML coverage report for an overview of test coverage.

## **Running Tests Manually**

To run tests with pytest:

pytest

To generate the Coverage Report results, open:

.\reports\coverage_report\index.html

To serve the Allure report:

allure serve ./reports/allure-results

**CI/CD Setup with Jenkins**
----------------------------

This repository is configured to use Jenkins for Continuous Integration (CI). The CI pipeline automatically runs tests on every push to the repository.

## **Jenkins Pipeline Configuration**

The Jenkins pipeline is defined in a Jenkinsfile at the root of the repository. The pipeline includes the following stages:

**1. Checkout**: Clones the repository to the Jenkins agent.

**2. Setup Environment**: Creates a virtual environment and installs the required dependencies.

**3. Run Unit and Integration Tests with Coverage**: Executes unit tests and generates a coverage report.

**4. Publish Coverage Report**: Archives the coverage report for further analysis.

**5. Publish Allure Report**: Generates and publishes the Allure report.

## **Running the Pipeline**

**Set Up Jenkins**: Ensure you have Jenkins installed and configured. You can set up a Jenkins job to monitor your repository for changes.

**Create a New Pipeline Job**: In Jenkins, create a new pipeline job and link it to your GitHub repository.

**Configure Build Triggers**: Use POLL SCM to trigger builds on every push.

**View Results**: Once the pipeline is configured, you can view the test results and reports in the Jenkins dashboard after each build.

**Challenges Faced**
--------------------

**. Using Httpx**: Implementing Httpx for asynchronous operations with pytest.asyncio presented challenges, as it required careful handling to ensure proper test execution.

**· Coverage Maintenance**: Ensuring 80% code coverage required thorough testing across all application logic, including edge cases.

**· Efficient SQLModel Setup**: Configuring an efficient SQLModel fixture was essential for clean and isolated test environments, allowing for streamlined test case execution.

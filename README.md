# About
This project represents the knowledge I gained during my automation course. For this project, I used the Python programming language and the Pytest testing framework to write automated tests. The framework is designed to support a wide range of platforms, including web-based applications, mobile applications, REST APIs, and desktop applications. The project is divided into two distinct components: the **Infrastructure** part, which includes design patterns, libraries, common operations, and external tools that support test execution; and the **Testing** part, which focuses on writing the test cases.

## Key Project Features:
- **Page Object Design Pattern**: Enhances code maintainability and readability by efficiently interacting with web elements.
- **Project Layers**: Organized into extensions, workflows, and test cases to create a scalable and maintainable codebase.
- **Platform Versatility**: Supports testing across multiple platforms, including web applications, mobile applications, REST APIs, Electron apps, and desktop applications.
- **Failure Handling**: Uses event listeners for graceful test failure management, ensuring the tests continue to run even when issues arise.
- **Data-Driven Testing**: Supports external file integration, especially CSV files, to enable dynamic and comprehensive testing. This approach allows the use of a wide range of test data.
- **Reporting System**: Integrates **Allure** for test reporting, including screenshots and videos, providing detailed insights into test results and helping to identify issues quickly.
- **Visual Testing**: Integrates **Applitools** to detect visual discrepancies and ensure UI integrity across applications.
- **Database Integration**: Supports integration with **MySQL** for thorough database testing (e.g., validating data in the Parabank web application).
- **Continuous Integration (CI) with Jenkins**: Automates the execution of tests with **Jenkins** to provide timely feedback on code changes and test results.

## List of Applications Tested:
- **Parabank** (Web-based Application)
- **Papa John’s Pizza** (Mobile Application)
- **jsonplaceholder.typicode.com** (Web API)
- **Windows Calculator** (Desktop Application)

## Tools & Frameworks Used:
- **Pytest** (Testing Framework)
- **Listeners** (Interface for Generating Logs and Customizing Pytest Reports)
- **MySQL Free Online Database** (Used for testing the Parabank Web Application)
- **Jenkins** (Continuous Integration and Test Execution)
- **REST Assured** (API Testing)
- **Allure Reports** (Primary Reporting System)

## Known Issues:
- The connection to the **MySQL Free Online Database** will fail due to the expiration of the associated database account.
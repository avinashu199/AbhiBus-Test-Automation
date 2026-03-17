🚍 AbhiBus Test Automation Framework
📌 Project Overview

This project is a test automation framework developed using Python, Selenium WebDriver, and Pytest to automate the bus booking workflow on the AbhiBus website.

The framework automates the complete booking flow by reading test data from an Excel file and interacting dynamically with the website elements. It includes intelligent automation logic to select buses based on maximum available discount and seat availability.

The framework is designed using reusable functions, loops, parameterization, and Pytest markers, making it scalable, maintainable, and easy to extend.

⚙️ Tech Stack

Language: Python

Automation Tool: Selenium WebDriver

Testing Framework: Pytest

Data Handling: Excel (Data Driven Testing)

Design Pattern: Page Object Model (POM)

✨ Features

✔ Data Driven Testing using Excel
✔ Automated source, destination, and travel date selection
✔ Automated customer details entry
✔ Automatically selects bus with maximum discount
✔ Dynamic seat selection based on availability
✔ Uses loops and parameterization for flexible execution
✔ Implements Pytest markers (tags) for selective test runs
✔ Custom command line parser options added in Pytest
✔ Supports cross-browser execution
✔ Reusable utility methods

📂 Project Structure
abhibus-test-automation
│
├── tests
│   └── test_abhibus_booking.py
│
├── pages
│   ├── home_page.py
│   ├── bus_selection_page.py
│   └── seat_selection_page.py
│
├── utilities
│   ├── waits.py
│   ├── excel_reader.py
│   └── common_methods.py
│
├── test_data
│   └── abhibus_testdata.xlsx
│
├── reports
│   └── html_reports
│
├── conftest.py
├── pytest.ini
└── requirements.txt
📊 Test Data (Excel Driven)

The framework reads test data from an Excel file containing inputs such as source, destination, travel date, and passenger details.

Example:

Source	Destination	Date	Customer Name	Age	Mobile	Email
Hyderabad	Bangalore	2026-04-10	Avinash	20	9989968834	avinash@gmail.com

This enables multiple test scenarios using different datasets.

🧠 Automation Workflow

The automation script performs the following steps:

Open AbhiBus website

Enter source and destination

Select travel date

Search for buses

Identify buses with the maximum discount

Automatically select the best bus

Choose available seats dynamically

Enter customer details

Complete the booking workflow (test scenario)

🧪 Running the Tests
Install dependencies
pip install -r requirements.txt
Run all tests
pytest
Run tests with HTML report
pytest --html=reports/report.html
🏷 Running Tests with Tags

Using Pytest markers:

pytest -m smoke
pytest -m regression
🌐 Cross Browser Execution

The framework supports execution on multiple browsers such as:

Chrome

Firefox

Edge

Example:

pytest --browser chrome
📸 Reports

Test execution generates HTML reports containing:

Test execution summary

Pass / Fail status

Execution duration

Failure details

Screenshots for failed test cases

CI/CD integration using Jenkins
Parallel test execution using pytest-xdist

📈 Future Improvements

Docker-based execution

Logging integration

Allure reporting

👨‍💻 Author

Avinash Uppalapati

Automation Test Engineer
Python | Selenium | Pytest | Test Automation Frameworks
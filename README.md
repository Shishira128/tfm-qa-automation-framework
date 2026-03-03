# tfm-qa-automation-framework
End-to-End QA Automation Framework for TFM web application using Selenium, Python, PyTest and Page Object Model with HTML reporting.


# TFM QA Automation Framework – End-to-End Test Automation

## 📌 Project Overview

This project is an End-to-End (E2E) automation framework built for the TFM Web Application:

## 🎥 Test Execution Recording
Screen Recording Link: https://drive.google.com/file/d/1mO9Uq1U1joJmlQ3u3EBuQyph--FqjCxX/view?usp=sharing
##
Application URL: https://dev.trulyfree.com/  
Environment: QA / Staging  
Browser: Chrome  

The framework automates the complete user journey from account creation to order placement and logout using Selenium with Python and PyTest.

---

##  Assessment Objective

This automation framework validates:

- User Signup
- Brand Navigation
- Product Selection (PLP → PDP)
- Add to Cart
- Cart Validation
- Checkout Process
- Shipping Address Addition
- Payment Processing (Test Card)
- Order Confirmation
- Order ID Capture
- Logout

The goal is to simulate a real customer purchase journey and validate system behavior using assertions.

---

## 🛠 Tech Stack Used

- Python 3.13
- Selenium WebDriver
- PyTest
- PyTest-HTML (for reporting)
- WebDriver Manager
- Chrome Browser

---

## 🏗 Framework Design

The framework follows:

✔ Page Object Model (POM)  
✔ Reusable methods  
✔ Explicit waits (WebDriverWait)  
✔ Assertions for validation  
✔ Structured folder architecture  
✔ HTML test reporting  

---

## 📂 Project Structure
TFM_QA_Automation/
│
├── pages/
│ ├── base_page.py
│ ├── signup_page.py
│ ├── brand_page.py
│ ├── product_page.py
│ ├── cart_page.py
│ ├── checkout_page.py
│ ├── payment_page.py
│ ├── order_page.py
│
├── tests/
│ └── test_e2e_flow.py
│
├── utils/
│ └── config.py
│
├── reports/
│ └── report.html
│
├── conftest.py
├── requirements.txt
├── pytest.ini
└── README.md


---

##  Framework Architecture Explanation

### 🔹 BasePage
Contains reusable methods:
- click()
- type()
- get_text()
- explicit wait handling

### 🔹 Page Classes
Each page has:
- Locators
- Page-specific methods
- Validations

Example:
- signup_page.py → Handles signup flow
- product_page.py → Handles product interactions
- payment_page.py → Handles card details entry

### 🔹 Test Layer
`test_e2e_flow.py` contains the full user journey execution.

---

##  Test Flow (Automated Scenario)

### Module 1 – Signup
- Click “Sign me up”
- Enter phone
- Enter OTP (1111)
- Enter First Name, Last Name, Email
- Verify homepage loads

### Module 2 – Brand Navigation
- Click Brands
- Select brand
- Verify Product Listing Page loads

### Module 3 – Product Selection
- Select product
- Verify Product Details Page (PDP) loads

### Module 4 – Add to Cart
- Change quantity
- Click Add to Cart
- Validate cart count updates

### Module 5 – Cart Validation
- Verify product name
- Verify quantity
- Verify price
- Proceed to Checkout

### Module 6 – Shipping Address
- Add shipping address:
    - Address: 24 Battery Pl
    - Zip: 10004
    - City: New York
    - State: New York
    - Country: USA
- Continue to Payment

### Module 7 – Payment
- Add test card:
    - Card: 4242 4242 4242 4242
    - CVV: 111
    - Expiry: 05/2026
- Confirm Order
- Verify Thank You page

### Module 8 – Order Page Validation
- Navigate to My Orders
- Capture Order ID
- Validate Order ID is generated

### Module 9 – Logout
- Navigate to Profile
- Click Sign Out
- Validate logout successful

---

## ⚙ Installation & Setup Instructions

### 1️⃣ Clone Repository


git clone <repository_url>
cd TFM_QA_Automation


### 2️⃣ Create Virtual Environment


python -m venv venv
venv\Scripts\activate (Windows)


### 3️⃣ Install Dependencies


pip install -r requirements.txt


---

## ▶ How to Execute Tests

### Run Normal Execution


pytest -v


### Run with HTML Report


pytest --html=reports/report.html --self-contained-html


---

## 📊 Reporting

The framework generates an HTML report after execution.

Location:

reports/report.html


The report contains:
- Test Status (Pass/Fail)
- Execution Time
- Environment Details
- Error Logs (if any)

---

## ✅ Validation Strategy

Assertions are added to verify:

- Page navigation (URL validation)
- Element visibility
- Cart count update
- Order ID generation
- Successful logout

The test only passes when the entire E2E flow completes successfully.

---

## 🔐 Test Data Used

### OTP
1111

### Shipping Address
24 Battery Pl  
10004  
New York  
New York  
United States of America  

### Payment Card
4242 4242 4242 4242  
CVV: 111  
Expiry: 05/2026  

---

## 🚀 Key Highlights

✔ Fully automated E2E user journey  
✔ Scalable Page Object Model  
✔ Clean, modular structure  
✔ Explicit wait strategy  
✔ Assertion-driven validation  
✔ Automated reporting  

---

## 📌 Conclusion

This framework demonstrates the ability to design and implement a scalable QA automation solution for a real-world e-commerce workflow.

The test execution validates complete user flow from signup to order placement and logout, ensuring application stability and functionality.

---

## 👤 Author: Shishira N

QA Automation Assessment Submission  
Built using Selenium + Python + PyTest

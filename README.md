# 🔌 REST API Automation Framework

## 📌 Project Overview
A modular API automation framework built to validate CRUD operations (Create, Read, Update, Delete) for RESTful services. This project currently targets **JSONPlaceholder** (simulating a real user management backend) and includes Continuous Integration (CI) via GitHub Actions.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **HTTP Client:** Requests Library
* **Testing Framework:** Pytest
* **CI/CD:** GitHub Actions
* **Reporting:** Pytest-HTML

## ✨ Key Features
* **Reusable API Wrapper:** A custom `APIClient` class that handles all GET, POST, PUT, DELETE requests with standardized headers.
* **Bot Protection Bypass:** Implements custom `User-Agent` headers to mimic real browser traffic and avoid 403 Forbidden errors.
* **CI/CD Pipeline:** Integrated with **GitHub Actions** to automatically trigger the test suite on every code push.
* **Response Validation:** Asserts Status Codes, JSON Schema, and Data Integrity.

## 🚀 How to Run Locally
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/API-Automation-Portfolio.git](https://github.com/YOUR_USERNAME/API-Automation-Portfolio.git)
    ```
2.  **Install Dependencies:**
    ```bash
    pip install requests pytest pytest-html
    ```
3.  **Run Tests:**
    ```bash
    pytest -v -s --html=report.html
    ```

## ☁️ Continuous Integration
This project runs automatically on the cloud!
* Check the **Actions** tab in this repository to see the latest build results.
* Workflow file: `.github/workflows/main.yml`
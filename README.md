# Enterprise UI Automation Framework – Books to Scrape

A production-ready UI automation framework built with **Playwright + Pytest** for validating the [Books to Scrape](https://books.toscrape.com/index.html) website.

---

## Project Overview

This framework is used to validate homepage content, book navigation, data consistency, broken links, and product images across paginated pages.

---

## Features

- Homepage validation
- Random book navigation testing
- Book data consistency checks
- Broken link detection
- Product image attribute validation
- Pagination testing
- HTML & Allure report generation
- GitHub Actions CI/CD integration
- Screenshots and video capture on failure

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Programming language |
| Playwright | Browser automation |
| Pytest | Test framework |
| pytest-playwright | Playwright-Pytest integration |
| pytest-html | HTML report generation |
| allure-pytest | Allure report generation |
| requests | HTTP link validation |

---

## Project Structure

```
project-root/
├── .github/
│   └── workflows/
│       └── playwright.yml
├── pages/
│   ├── __init__.py
│   ├── home_page.py
│   └── book_detail_page.py
├── tests/
│   ├── __init__.py
│   ├── test_homepage.py
│   ├── test_book_navigation.py
│   ├── test_data_consistency.py
│   ├── test_broken_links.py
│   └── test_images.py
├── test-results/
├── allure-results/
├── screenshots/
├── videos/
├── conftest.py
├── requirements.txt
└── README.md
```

---

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/Parisa-Reza/Enterprise-UI-Automation-Parisa-Reza
cd Enterprise-UI-Automation-Parisa-Reza
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` should contain:

```
pytest-playwright==0.5.0
pytest-html==4.1.1
allure-pytest==2.13.5
requests==2.31.0
```


---

## Running Tests

### Run All Tests

```bash
pytest
```

this will testify and create Screenshots & Videos




---

## Report Generation

### HTML Report

```bash
pytest --html=test-results/report.html --self-contained-html
```

The report is saved to `test-results/report.html` and can be opened directly in any browser.

### Allure Results

```bash
pytest --alluredir=allure-results
```

---

## Test Case Description

| # | Test Case | Description |
|---|---|---|
| 1 | Homepage Validation | URL, title, headings, and book list are verified |
| 2 | Random Book Navigation | 5 random books are clicked and detail pages are verified |
| 3 | Data Consistency | Homepage title and price are compared with the detail page |
| 4 | Broken Link Validation | All anchor href values are checked for HTTP 200 response |
| 5 | Product Image Validation | src, alt, and class attributes are verified across 5 pages |

---

## GitHub Actions CI/CD



The pipeline is triggered automatically on every **push** and **pull request** to the `main` branch.

---

## Design Decisions

- Separation of Code from UI Elements (POM): Webpage buttons and input fields are kept inside the pages/ folder, while the actual test verifications are isolated inside the tests/ folder. If a button is changed on the website, the required fix only needs to be applied in a single location.

- Automatic Screenshots via Hooks: A background listener is configured inside conftest.py. No additional code needs to be written inside individual tests to trigger screenshots; full-page captures are automatically taken at the end of every execution run and labeled with either a _PASSED or _FAILED status tag.

- Clean Git Repository Maintenance (.gitignore): Heavy execution files such as recorded videos, full-page screenshots, and the local Python virtual environment (venv/) are explicitly blocked from being uploaded to the remote GitHub code repository. By using this approach, the repository footprint is kept lightweight and fast to download.

---

## Known Limitations

- Broken link tests may take longer due to sequential HTTP requests for each URL.
- Allure reports require the Allure CLI to be installed separately for local viewing 
- Video and trace capture increase test execution time slightly.
- approximately 13-15 git commit history has been reset due to git corruption issue
- Building might fail

## Lisence
 This project is for learning purpose assigned by W3 Engineers Ltd.
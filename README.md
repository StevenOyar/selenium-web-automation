# Selenium Web Automation Tests

Simple guide to clone and run the Selenium automation tests from the repository.

## Prerequisites

- Python 3.7+
- Google Chrome browser
- Git

## Clone the Repository

```bash
git clone https://github.com/StevenOyar/selenium-web-automation.git
cd selenium-web-automation
```

## Create Virtual Environment

Create and activate a Python virtual environment:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

## Installation

1. Install required packages:
```bash
pip install selenium
```

2. Download WebDriver:
   - **For Chrome**: Download ChromeDriver from https://chromedriver.chromium.org/
   - **For Firefox**: Download GeckoDriver from https://github.com/mozilla/geckodriver/releases
   - **For Edge**: Download EdgeDriver from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   - Choose the version matching your browser version
   - Extract and add to your system PATH, or place in your project directory

## Running the Tests

1. Update credentials in the test script:
   - Replace `"your LMS email"` with your actual email
   - Replace `"Your LMS passeword"` with your actual password

2. Change the browser in the script (if needed):
   - **Chrome** (default):
     ```python
     driver = webdriver.Chrome()
     ```
   
   - **Firefox**:
     ```python
     driver = webdriver.Firefox()
     ```
   
   - **Edge**:
     ```python
     driver = webdriver.Edge()
     ```

3. Run the test:
```bash
python plp-test. 
or
python coursera-test.
```

4. The browser will open automatically. Press Enter in the terminal when finished to close the browser.

## What the Tests Do

- **Test 1**: Navigates to PLP Academy, logs in, and tests password reset flow
- **Test 2**: Opens Coursera, browses Project Manager courses, and joins a Microsoft course

## Troubleshooting

- **ChromeDriver version mismatch**: Ensure your ChromeDriver version matches your Chrome browser version
- **Module not found**: Run `pip install selenium` again
- **Element not found**: Website layouts may change; update XPaths as needed

## Notes

- Tests use explicit waits (WebDriverWait) to handle loading times
- Chrome browser must be installed on your system
- Tests will pause and wait for you to press Enter before closing
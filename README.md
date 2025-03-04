# Automation

This project is a test automation suite for Myer Account Management, focusing on login and profile update functionalities using Playwright and pytest-bdd.

## Project Structure
```
├── features
│   └── order_items.feature
├── pages
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── product_search_page.py
│   ├── product_detail_page.py
│   ├── cart_page.py
│   ├── order_summary_page.py
│   └── my_orders_page.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_order_items.py
├── utils
│   ├── __init__.py
│   ├── list_utils.py
├── .github
│   └── workflows
│       └── daily-test.yml
├── .gitignore
├── requirements.txt
└── README.md

```

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Install Playwright browsers:
    ```sh
    playwright install
    ```

### MacOS Installation

1. Install Homebrew (if not installed):
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Install Python:
    ```sh
    brew install python3
    ```

3. Follow the same installation steps as above.

### Ubuntu Installation

1. Update and install Python:
    ```sh
    sudo apt update && sudo apt upgrade
    sudo apt install python3 python3-venv python3-pip
    ```

2. Follow the same installation steps as above.


## Usage

### Run the tests:
    ```sh
    pytest --headed
    ```

## Running Tests

To run the tests, use the following command:
```sh
pytest
```

You can also run specific tests by specifying the test file:
```sh
pytest tests/test_order_items.py
```

## Project Features

### Login and Profile Update

- **Log in with an existing account**
- **Verify account settings page**
- **Update last name and mobile number**
- **Update password**
- **Validate changes persist after logout and re-login**

### Feature File

The feature file `order_items.feature` contains the scenarios for testing the Myer Account Management functionalities.

### Page Objects

The pages directory contains the Page Object Model (POM) classes for different pages of the application:
- `base_page.py`: Base class for all page objects.
- `login_page.py`: Page object for the login page.
- `home_page.py`: Page object for the home page.

# Myer Account Management - Login and Profile Update

This project is a test automation suite for Myer Account Management, focusing on login and profile update functionalities using Playwright and pytest-bdd.

## Project Structure
```
├── features
│   └── myer_account_management.feature
├── pages
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── my_account_page.py
│   ├── account_setting_page.py
│   └── update_password_page.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_account_management.py
│   └── test_login.py
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


## Notes

The production website `www.myer.com.au` has mechanisms in place to prevent automated testing. To bypass these restrictions, I employ a workaround by running Chrome in debug mode and connecting Playwright to that instance. This setup allows us to circumvent the blocking measures effectively.

## Usage

1. Start the Chrome browser in development mode with remote debugging:

    - Window 
    ```sh
    start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --user-data-dir=C:\path\data --remote-debugging-port=9222
    ```
    - Mac and Ubuntu
    ```
    google-chrome --user-data-dir=/path/to/data --remote-debugging-port=9222
    ```

2. Run the tests:
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
pytest tests/test_login.py
```

## Project Features

### Login and Profile Update

- **Log in with an existing account**
- **Verify account settings page**
- **Update last name and mobile number**
- **Update password**
- **Validate changes persist after logout and re-login**

### Feature File

The feature file `myer_account_management.feature` contains the scenarios for testing the Myer Account Management functionalities.

### Page Objects

The pages directory contains the Page Object Model (POM) classes for different pages of the application:
- `base_page.py`: Base class for all page objects.
- `login_page.py`: Page object for the login page.
- `home_page.py`: Page object for the home page.
- `my_account_page.py`: Page object for the My Account page.
- `account_setting_page.py`: Page object for the Account Settings page.
- `update_password_page.py`: Page object for the Update Password page.



## Notes
- The Production website `www.myer.com.au` has some mechanism to prevent the automation test. So we need to do an workaround solution that run the Chrome on debug mode and connect playwright to that instance. With that setup we can work arund the block
Feature: Myer Account Management - Login and Profile Update

  Scenario: Log in with an existing account
    Given the user is on the login page
    When the user enters username "chuyenspam13@gmail.com" and password "At12345614"
    And the user clicks the login button
    Then the user should be redirected to the account dashboard

  Scenario: Verify account settings page
    Given the user is logged into their Myer account
    When the user navigates to the account settings page
    Then the account settings page should display

  Scenario: Update last name, and mobile number
    Given the user is on the account settings page
    When the user updates their last name to "Tuasaan", and mobile number to "0411111125"
    And clicks the Update button
    Then the Success message should be displayed

  Scenario: Update password
    Given the user is on the account settings page
    When the user click on Update password link
    And enter the old password is "At12345614" and new password is "At12345615"
    And clicks the "Save Changes" button
    Then the password update success message should be displayed

  Scenario: Validate changes persist after logout and re-login
    Given the user is logged out
    When logs in with username "chuyenspam13@gmail.com" and password "At12345615"
    And the user navigate to the account settings page
    Then it should show lastname is "Tuasaan" and mobile number is "0411111125"
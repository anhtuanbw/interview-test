Feature: Online Shopping and Order Placement

  Scenario: A registered user places an order successfully
    Given the user is logged in as a registered user
    When the user adds the following items to the cart:
      | Category             | Item Name | Quantity |
      | Men-Tops-Jackets     |           | 2        |
      | Men-Bottoms-Pants    |           | 1        |
    And the user proceeds to the Cart page
    And the user reviews the Order Summary including products and prices
    And the user enters a valid delivery address
    And the user selects a delivery method
    And the user places the order
    Then the order should be successfully submitted
    And the order should be visible under "My Orders"

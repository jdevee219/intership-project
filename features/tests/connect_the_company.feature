Feature: Connect the company
  # Verifying the "Connect the developer" button functionality

  Scenario: Connect the developer opens in new tab
    Given Open the main page
    When Enter email tower219@gmail.com
    And Enter password Cooper@221
    And Click on Connect the developer button
    And Switch to new window
    Then Verify For Developers page is opened
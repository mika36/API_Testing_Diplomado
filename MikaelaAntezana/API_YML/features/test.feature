Feature: API

Scenario:
    Given I have a connection to "http://www.google.com"
    When I GET
    Then I receive the status code 200
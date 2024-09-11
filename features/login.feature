@login
Feature: Login

  Background:
    Given I am on the login page

  @successful
  Scenario: Successful login with valid credentials
    When I enter valid credentials
    And I click login button
    Then I should be redirected to my account page

  @unsuccessful
  Scenario: Unsuccessful login with invalid credentials
    When I enter invalid credentials
    And I click login button
    Then I should see an error message
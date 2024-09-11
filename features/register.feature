@register
Feature: User Registration

  Background:
    Given I am on the registration page


  @successful
  Scenario: Successful registration with valid details
    When I enter a valid email
    And I click create an account button
    Then I should be redirected to the account creation page
    When I enter valid details for account creation
    And I submit the registration form
    Then I should be redirected to my account page


  @unsuccessful
  Scenario: Unsuccessful registration email has already been registered
    When I enter an already registered email
    And I click create an account button
    Then I should see an error message email has already been registered


  @unsuccessful
  Scenario: Unsuccessful registration with invalid details
    When I enter a valid email
    And I click create an account button
    Then I should be redirected to the account creation page
    When I enter invalid details for account creation
    And I submit the registration form
    Then I should see error messages for invalid details

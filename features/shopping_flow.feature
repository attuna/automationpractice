@e2e
Feature: Shopping Flow

  Background:
    Given I am on the homepage

  @successful
  Scenario: Add a product to the cart and proceed to checkout
    When I choose a product
    Then I am redirected to the product detail page
    When I select available size
    And I add the product to the cart
    And I proceed to checkout
    Then I should be redirected to the checkout page
    And the product should be in the cart
@sorting @filtering
Feature: Item Sorting and Filtering

  Background:
    Given I am on the product listing page

  @successful
  Scenario: Filter and sort items by price lowest first
    When I filter items by category
    When I sort items by price asc
    Then I should see items sorted by price in ascending order


  @successful
  Scenario: Sort items by price highest first
    When I sort items by price desc
    Then I should see items sorted by price in descending order

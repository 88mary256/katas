# Created by Admin at 3/26/2019
Feature: This is a test
  # Enter feature description here

  Scenario: Create Todoly project
    Given I made connection
    When I create project with data mi octavo gherkin
    Then The create project status is 204
    And Project Name is "Project 1"
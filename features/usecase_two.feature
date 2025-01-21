Feature:usecase_two

  Background:
    Given Login to salesforce

  Scenario: Create an account attach contact and opportunity
    When Create an account: "Tech" attach opportunity: "Cycle" and contact: "Biju",close_date: "31/12/2025",Stage: "Qualify"
    Then Validate these account: "Tech" attach opportunity: "Cycle" and contact: "Biju"
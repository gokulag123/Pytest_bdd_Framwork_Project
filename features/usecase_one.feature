Feature:usecase_one

  Background:
    Given Login to salesforce


  Scenario Outline: Creating a lead
    When Creating new lead as "<firstname>" "<lastname>" "<company>"
    Then Validating the lead with "<firstname>" "<lastname>"

    Examples:
      | firstname | lastname  | company  |
      | Rajeev    | Malhotra  | Visa     |
      | Sam       | Malik     | DK       |

  Scenario Outline: Creating an account
    When Creating an account "<account_name>"
    Then Validating account created "<account_name>"

    Examples:
      | account_name |
      | Maharajas    |
      | Viswajothi   |

  Scenario: Converting lead to account as new account
    When Convert lead to account lead "Rajeev" "Malhotra"
    Then Validating account created "Visa"
#
  Scenario: Converting lead to an existing account
    When Convert lead to an existing "Acc_Convert" "Sam" "Malik"
    Then Checking the new contact created : "Sam Malik" and account: "Acc_Convert"









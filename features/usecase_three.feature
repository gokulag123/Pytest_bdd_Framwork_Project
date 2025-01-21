Feature:usecase_three

  Background:
    Given Login to salesforce

  Scenario: Create an account attach contact and opportunity
      When Creating an event subject: "ICC_Champions",date:"25-Mar-2025",time:"10:00 pm",Account: "Acc_Meeting"
      Then Validating the event subject: "ICC_Champions",date:"25-Mar-2025",time:"10:00 pm",Account: "Acc_Meeting"
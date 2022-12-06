#User Story 1
Feature: Creating an account
Scenario: I am a new user trying to register a new account
Given a valid email address 
Given a valid password
Given a first and last name
When I press “register” 
Then I will have registered a new account


Scenario: I am a user trying to register a new account with an already registered email 
Given a valid username
Given a first and last name
Given a valid email address but it is already registered 
When I press “add a user":
Then I will be given an error saying email is already being used

#User Story 2
Feature: User login
Scenario: I am a registered user going to the application to input their data
Given an already registered email
Given the password registered with the email
When I press “Login”
Then I will be logged into the app and brought to the home screen

#User Story 3
Feature: Edit Task 
Scenario: I am a registered user wanting to edit an already posted Task
Given I am a registered user already logged in 
Given an already posted Task 
Given that I am on the "my tasks" screen
When I press Edit 
Then I will be able to edit my task 
Given my edits have been made 
When I press the update task button 
Then the edit task will be posted with the edits

#User Story 4
Feature: Adding a task
Scenario: I am a registered user wanting to add a task to my project 
Given a Task Name
Given  Task Members
Given Task info
Given Task Importance 
When I press “Add Task”
Then I will be taken to the "my tasks" screen 
And the new task will be saved 
And added to the backlog

#User Story 5 
Feature: Delete a Task 
Scenario: I am a registered user wanting to delete a task
Given an already posted Task 
Given that I am on the "my tasks" screen
When I press Delete 
Then that task will be deleted

#User Story 6 
Feature: Task Comment 
Scenario: I am a registered user wanting to comment on a task
Given an already posted Task 
Given that I am on the specific Task page
When I type in a comment into the comment text area and press the comment
Then the comment will be posted below the task details 

#User Story 7
Feature: Task Importance 
Scenario: I am a registered user wanting to rate a task on a scale of 0-10 importance 
Given I am on either the added task or edit task screen
Given I type in an importance "score" of 0-10 and I press update or add task
Then the task will have an importance rating 

#User Story 8 
Feature: Task Members 
Scenario: I am a registered user wanting to add members to a task 
Given I am on either the add task or edit task screen 
Given I type in Members names into the correct text area and press update or add task 
Then the task will have members associated with it 

#User Story 9
Feature: Task Name 
Scenario: I am a registered user wanting to add a name to a task 
Given that I am on either the add task or edit task screen
Given I type a name for the task into the correct input aera and press update or add task
Then the task will have a name 

#User Story 10
Feature: Task Deadline
Scenario: I am a registered user wanting to add a deadline date to a task 
Given that I am on either the add task or edit task screen
Given I enter a date into the deadline input and press update or add task 
Then the task will have a deadline date 

#User Story 11
Feature: Task Status
Scenario: I am a registered user wanting to add a status to a task 
Given that I am on either the add task or edit task screen 
Given I select a status from the drop down and press update or add task 
Then the task will have a status 


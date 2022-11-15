#User Story 1 when registering a new user 
Feature: Adding a new user. In order to use the application everyone needs to be registered as a user so we can save their data to their account. 
Scenario: I am a new user trying to register a new account
Given a valid email address 
Given a valid username
Given a role selection
Given a first and last name
When I press “add user” 
Then I will have registered a new account


Scenario: I am a user trying to register a new account with a already registered email 
Given a valid username
Given a role selection
Given a first and last name
Given a valid email address but it is already registered 
When I press “add user:
Then I will be given an error saying email is already being used


#User Story 2
Feature: User adding their information into application
Scenario: I am a registered user going to the application to input their data
Given username
Given password
When I press “Login”
Then I will be taken to the Home screen 
When I press “Data and analytics”
Then I will be taken to the page where it will have a plus symbol to the bottom right of the screen.
Then I will be able to insert user information that needs to be in that section.
When I hit done or save near the bottom the data will be stored and will show on screen
Then I will be able to see data






#User Story 3
Feature: Customization 
Scenario I want to customize the applications appearance 
Given username
Given password
When I press “Login”
Then I will be taken to the Home screen 
When I press “Settings”
Then will take me to user options
When in user options you will see the customization options
Then you will be able to pick Light or Dark mode
Then you can either choose the color for the application like light blue or green or yellow
Given a save option you will then save 
Then the changes will be saved and you will be able to see the new customization


#User Story 4
Feature: Adding a task
Scenario I want to add a task to my project 
Given a Deadline Date
Given a Task Name
Given a Task Team
Given a Task Leader
Given Task info
When I press “Add Task”
Then I will be taken to the Home screen 
And the new task will be saved 
And added to the backlog
When members of the given task team and team leader open the home screen 
Then they will see the given task in their To-Do and backlog
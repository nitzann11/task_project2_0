
## Task manager project
## by: Nitzan BZ

An OOP python project that was made for user and tasks managment using the VSC terminal as GUI as part of my coding studies.

#How the project works?:
The App is built from multiple parts and divided to diffrent modules +20points:

OOP- according to demands +55 points
Classes-there are 2 classes files in the project:user_class.py and class_Task.py to each their own parameters according to the demands and they rely on each other on multiple fields.

Functions-There are 4 functions files.

 2 dedicated files for CRUD functions, crud.py and login_functions.py. The first is for users info crud and the second is for tasks info crud

 files.py for data transfer managment. Data is stored on 2 pickle files- "accounts.pickle" for users data and "tasks.pickle" for tasks data

 tests.py for unit testing for the tasks Crud only (according to the demands)

 and 2 main files- one is main.py which functions as the starting page of the proggram and users crud manipulation the second one is task_manager.py for tasks crud manipulation.






## Functions

The project uses multiple functions, the description for each on of them can be found in a comment on each one of them

## how it work?
The GUI is very self explenatory..
first the user will want to create an account by providing his details accordingly

after that he can use freely the first menu or log in into the second one

on the second menu the user can create tasks and play with the info as he/she wishes. 

Individual user premissions and responsibilities+10 points

For premissions the client should use the admin password - 9999 - (the input will be turned automatically to string so an error won't occour)

categories selection +5 points

Client can select tasks through BOTH categories from menu (list) for easy use AND free text (provided the necessary premissions.)

Overall points- 100

Had great time building this project and it tought me alot about the in and out of OOP at least on a basic level.
⠀⡶⠛⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⠚⢲⡀⠀
⣰⠛⠃⠀⢠⣏⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣀⡀⠀⠀⠀⣸⡇⠀⠈⠙⣧
⠸⣦⣤⣄⠀⠙⢷⣤⣶⠟⠛⢉⣁⣠⣤⣤⣤⣀⣉⠙⠻⢷⣤⡾⠋⢀⣠⣤⣴⠟
⠀⠀⠀⠈⠳⣤⡾⠋⣀⣴⣿⣿⠿⠿⠟⠛⠿⠿⣿⣿⣶⣄⠙⢿⣦⠟⠁⠀⠀⠀
⠀⠀⠀⢀⣾⠟⢀⣼⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣷⡄⠹⣷⡀⠀⠀⠀
⠀⠀⠀⣾⡏⢠⣿⣿⡯⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠤⠤⠽⣿⣿⡆⠹⣷⡀⠀⠀
⠀⠀⢸⣟⣠⡿⠿⠟⠒⣒⣒⣈⣉⣉⣉⣉⣉⣉⣉⣁⣒⣒⡛⠻⠿⢤⣹⣇⠀⠀
⠀⠀⣾⡭⢤⣤⣠⡞⠉⠉⢀⣀⣀⠀⠀⠀⠀⢀⣀⣀⠀⠈⢹⣦⣤⡤⠴⣿⠀⠀
⠀⠀⣿⡇⢸⣿⣿⣇⠀⣼⣿⣿⣿⣷⠀⠀⣼⣿⣿⣿⣷⠀⢸⣿⣿⡇⠀⣿⠀⠀
⠀⠀⢻⡇⠸⣿⣿⣿⡄⢿⣿⣿⣿⡿⠀⠀⢿⣿⣿⣿⡿⢀⣿⣿⣿⡇⢸⣿⠀⠀
⠀⠀⠸⣿⡀⢿⣿⣿⣿⣆⠉⠛⠋⠁⢴⣶⠀⠉⠛⠉⣠⣿⣿⣿⡿⠀⣾⠇⠀⠀
⠀⠀⠀⢻⣷⡈⢻⣿⣿⣿⣿⣶⣤⣀⣈⣁⣀⡤⣴⣿⣿⣿⣿⡿⠁⣼⠟⠀⠀⠀
⠀⠀⠀⢀⣽⣷⣄⠙⢿⣿⣿⡟⢲⠧⡦⠼⠤⢷⢺⣿⣿⡿⠋⣠⣾⢿⣄⠀⠀⠀
⢰⠟⠛⠟⠁⣨⡿⢷⣤⣈⠙⢿⡙⠒⠓⠒⠓⠚⣹⠛⢉⣠⣾⠿⣧⡀⠙⠋⠙⣆
⠹⣄⡀⠀⠐⡏⠀⠀⠉⠛⠿⣶⣿⣦⣤⣤⣤⣶⣷⡾⠟⠋⠀⠀⢸⡇⠀⢠⣤⠟
⠀⠀⠳⢤⠼⠃⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠘⠷⢤⠾⠁⠀
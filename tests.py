from files import dump
from crud import create_task,view_tasks,update_task,delete_task
from login_functions import create_user,view_user
from random import randrange,choice
from task_class import Task
from user_class import User
from datetime import datetime


def reset_pickle(filename:str="tasks.pickle",data:list=[]):
    """This function was made for convinience it will reset the pickle file so the user wont be needing to do it each time. it is added to the start of every testing function."""
    with open(filename,"wb") as f:
        dump(data,f)

def random_user_test(num:int=10):
    """This function will generate  user objects and provide a general example of how  data is created using small generic batch of inputs you will expect to recieve from the user."""
    reset_pickle("accounts.pickle")
    for i in range(num):
        create_user(User(
            name=choice(["luffy","zoro","sanji","nami","chopper"]),
            username=choice(["strawhat","piratehunter","blacklag","catburgler","racoon"]),
            password=choice(["111","222","333","444","555"]),
            email=choice(["walla","gmail","hotmail","yahoo","other"]),))
    view_user()


def random_task_test(num:int=10):
    """This function will generate  task objects and provide a general example of how  data is created using small generic batch of inputs you will expect to recieve from the user for tasks."""
    reset_pickle()
    for i in range(num):
        create_task(Task(name=choice(["luffy","zoro","sanji","nami","chopper"]),
                        task_name=choice(["grocery","bills","errends","clean car","meeting","buy clothes","read book"]),
                        category=choice(["general","cleaning","shopping","work","workout"]),
                        deadline=datetime(year=2023,month=randrange(8,12),day=randrange(1,31))))
    view_tasks()

def specific_create_user():
    """This function is an example of how C-create works using a premade info without reciving an exception"""
    reset_pickle("accounts.pickle")
    create_user(User(
        name="mr.test",username="cooltest123",password="testest",email="test@mail.com"))
    try:
        view_user("2","mr.test")
    except:
        print("this is not working!!!")

def specific_create_task():
    """This function is an example of how R-Read works using a premade info without reciving an exception"""
    reset_pickle()
    create_task(Task(name="mr.test",task_name="testing the functions",category="general",deadline=(datetime(year=2023,month=8,day=2))))
    try:
        view_tasks("3","testing the functions")
    except:
        print("this is not working 2!!!")

def specific_del():
    """This function is an example of how D-Delete works using a premade info without reciving an exception function will recieve 2 objects display them,delete one and will display the end result as well"""
    reset_pickle()
    create_task(Task(name="mr.test",task_name="first test",category="general",deadline=(datetime(year=2023,month=8,day=3))))
    create_task(Task(name="mr.test",task_name="second test",category="general",deadline=(datetime(year=2023,month=8,day=3))))
    view_tasks("1")
    delete_task(name="mr.test",task_name="second test")
    view_tasks()

def specific_update():
    """This function is an example of how U-Update works using a premade info without reciving an exception (will only show one way of updating as it works about the same value will change according to the parameter provided by the client.)"""
    reset_pickle()
    specific_create_task()
    view_tasks("1")
    try:
        update_task(parameter="1",value="mr.test2",name="mr.test",task_name="testing the functions")
        view_tasks(parameter="2",value="mr.test2")
    except:
        print("update not working..")

def test_menu():
    """This function serves as a simplfied menu for testing it is ordered by the order tests should follow."""
    print("""
    test menu:
          1.make random useres
          2.make random tasks
          3.make specific user
          4.specific view
          5.specific delete
          6.specific update
          7.exit""")
    options=("1","2","3","4","5","6","7")
    option=input("choose option 1-6: ")

    if option in options:
        if option=="1":
            random_user_test()
        elif option=="2":
            random_task_test()
        elif option=="3":
            specific_create_user()
        elif option=="4":
            specific_create_task()
        elif option=="5":
            specific_del()
        elif option=="6":
            specific_update()
        elif option=="7":
            exit()

test_menu()
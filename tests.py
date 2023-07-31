from files import dump
from crud import create_task,view_tasks,update_task,delete_task
from login_functions import create_user,view_user
from random import randrange,choice
from task_class import Task
from user_class import User
from datetime import datetime


def reset_pickle(filename:str="tasks.pickle",data:list=[]):
    with open(filename,"wb") as f:
        dump(data,f)

def random_user_test(num:int=10):
    for i in range(num):
        create_user(User(
            name=choice(["luffy","zoro","sanji","nami","chopper"]),
            username=choice(["strawhat","piratehunter","blacklag","catburgler","racoon"]),
            password=choice(["111","222","333","444","555"]),
            email=choice(["walla","gmail","hotmail","yahoo","other"]),))
    view_user()


def random_task_test(num:int=10):
    for i in range(num):
        create_task(Task(name=choice(["luffy","zoro","sanji","nami","chopper"]),
                        task_name=choice(["grocery","bills","errends","clean car","meeting","buy clothes","read book"]),
                        category=choice(["general","cleaning","shopping","work","workout"]),
                        deadline=datetime(year=2023,month=randrange(8,12),day=randrange(1,31))))
    view_tasks()

def specific_create_user():
    reset_pickle("accounts.pickle")
    create_user(User(
        name="mr.test",username="cooltest123",password="testest",email="test@mail.com"))
    try:
        view_user("2","mr.test")
    except:
        print("this is not working!!!")

def specific_create_task():
    reset_pickle()
    create_task(Task(name="mr.test",task_name="testing the functions",category="general",deadline=(datetime(year=2023,month=8,day=2))))
    try:
        view_tasks("3","testing the functions")
    except:
        print("this is not working 2!!!")

def specific_del():
    reset_pickle()
    create_task(Task(name="mr.test",task_name="first test",category="general",deadline=(datetime(year=2023,month=8,day=3))))
    create_task(Task(name="mr.test",task_name="second test",category="general",deadline=(datetime(year=2023,month=8,day=3))))
    view_tasks("1")
    delete_task(name="mr.test",task_name="second test")
    view_tasks()

def specific_update():
    reset_pickle()
    specific_create_task()
    view_tasks("1")
    try:
        update_task(parameter="1",value="mr.test2",name="mr.test",task_name="testing the functions")
        view_tasks(parameter="2",value="mr.test2")
    except:
        print("update not working..")

def test_menu():
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
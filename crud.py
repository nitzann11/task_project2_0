from files import save_data,load_data
from task_class import Task
from datetime import datetime


def create_task(task=Task):
    """This function load the pickle file, handles new Task class data and writes it anew into the pickle file again."""
    user_data=load_data(filename="accounts.pickle")
    data=load_data()
    for user in user_data:
        if task.name==user.name and task.category in user.task_premissions:
            if task not in data:
                data.append(task)
                save_data(data=data)
                print("Task created!")
        else:
            print("Creation error..")


def view_tasks(parameter:str="1",value:str=""):
    """"This function lets us see data on existing tasks, it can even filter it in diffrent ways"""
    titles="\nName\t\tTask name\t\tCategory\t\t\tCreation date\t\t\tDeadline\t\t\tTime left'"
    data=load_data(filename="tasks.pickle")
    for task in data:
        if parameter=="1":
            print(titles)
            print(task)
        elif parameter=="2":
            if task.name==value:
                print(titles)
                print(task)
        elif parameter=="3":
            if task.task_name==value:
                print(titles)
                print(task)
        elif parameter=="4":
            if task.category==value:
                print(titles)
                print(task)



def update_task(parameter:str="",value:str="",name:str="",task_name:str="",date_value:datetime=datetime):
    """This function lets us update and manipulate information on existing tasks and saves it, it has several validations so data won't duplicate or mess up."""
    user_data=load_data(filename="accounts.pickle")
    data=load_data()
    for task in data:
        if task.name==name and task.task_name==task_name:
            if parameter=="1":
                task.name=value
            elif parameter=="2":
                task.task_name=value
            elif parameter=="3":
                for i in user_data:
                    if value in i.task_premissions:
                        task.category=value
                    else:
                        print("Permission missing..")
            elif parameter=="4":
                task.deadline=date_value
            elif parameter=="5":
                task.time_diffrence=task.deadline-task.creation_date
        
            save_data(data=data)        
            print("Task has been updated!")
        else:
            print("Update error..")
def delete_task(name,task_name):
    """This function lets us delete tasks simply by providing the name of the one responsible to it and the task name."""
    data=load_data()
    for task in data:
        if task.name==name and task.task_name==task_name:
            data.remove(task)
            save_data(data=data) 
            print("Task has been deleted!")
    else:
        print("Task not found..")
               
def add_premission(username:str="",password:str="",value:str="",admin_password:str=""):
    """This function lets us add more premissions to an individual User class's object, without the required premission user wont be able to create a customized category for tasks.
    ADMIN PASSWORD IS "9999" !!!"""
    data=load_data("accounts.pickle")
    for user in data:
        if user.username==username and user.password==password and admin_password=="9999":
            if value not in user.task_premissions:
                user.task_premissions.append(value)
                save_data(filename="accounts.pickle",data=data)
                print("Premission has been granted!")
            else:
                print(" Task already exist..")
    

    
def del_premission(username,password,value,admin_password):
    """This function is the oposite end of add_premission, it lets us remove a premission from an object from customized ones to the basic ones that comes in initialzion of the object."""
    data=load_data("accounts.pickle")
    for user in data:
        try:
            if user.username==username and user.password==password and admin_password=="9999":
                if value in user.task_premissions:
                    user.task_premissions.remove(value)
                    save_data(filename="accounts.pickle",data=data)
                    print("Premission has been removed!")
                else:
                    print("Value not in premissions..")
            else:
                print("Wrong info..")
        except:
            print("Invalid info..")
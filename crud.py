from files import save_data,load_data
from task_class import Task
from datetime import datetime

def create_task(task=Task):
    user_data=load_data(filename="accounts.pickle")
    data=load_data()
    for user in user_data:
        if task.name==user.name and task.category in user.task_premissions:
            if task not in data:
                data.append(task)
                save_data(data=data)
                print("task created.")
        else:
            print("creation error..")


def view_tasks(parameter:str="1",value:str=""):
    titles="\nName\t\tTask name\t\tcategory\t\t\tCreation date\t\t\tDeadline\t\t\tTime left'"
    data=load_data()
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
    user_data=load_data(filename="accounts.pickle")
    data=load_data()
    for task in data:
        if task.creator_name==name and task.task_name==task_name:
            if parameter=="1":
                task.creator_name=value
            elif parameter=="2":
                task.task_name=value
            elif parameter=="3":
                for i in user_data:
                    if value in i.task_premissions:
                        task.category=value
                    else:
                        print("permission missing..")
            elif parameter=="4":
                task.deadline=date_value
            elif parameter=="5":
                task.time_diffrence=task.creation_date-task.deadline
        
            save_data(data=data)        
            print("task has been updated")
        else:
            print("update error..")
def delete_task(name,task_name):
    data=load_data()
    for task in data:
        if task.creator_name==name and task.task_name==task_name:
            data.remove(task)
            save_data(data=data) 
            print("task deleted.")
        else:
            print("task wasn't found.")
               
def add_premission(username,password,value,admin_pass):
    admin_password="9999"
    data=load_data()
    try:
        for user in data:
            if user.username==username and user.password==password and admin_pass==admin_password:
                if value not in user.task_premissions:
                    data.task_premissions.append(value)
                    save_data(data=data)
                    print("premission has been granted")

    except:
        print("invalid info")

    
def del_premission(username,password,value,admin_pass):
    admin_password="9999"
    data=load_data()
    for user in data:
        try:
            if user.username==username and user.password==password and admin_pass==admin_password:
                if value in user.task_premissions:
                    data.user.task_premissions.remove(value)
                    save_data(data=data)
                    print("premission has been removed")
        except:
            print("invalid info")
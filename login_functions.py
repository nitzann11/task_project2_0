from user_class import User
from files import save_data,load_data
from task_manager import tasks_manager

def login(username:str="",password:str=""):
        data=load_data(filename="accounts.pickle")
        for user in data:
                if user.username==username and user.password==password:
                    print(f"\nWelcome {user.name}!")
                    tasks_manager()
                else:
                    print("wrong cradentials..")
                    
           
           
            


def create_user(user:User):
    data=load_data(filename="accounts.pickle")
    validation=True
    try:
        for i in data:
            if i.username==user.username and i.password==user.password:
                validation=False 
        if validation==True:
            data.append(user)
            save_data(filename="accounts.pickle",data=data)
        elif validation==False:
            print("user already registered")
    except:
        print("creation error.")



            

def view_user(parameter:str="1",value:str=""):
    data=load_data("accounts.pickle")
    for user in data:
        if parameter=="1":
            print(user)
        elif parameter=="2":
            if value==user.name:
                print(user)
        elif parameter=="3":
            if value==user.username:
                print(user)
        elif parameter=="4":
            if value in user.task_premissions:
                print(user)
    

def update_user(parameter:str="",value:str="",username:str="",password:str=""):
    data=load_data(filename="accounts.pickle")
    try:
        for user in data:
            if parameter=="1":
                if username==user.username and password==user.password:
                    user.name=value
            elif parameter=="2":
                if username==user.username and password==user.password:
                    user.username=value
            elif parameter=="3":
                if username==user.username and password==user.password:
                    user.password=value
            elif parameter=="4":
                if username==user.username and password==user.password:
                    user.email=value
        save_data(filename="accounts.pickle",data=data)
    except:
        print("update error.")
def delete_user(username:str="",password:str=""):
    data=load_data(filename="accounts.pickle")
    try:
        for user in data:
            if username==user.username and password==user.password:
                data.remove(user)
                save_data(filename="accounts.pickle",data=data)
                print("user has been deleted")
    except:
        print("delete error.")
from crud import create_task,view_tasks,update_task,delete_task,add_premission,del_premission
from task_class import Task
from datetime import datetime

def tasks_manager():
    while True:
        print("""
        Tasks manager:
        1.create a new task
        2.view tasks
        3.update existing task
        4.delete a task
        5.add user premission
        6.delete user premission
        7.return to main menu""")
        options=("1","2","3","4","5","6","7")
        action=str(input("choose action 1-7: "))
        category_options=("1","2","3","4","5","6","7")
        if action in options:
            if action=="1":
                name=str(input("task owner: "))
                task_name=str(input("task name: "))
                print("""
                category menu:
                    choose category for the task:
                      1.general
                      2.cleaning
                      3.shopping
                      4.work
                      5.workout
                      6.custom category (requires permission first)""")
                category_type=str(input("choose category type: "))
                if category_type in category_options:
                    if category_type=="1":
                        category="general"
                    elif category_type=="2":
                        category="cleaning"
                    elif category_type=="3":
                        category="shopping"
                    elif category_type=="4":
                        category="work"
                    elif category_type=="5":
                        category="workout"
                    elif category_type=="6":
                        category=str(input("task category: "))
                deadline=datetime(year=int(input("enter year")),month=int(input("enter month:")),day=int(input("enter day")))
                create_task(Task(name=name,task_name=task_name,category=category,deadline=deadline))
                print("task has been added")
            
            elif action=="2":
                view_options=("1","2","3","4")
                print("""
                view by:
                      1.view all
                      2.view by task owner
                      3.view by task name
                      4.view by category""")
                view_action=str(input("choose option 1-4: "))
                if view_action in view_options:
                    if view_action=="1":
                        view_tasks()
                    elif view_action=="2" or view_action=="3" or view_action=="4":
                        filter_by=str(input("write the value to filter by: "))
                        view_tasks(parameter=view_action,value=filter_by)
                else:
                    print("invalid input..")
            
            elif action=="3":
                update_options=("1","2","3","4","5")
                print("""
                task update menu:
                 1.update task owner
                 2.update task name
                 3.update task category
                 4.update task deadline
                 5.update remaining time
                """)
                update_action=str(input("choose action 1-5: "))
                if update_action in update_options:
                    find_name=str(input("enter task owner: "))
                    find_task_name=str(input("enter task name: "))
                    if update_action=="1":
                        new_change=str(input("enter the new name: "))
                        update_task(parameter=update_action,value=new_change,name=find_name,task_name=find_task_name)
                    elif update_action=="2":
                        new_change=str(input("enter the new task name: "))
                        update_task(parameter=update_action,value=new_change,name=find_name,task_name=find_task_name)
                    elif update_action=="3":
                        new_change=str(input("enter the new category name: "))
                        update_task(parameter=update_action,value=new_change,name=find_name,task_name=find_task_name)
                    elif update_action=="4":
                        new_change=datetime(year=int(input("year: ")),month=int(input("month: ")),day=int(input("day: ")))
                        update_task(parameter=update_action,date_value=new_change,name=find_name,task_name=find_task_name)
                    elif update_action=="5":
                        update_task(parameter=update_action,name=find_name,task_name=find_task_name) 
                else:
                    print("invalid input")
                
            
            elif action=="4":
                del_name=str(input("specify task owner: "))
                del_task_name=str(input("specify task name: "))
                delete_task(del_name,del_task_name)
            
            elif action=="5":
                perm_username=str(input("which username to give permission: "))
                perm_password=str(input("enter user's password"))
                a_pass=str(input("enter admin password: "))
                new_perm=str(input("enter new task type: "))
                add_premission(username=perm_username,password=perm_password,admin_pass=a_pass,value=new_perm)
                
            elif action=="6":
                del_perm_username=str(input("which username to take permission: "))             
                del_perm_password=str(input("enter user's password"))
                del_a_pass=str(input("enter admin password: "))
                del_premission(username=del_perm_username,password=del_perm_password,admin_pass=del_a_pass)
                
            elif action=="7":
                break
        else:
            print("invalid input")

from crud import create_task,view_tasks,update_task,delete_task,add_premission,del_premission
from task_class import Task
from datetime import datetime


def tasks_manager():
    """This function serves as the second menu which lets client manipulate data on tasks through CRUD such as: create,read,update and delete tasks. Client can also give premissions for users for new types of categories. Exiting this menu will lead the client back to the main menu."""
    while True:
        print("""
        Tasks manager:
        1.Create a new task
        2.View tasks
        3.Update existing task
        4.Delete a task
        5.Add user premission
        6.Delete user premission
        7.Return to main menu""")
        options=("1","2","3","4","5","6","7")
        action=str(input("Choose action 1-7: "))
        category_options=("1","2","3","4","5","6","7")
        if action in options:
            if action=="1":
                name=str(input("Task owner: "))
                task_name=str(input("Task name: "))
                print("""
                Category menu:
                    Choose category for the task:
                      1.General
                      2.Cleaning
                      3.Shopping
                      4.Work
                      5.Workout
                      6.Custom category (requires permission first)""")
                category_type=str(input("Choose category type: "))
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
                        category=str(input("Task category: "))
                deadline=datetime(year=int(input("Enter year: ")),month=int(input("Enter month: ")),day=int(input("Enter day: ")))
                create_task(Task(name=name,task_name=task_name,category=category,deadline=deadline))
                print("Task has been added!")
            
            elif action=="2":
                view_options=("1","2","3","4")
                print("""
                View by:
                      1.View all
                      2.View by task owner
                      3.View by task name
                      4.View by category""")
                view_action=str(input("Choose option 1-4: "))
                if view_action in view_options:
                    if view_action=="1":
                        view_tasks()
                    elif view_action=="2" or view_action=="3" or view_action=="4":
                        filter_by=str(input("Write the value to filter by: "))
                        view_tasks(parameter=view_action,value=filter_by)
                else:
                    print("Invalid input..")
            
            elif action=="3":
                update_options=("1","2","3","4","5")
                print("""
                Task update menu:
                 1.Update task owner
                 2.Update task name
                 3.Update task category
                 4.Update task deadline
                 5.Update remaining time
                """)
                update_action=str(input("Choose action 1-5: "))
                if update_action in update_options:
                    find_name=str(input("Enter task owner: "))
                    find_task_name=str(input("Enter task name: "))
                    if update_action=="1":
                        new_change=str(input("Enter the new name: "))
                        update_task(parameter=update_action,value=new_change,name=find_name,task_name=find_task_name)
                    elif update_action=="2":
                        new_change=str(input("Enter the new task name: "))
                        update_task(parameter=update_action,value=new_change,name=find_name,task_name=find_task_name)
                    elif update_action=="3":
                        new_change=str(input("Enter the new category name: "))
                        update_task(parameter=update_action,value=new_change,name=find_name,task_name=find_task_name)
                    elif update_action=="4":
                        new_change=datetime(year=int(input("Year: ")),month=int(input("Month: ")),day=int(input("Day: ")))
                        update_task(parameter=update_action,date_value=new_change,name=find_name,task_name=find_task_name)
                    elif update_action=="5":
                        update_task(parameter=update_action,name=find_name,task_name=find_task_name) 
                else:
                    print("Invalid input..")
                
            
            elif action=="4":
                del_name=str(input("Specify task owner: "))
                del_task_name=str(input("Specify task name: "))
                delete_task(del_name,del_task_name)
            
            elif action=="5":
                perm_username=str(input("Which username to give permission?: "))
                perm_password=str(input("Enter user's password: "))
                a_pass=str(input("Enter admin password: "))
                new_perm=str(input("Enter new task type: "))
                add_premission(username=perm_username,password=perm_password,admin_password=a_pass,value=new_perm)
                
            elif action=="6":
                del_perm_username=str(input("Which username to take permission: "))             
                del_perm_password=str(input("Enter user's password: "))
                del_a_pass=str(input("Enter admin password: "))
                del_perm=str(input("Which premission to take?: "))
                del_premission(username=del_perm_username,password=del_perm_password,admin_password=del_a_pass,value=del_perm)
                
            elif action=="7":
                break
        else:
            print("Invalid input")

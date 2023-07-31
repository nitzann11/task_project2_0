from login_functions import create_user,delete_user,login,update_user,view_user
from user_class import User
def main_menu():
    while True:    
        print("""
            Login menu:
            1.Log in
            2.Create a new account
            3.view user/s
            4.update user
            5.delete user
            6.exit""")
        
        options=("1","2","3","4","5","6")
        action=str(input("choose option:1-6: "))
        if action in options:
            if action=="1":
                login_username=str(input("Enter Username: "))
                login_password=str(input("Enter password: "))
                login( username=login_username , password=login_password)
            
    
            elif action =="2":
                new_name=str(input("enter your name: "))
                new_username=str(input("enter your username: "))
                new_password=str(input("enter your password: "))
                new_email=str(input("enter your email: "))
                create_user(User(name=new_name,username=new_username,password=new_password,email=new_email))


            elif action =="3":
                view_options=("1","2","3","4")
                print('''
                view menu:
                      1.view all users
                      2.view user by name
                      3.view user by username
                      4.view user by premission type''')
                view_action=str(input("choose option 1-4: "))
                if view_action in view_options:
                    if view_action=="1":
                        view_user()
                    elif view_action=="2" or view_action=="3" or view_action=="4":
                        view_value=input("enter filter value: ")
                        view_user(parameter=view_action,value=view_value)
                else:
                    print("invalid input")    
            
            elif action=="4":
                update_options=view_options
                print("""
                update menu:
                      1.update user's name
                      2.update user's username
                      3.update user's password
                      4.update user's email""")
                update_action=str(input("choose update option 1-4: "))
                if update_action in update_options:
                        update_username=str(input("username of the user: "))
                        update_password=str(input("enter user password: "))
                        update_value=str(input("enter the new value: "))
                        update_user(parameter=update_action,username=update_username,password=update_password,value=update_value)
                else:
                    print("invalid input..")
            elif action=="5":
                del_username=str(input("enter the user's username for delete: "))
                del_password=str(input("enter the password of the user for delete: "))
                delete_user(username=del_username,password=del_password)
            elif action=="6":
                exit()
                
        else:
            print("Invalid action, try again..") 
        
if __name__ == '__main__': 
    main_menu()
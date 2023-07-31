class User:
    """This is the class of the user, client can create an user object by providing name, username, password and email. The user will recieve 5 default premissions automatically, and can create tasks using them. For customized tasks user should get more premissions using admin password in the task managment menu."""
    def __init__(self,name:str="undefined",username:str="undefined",password:str="undefined",email:str="undefined",task_premissions:list=["general","cleaning","shopping","work","workout"]):
        self.name=name
        self.username=username
        self.password=password
        self.email=email
        self.task_premissions=task_premissions    
    def __str__(self) -> str:
        return f'"name\t\tusername\t\temail\t\tpremissions"\n\n{self.name}\t\t{self.username}\t\t{self.email}\t\t{self.task_premissions}'


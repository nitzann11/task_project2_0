class User:
    def __init__(self,name:str="undefined",username:str="undefined",password:str="undefined",email:str="undefined",task_premissions:list=["general","cleaning","shopping","work","workout"]):
        self.name=name
        self.username=username
        self.password=password
        self.email=email
        self.task_premissions=task_premissions    
    def __str__(self) -> str:
        return f'"name\t\tusername\t\tpassword\t\temail\t\tpremissions"\n\n{self.name}\t\t{self.username}\t\t{self.email}\t\t{self.task_premissions}'


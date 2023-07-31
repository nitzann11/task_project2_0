from datetime import datetime
class Task:
    def __init__(self,name:str="undefined",task_name:str="undefined",category:str="undefined",creation_date:datetime=datetime.today(),deadline:datetime=datetime.today()):

        self.name=name
        self.task_name=task_name
        self.category=category
        self.creation_date=creation_date
        self.deadline=deadline
        self.time_diffrence=deadline-creation_date
        
    def __str__(self) -> str:
        return f'\n{self.name}\t\t{self.task_name}\t\t{self.category}\t\t{(self.creation_date)}\t\t{(self.deadline)}\t\t{(self.time_diffrence)}'

from pickle import dump,load

def save_data(filename:str="tasks.pickle",data:list=[]):
    """This function serves as the save option in this app its saves data on pickle file."""
    try:
        with open(filename,"wb") as f:
            dump(data,f)
    except:
        print("Oops something went wrong")

def load_data(filename:str="tasks.pickle"):
    """This function reads data out of pickle file so we can use it."""
    try:
        with open(filename,"rb") as f:
            data=load(f)
            return data
    except:
        with open(filename,"wb") as f:
            dump([],f)
            return []
        
        
from pickle import dump,load

def save_data(filename:str="tasks.pickle",data:list=[]):
    try:
        with open(filename,"wb") as f:
            dump(data,f)
    except:
        print("Oops something went wrong")

def load_data(filename:str="tasks.pickle"):
    try:
        with open(filename,"rb") as f:
            data=load(f)
            return data
    except:
        with open(filename,"wb") as f:
            dump([],f)
            return []
        
        
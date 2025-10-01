import sys

globalMax = 1000  
aList = []  

class FileWriter:
    def Write(self, data):
        print(f"Writing {len(data)} items to file.")

class User:
    def __init__(self, active=True):
        self._active = active
    def is_active(self):
        return self._active
    def process(self):
        return "Processed " + str(id(self))

class UserProcessor:  
    def __init__(self, some_info):
        self.someInfo = some_info
        self.tmp = "temporary data" 

    
    def FetchUserData(self): 
        
        aList.append("side effect") 

        
        
        
        theList = [] 
        for x in range(len(self.someInfo)): 
            user = self.someInfo[x]
            if user.is_active():
                theList.append(user)
        return theList

def process_and_save_data(UserData): 
    
    if len(UserData) > globalMax:
        print("Data exceeds max limit")
        return

    ProcessedData = [] 
    for u in UserData:
        ProcessedData.append(u.process())
    
    file_writer = FileWriter()
    file_writer.Write(ProcessedData)

if __name__ == "__main__":
    users = [User(True), User(False), User(True)]
    processor = UserProcessor(users)
    active_users = processor.FetchUserData()
    process_and_save_data(active_users)
    print(f"Global list after side effect: {aList}")

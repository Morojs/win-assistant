from pathlib import Path
import os
class FileProcess() :
    
    def __init__(self,input) :
        self.fileName=input[2]
        #self.filePath=input[3]
        self.isFile = os.path.isfile("./"+input[2]) 
        self.fileType=input[1]
        self.key=input[0]

    def file_key(self,argument): 
        switcher = { 
            "create": "w", 
            "delete": "rm", 
            "make"  : "w", 
            "open"  : "o",
            "read"  : "rd"
        } 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
        return switcher.get(argument, "null") 

    def create(self) :
        if self.fileType=="file" and self.isFile==False :
            with open("./"+self.fileName,self.file_key(self.key)) :
                return True
        else :
            if self.fileType=="folder" and self.isFile==False :
                os.mkdir("./"+self.fileName)
                return True
            else : 
                return False


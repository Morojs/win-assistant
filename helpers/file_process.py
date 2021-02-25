from pathlib import Path
import os,subprocess,platform
class FileProcess() :
    
    def __init__(self,input) :
        self.fileName=input[2]
        #self.filePath=input[3]
        self.isFile = os.path.isfile("./"+input[2]) 
        self.fileType=input[1]
        self.key=input[0]
        self.success=False

    def request_process(self): 
        switcher = { 
            "create": self.create("w"), 
            "delete": self.delete(), 
            "make"  : self.create("w"), 
            "open"  : self.open(),
            "read"  : self.open()
        } 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument
        return switcher.get(self.fileType, self.success) 

    def create(self,mode) :
        if self.fileType=="file" and self.isFile==False :
            with open("./"+self.fileName,mode) :
                self.success=True
        else :
            if self.fileType=="folder" and self.isFile==False :
                os.mkdir("./"+self.fileName)
                self.success=True
        return self.success

    def delete(self) : 
        if self.fileType=="file" or self.fileType=="folder" and self.isFile==False  :
             os.remove("./"+self.fileName)
             self.success=True
        return self.success

    def open(self) : 
        if self.fileType=="file" or self.fileType=="folder" and self.isFile==False  :
            if platform.system() == 'Windows':    # Windows
                os.startfile("./"+self.fileName)
                self.success=True
        return self.success

        

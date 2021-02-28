from pathlib import Path
import os,subprocess as sp,platform ,shutil
class FileProcess() :
    
    def __init__(self,input) :
        #self.filePath=input[3]
        self.key=input[0]
        self.fileType=input[1]
        self.fileName=input[2]
        self.isFile = os.path.isfile(self.fileName) 

    def request_process(self): 
        if self.key in ["create","make"] :
            return self.create("w")
        if self.key=="delete":
            return self.delete()
        if self.key in ["open","read"] :
            return self.open()
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument
        return False

    def create(self,mode) :
        if self.fileType=="file" and self.isFile==False :
            with open(self.fileName,mode) :
                return True
        else :
            if self.fileType=="folder" and self.isFile==False :
                os.mkdir(self.fileName)
                return True
        return False

    def delete(self) : 
        if self.isFile==True :
            os.remove(self.fileName)
            return True
        elif self.fileType=="folder" : 
            shutil.rmtree(self.fileName)
            return True
        return False

    def open(self) : 
        if self.fileType=="file" and self.isFile==True   :
            if platform.system() == 'Windows':    # Windows
                programName = "notepad.exe"
                sp.Popen([programName, self.fileName])
                return True
        else :
            os.startfile(self.fileName)
            return True
        return False

        

"""
Basic of speech recognition grammar
================

"""
from lark import Lark,Token, Transformer, v_args
import numpy as np
import os

"""
[a-zA-Z]    : is for the drive letter and :.
[\\\/]      : to match either \ or /.
(?:[a-zA-Z0-9]+[\\\/])*     : is for folder names. You can add any charcters in the character class that you may need. I used only a-zA-Z0-9.
([a-zA-Z0-9]+\.txt)         : is for the file name - it matches the file name
"""
speech_grammar = """
start              : KEY TYPE FNAME PATH?
KEY                : "create" | "delete" | "open" | "read" | "make" 
TYPE               : "file" | "folder" 
FNAME              : (/[a-z]/)+ 
PATH               : (/[a-zA-Z]/)+":"(/[\\/]/)+DIRNAME
DIRNAME            : ((/[a-zA-Z0-9]/)+(/[\\/]/)?)*

%ignore (" ")+
"""

speech_parser = Lark(speech_grammar)

def file_key(argument): 
    switcher = { 
        "create": "w", 
        "delete": "dlt", 
        "make"  : "w", 
        "open"  : "op",
        "read"  : "rd"
    } 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(argument, "null") 
  
def file_process(inst_arr) :
    if inst_arr[1]=="file" :
        with open("./"+inst_arr[2],file_key(inst_arr[0])) :
            print('file created...')
    else :
        if inst_arr[1]=="folder" :
            os.mkdir("./"+inst_arr[2])
            print('folder created...')

def run(input):
    try:
        speech = speech_parser.parse(input)
        arr=np.array(speech.children)
        file_process(arr)
    except Exception as e :
        print(e)

def main(input):
    return run(input)

def test():
    print(run("make file test d:/test"))
    print(run("delete file test"))


#if __name__ == '__main__':
    # test()
    #main()
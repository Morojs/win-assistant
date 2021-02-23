"""
Basic of speech recognition grammar
================

"""
from lark import Lark,Token, Transformer, v_args
from helpers.file_process import FileProcess
import numpy as np

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

def run(input):
    try:
        speech = speech_parser.parse(input)
        instr=np.array(speech.children)
        return FileProcess(instr).request_process()
    except Exception as err :
        return err

def main(input):
    return run(input)

def test():
    print(run("make file test d:/test"))
    print(run("delete file test"))


#if __name__ == '__main__':
    # test()
    #main()
from lark import Lark
from helpers.file_process  import FileProcess 
from helpers.interaction_process import Interact
from parse.task_grammar  import speech_grammar 
from parse.phrase_grammar import phrase_grammar
import numpy as np

speech_parser = Lark(speech_grammar)
dialog_parser = Lark(phrase_grammar)

def run(input):
    try:
        parse_speech = dialog_parser.parse(input)
        instr=np.array(parse_speech.children)
        return Interact(instr).request_process()
    except Exception as err :
        try :
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
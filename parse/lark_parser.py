from lark import Lark
from helpers.file_process import FileProcess
from parse.lark_grammar import speech_grammar
import numpy as np

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
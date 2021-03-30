from lark import Lark
from helpers.file_process import FileProcess
from helpers.interaction_process import Interact
from parse.task_grammar import task_grammar
import numpy as np

task_parser = Lark(task_grammar)


def run(text):
    try:
        speech = task_parser.parse(text)
        instr = np.array(speech.children)
        return FileProcess(instr).request_process()
    except Exception as err:
        try:
            return Interact(text).request_process()
        except Exception as err:
            return err


def main(input):
    return run(input)


def test():
    print(run("make file test d:/test"))
    print(run("delete file test"))


# if __name__ == '__main__':
# test()
# main()

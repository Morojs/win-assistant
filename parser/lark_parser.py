"""
Basic of speech recognition grammar
================

"""
from lark import Lark, Transformer, v_args

speech_grammar = """
start           : M" "F" "N
M               : "make" | "delete"
F               : "file" | "folder"
N               : (/[a-z]/)+
"""

calc_parser = Lark(speech_grammar)
calc = calc_parser.parse

def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(s))


def test():
    print(calc("make file test"))
    print(calc("delete file test"))


if __name__ == '__main__':
    # test()
    main()
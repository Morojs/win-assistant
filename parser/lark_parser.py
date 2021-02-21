"""
Basic of speech recognition grammar
================

"""
from lark import Lark, Transformer, v_args
"""
[a-zA-Z]    : is for the drive letter and :.
[\\\/]      : to match either \ or /.
(?:[a-zA-Z0-9]+[\\\/])*     : is for folder names. You can add any charcters in the character class that you may need. I used only a-zA-Z0-9.
([a-zA-Z0-9]+\.txt)         : is for the file name - it matches the file name
"""
speech_grammar = """
start              : KEY TYPE FNAME PATH
KEY                : "create" | "delete" | "open" | "read" | "make"
TYPE               : "file" | "folder"
FNAME              : (/[a-z]/)+
PATH               : (/[a-zA-Z]/)+":"(/[\\/]/)+DIRNAME
DIRNAME            : ((/[a-zA-Z0-9]/)+(/[\\/]/)?)*

%ignore (" ")+
"""

speech_parser = Lark(speech_grammar)
speech = speech_parser.parse

def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(speech(s))


def test():
    print(speech("make file test"))
    print(speech("delete file test"))


if __name__ == '__main__':
    # test()
    main()
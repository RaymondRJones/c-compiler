from __future__ import absolute_import
from lexer import *
from parserClass import *
import sys
def main():

    print("Simple Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1],'r') as inputFile:
        input = inputFile.read()

    lex = Lexer(input)
    parser = Parser(lex)
    
    parser.program()
    print("Parsing Completed")
main()
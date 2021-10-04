from lexer import *

def main():
    input = "+- */"
    lex = Lexer(input)
    token = lex.getToken()

    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lex.getToken()
main()
from lexer import *

def main():
    input = "IF+-123 foo*THEN/"
    lex = Lexer(input)
    token = lex.getToken()

    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lex.getToken()
main()
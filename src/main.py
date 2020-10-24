import re
from CST_const_tokens import TOKENS
from CST_Tokenizer import Tokenizer
from parser_states import States

print("cst Parser v0.1")

# in the parse function
# get the source text pass it to the tokenizer.
# build an ast with the tokens
def parse(source_text):
    izer = Tokenizer(source_text, TOKENS)
    return States.start(izer)


# check if the computations in the ast are using the supported types
def type_check_ast(ast):
    pass

def execute(ast): # this will run the code in python
    pass

# translate the ast into an other language
def translate(ast, language):
    pass



# define the read execute print loop
def repl():
    running = True
    while running:
        user_in = input(">")
        if user_in == "quit":
            running = False
        else:
            ast = parse(user_in)
            type_check_ast(ast)
            other_source = translate(ast, "PY")
            execute(ast)

# repl()
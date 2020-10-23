import re

print("cst Parser v0.1")

# in the parse function
# get the source text pass it to the tokenizer.
# build an ast with the tokens
def parse(source_text):
    izer = tokenizer(source_text)



# define the read execute print loop
def repl():
    running = True
    while running:
        user_in = input(">")
        ast = parse(user_in)
        verify_ast(ast)
        execute(ast)

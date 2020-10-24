from main import parse
# contains a couple tests for the parser

# test two comments with whitespace inbetween
ast = parse("""// parse comment line 1
// parse comment line 2
""")

print('AST:', ast)

ast = parse(""" //this is a single line starting comment
//--> starting description
continuing description
ending description <--//
//this will be a single line ending comment
""")

print('AST:', ast)
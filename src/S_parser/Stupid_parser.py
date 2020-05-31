
import Selector
import Option

# regex values for the parser
TAG = "\<[a-zA-Z0-9_]+\>"
COLON = "\:"
LPAREN = "\["
RPAREN = "\]"
COMMA = "\,"
STRING = "\".+?\""

# options for patterns to match
options = []
options.append(Option.Option("Tag", TAG))
options.append(Option.Option("Colon", COLON))
options.append(Option.Option("LParen", LPAREN))
options.append(Option.Option("RParen", RPAREN))
options.append(Option.Option("Comma", COMMA))
options.append(Option.Option("String", STRING))

class Parser:
    def __init__(self, grammar):
        # put the grammar for the parser into a variable
        self.grammar = grammar
        print("creating the parser!")

    # building the parser by the grammar
    def build(self):
        # start parsing the grammar file
        while len(self.grammar) > 0:
            self.selector([])


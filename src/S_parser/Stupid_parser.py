from S_parser.Stup_Option import Option
from S_parser.Stup_Selector import Selector
import re

# MainOptions with patterns to match
MainOptions = []
MainOptions.append(Option("Tag", r"\<([a-zA-Z0-9_]+)\>"))
MainOptions.append(Option("Colon", r"\:"))
MainOptions.append(Option("LBrace", r"\["))
MainOptions.append(Option("RBrace", r"\]"))
MainOptions.append(Option("Comma", r"\,"))
MainOptions.append(Option("String", r"\".+?\""))
MainOptions.append(Option("plus", r"\+"))
MainOptions.append(Option("star", r"\*"))
# the whitespaces for debugging (whitespace after newline)
MainOptions.append(Option("NewLine", r"\n"))
MainOptions.append(Option("Whitespace", r"\s+"))

class Parser:
    def __init__(self, grammar):
        # put the grammar for the parser into a variable
        self.grammar = grammar
        print("creating the parser!")
        self.MainSelector = Selector(MainOptions)
        self.build()
        print("build the parser!")

    # building the parser by the grammar
    def build(self):
        # get all the tokens from the grammar file
        for tok in self.get_Tokens():
            print(tok)
            self.grammar = self.grammar[len(tok):]

    def get_Tokens(self):
        canParse = True
        # start parsing the grammar file
        while len(self.grammar) > 0 and canParse:
            canParse = False
            choiceIndex = self.MainSelector.select(self.grammar)
            # verify the index
            if self.MainSelector.verifyIndex(choiceIndex):
                canParse = True
                # get the matched text from the chosen option
                matched_text = self.MainSelector.options[choiceIndex].match(self.grammar)
                yield matched_text.group(0)
            else:
                # we will have to break out of this loop and see what text does not parse.
                canParse = False
        # could not parse a piece of text
        raise SyntaxError("The grammar file could not be read correctly. error on:'{}'".format(self.grammar))

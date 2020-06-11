# general imports
import re

# tokenizer imports
from S_parser.Tokenizer.Stup_Option import Option
from S_parser.Tokenizer.Stup_Selector import Selector
from S_parser.Tokenizer.Token import Token
# imports for the ast
from S_parser.Tree.Stup_Token_Selector import TokenSelector

# DEBUG FLAGS
DebugShowTokens = True

# MainOptions with patterns to match
MainOptions = []
MainOptions.append(Option("Tag", r"\<([a-zA-Z0-9_]+)\>", 1))
MainOptions.append(Option("String", r'"(?:[^"\\]|\\.)*"'))
MainOptions.append(Option("Regex", r"R/(.+?)\/R", 1))
MainOptions.append(Option("Colon", r"\:"))
MainOptions.append(Option("SemiColon", r"\;"))
MainOptions.append(Option("LBrace", r"\["))
MainOptions.append(Option("RBrace", r"\]"))
MainOptions.append(Option("Comma", r"\,"))
MainOptions.append(Option("plus", r"\+"))
MainOptions.append(Option("star", r"\*"))

# the whitespaces for debugging (whitespace after newline)
MainOptions.append(Option("NewLine", r"\n"))
MainOptions.append(Option("Whitespace", r"\s+"))

class Parser:
    # give the grammar to the parser.
    # the default entrypoint
    def __init__(self, grammar, entry_point="start"):
        # put the grammar for the parser into a variable
        self.grammar = grammar
        self.grammar_text = grammar
        # keep track of where I am inside the grammar
        self.line = 1
        self.index = 0
        print("creating the parser!")
        self.MainSelector = Selector(MainOptions)
        # start building the grammar for my parser
        toks = self.Grammar_to_tokens()
        print("build the parser! from text:")
        print(self.grammar_text)
        self.Meta_Selector = TokenSelector(toks, entry_point)

    # get the tokens from the grammar file
    def Grammar_to_tokens(self):
        # get all the tokens from the grammar file
        tokens = []
        for tok in self.get_Tokens():
            if tok[1].name == "NewLine":
                self.line += 1
                self.index = 0
            else:
                # update the location after setting the token
                if tok[1].name != "Whitespace":
                    tok[1].setLocation(self.line, self.index)
                    tokens.append(tok)
                # add the length of the token to the index
                self.index += len(tok[0])

            # tok[0] is the full matched string.
            # tok[1] is the token that get's made
            self.grammar = self.grammar[len(tok[0]):]

        # now that we have the tokens we only keep the token object
        tokens = [tok[1] for tok in tokens]
        if DebugShowTokens:
            # show the tokens
            for tok in tokens:
                print(tok)
        return tokens

    # private function that returns the tokens
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
                yield [matched_text.group(0), Token(self.MainSelector.options[choiceIndex].name, matched_text.group(self.MainSelector.options[choiceIndex].group))]
            else:
                # we will have to break out of this loop and see what text does not parse.
                canParse = False
        if len(self.grammar) > 0:
            # could not parse a piece of text
            print("length of text is:'{}'".format(len(self.grammar)))
            raise SyntaxError("The grammar file could not be read correctly. error on:'{}'".format(self.grammar))
        else:
            print("grammar tokenized succesfully")
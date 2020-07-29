from .Tokenizer.Tokenizer import Tokenizer
from .Tokenizer.Data.TokenQuery import TokenQuery

# queries for the tokenizer used in the grammar
def get_grammar_queries():
    return [
        TokenQuery("Tag", r"^(<[a-zA-Z_]\w*?>)"),
        TokenQuery("Colon", r":"),
        TokenQuery("SemiColon", r";"),
        TokenQuery("NewLine", r"\n"),
        TokenQuery("Whitespace", r"\s+"),
        TokenQuery("String", r"\"([^\\\"]|\\\"|\\)*\"")
    ]

class Parser:
    def __init__(self, _grammar, _entryPoint="start"):
        self.grammar = _grammar
        self.entryPoint = _entryPoint
        self.grammarTokenizer = Tokenizer(get_grammar_queries())

        self.tokens = self.extractTokensFromGrammar()
        print("print the tokens from the grammar:")
        print(self.tokens)

    def extractTokensFromGrammar(self):
        return self.grammarTokenizer.getTokenList(self.grammar)

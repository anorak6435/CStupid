from .Tokenizer.Tokenizer import Tokenizer
from .Tokenizer.Data.TokenQuery import TokenQuery
from .GrammarSyntax.GrammarAnalyser import GrammarAnalyser

# queries for the tokenizer used in the grammar
def get_grammar_queries():
    return [
        TokenQuery("Tag", r"^(<[a-zA-Z_]\w*?>)"),
        TokenQuery("Colon", r":"),
        TokenQuery("SemiColon", r";"),
        TokenQuery("NewLine", r"\n"),
        TokenQuery("Whitespace", r"\s+"),
        TokenQuery("Or", r"\|"),
        TokenQuery("String", r"\"([^\\\"]|\\\"|\\)*\"")
    ]

class Parser:
    def __init__(self, _grammar, _entryPoint="start"):
        self.grammar = _grammar
        self.entryPoint = _entryPoint
        self.grammarTokenizer = Tokenizer(get_grammar_queries())

        self.tokens = self.extractTokensFromGrammar()
        # filter the whitespace from the tokens
        self.tokens = [token for token in self.tokens if self.notWhitespaceOrNewLine(token)]
        print("print the tokens from the grammar:")
        print(self.tokens)

        GrammarAlyser = GrammarAnalyser(self.tokens)
        rules = GrammarAlyser.fetchRules()
        # wait until after I get all the rules then I can compile them because rules could
        # reference other rules that are further down in the grammar file.
        print("rules:")
        for rule in rules:
            print(rule)

    def extractTokensFromGrammar(self):
        return self.grammarTokenizer.getTokenList(self.grammar)

    # check if a token is not a Whitespace
    def notWhitespaceOrNewLine(self, token):
        return token.name != "Whitespace" and token.name != "NewLine"
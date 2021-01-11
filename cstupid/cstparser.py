from cstupid.data_objects.cstast import VarDeclar, CNumber, Node
from cstupid.data_objects.cstrule import Rule, Tag
from cstupid.data_objects.csttoken import Token
from typing import List, Iterator, Callable, Optional

class Parser:
    def __init__(self, defined_rules : List[Tag]) -> None:
        # keep track of what rules are defined in the parser
        self.defined_rules = defined_rules

    # choose one of the Tags in the given list
    def choose(self, tags : List[Tag], in_string : str) -> Optional[Tag]:
        Chose : Optional[Tag] = None
        for tag in tags:
            if tag.canParse(in_string):
                Chose = tag
                break

        return Chose


    # create a tree from the stream of tokens given. using the rules we defined
    def parse(self, stream : Iterator[Token]) -> List[Node]:
        # keep track of what tag I am trying to resolve
        pass

# will listen for the state changes inside of the 
class ParserGenerator:
    def __init__(self) -> None:
        # contains the tags of rules I would like the parser to deal with
        self.rules : List[Tag] = []
        # expected rules for a grammar rule
        self.rule_grammar = [Rule("rule_name", r"[a-zA-Z]\w*"), Rule("colon", ":")]
        # the grammar matcher that matches if the grammar rule given inside the self.add function is complete
        # self.ruleMatcher : GrammarMatcher = GrammarMatcher(rule_tags)
    
    # add a rule to the parser generator it should follow
    # the rule should show the relation between the rules I want to make
    def add(self, rule : str) -> None:
        rule_list = rule.split()
        grammarIndex : int = 0
        while grammarIndex < len(self.rule_grammar):
            grammar_tag = self.rule_grammar[grammarIndex]
            assert grammar_tag.canParse(rule_list[grammarIndex]), f"ParserGenerator could not parse string: '{rule_list[grammarIndex]}' in rule: '{rule}' expected: '{grammar_tag}'"
            
            grammarIndex += 1
            

        




pg = ParserGenerator()

# @pg.production("main : statements")
# def statements(s):
#     return s[0]

# @pg.production("statements : statement statements")
# def some_statement(s):
#     return s[0]

# @pg.production("statements : statement")
# def handle_single_statement(s):
#     return s[0]

# @pg.production("statement : expr ")
# def expression(s):
#     return s[0]

# @pg.production("expr : VARKEY IDENTIFIER IDENTIFIER ASSIGN expr SEMICOLON")
# def vardeclar(s):
#     return VarDeclar(s[1], s[2], s[4])

# @pg.production("expr : NUMBER")
# def handle_number_expression(s):
#     return CNumber(s[0])

# @pg.error
# def error_handler(token):
#     raise ValueError("Ran into a %s where it was't expected" % token.gettokentype())
# Parser = pg.build()
import re

from cstupid.data_objects.cstrule import TokenRule
from cstupid.data_objects.csttoken import Token
from cstupid.cst_const_tokens import TT_NEWLINE

from typing import Iterator, List, Optional, Tuple

class Lexer:
    def __init__(self, rules : List[TokenRule], ignore_rules : List[TokenRule]) -> None:
        self.rules = rules
        self.ignores = ignore_rules
        # self.previousTokens : List[Token] = [] # a list containing the previous tokens from the lexer
        self.tokens : List[Tuple[Token, int, int]] = []
        # keep track of what line I am on inside the source text
        self.src_line = 1
        # keep track of what index I am on inside the source text
        self.src_idx = 0

    def match(self, rule : TokenRule, input_string : str) -> Tuple[Optional[Token], str]:
        m = re.match(rule.pattern, input_string)
        if isinstance(m, re.Match):
            input_string = input_string[len(m[0]):]
            return (Token(rule.name, m[0]), input_string)
        else:
            return (None, input_string)

    def lex(self, input_string : str) -> List[Tuple[Token, int, int]]:
        can_parse : bool = True
        self.tokens = []
        while can_parse and len(input_string) > 0:
            can_parse = False
            ignore_index : int = 0
            while ignore_index < len(self.ignores):
                tok, input_string = self.match(self.ignores[ignore_index], input_string)
                if tok:
                    can_parse = True
                    if tok.name == TT_NEWLINE:
                        self.src_idx = 0
                        self.src_line += 1
                    else:
                        self.src_idx += len(tok.value)
                    ignore_index = len(self.ignores)
                    # I won't yield a token here because these tokens have to be ignored
                ignore_index += 1

            # only if none of the self.ignores tokens have been found the Lexer will check the self.rules tokens
            if not can_parse:
                rule_index : int = 0
                while rule_index < len(self.rules):
                    tok, input_string = self.match(self.rules[rule_index], input_string)
                    if tok:
                        can_parse = True
                        rule_index = len(self.rules)
                        # self.previousTokens.append(tok) # add the token to the list of previous tokens
                        # # keep the previous tokens at a length of 5 (arbitrary) for memory
                        # if len(self.previousTokens) > 5:
                        #     self.previousTokens = self.previousTokens[-5:]
                        self.tokens.append((tok, self.src_idx, self.src_line))
                        self.src_idx += len(tok.value)
                    rule_index += 1
        if len(input_string) > 0:
            raise Exception(f"The lexer could not parse the full input! It is stuck on:'{input_string}'")
        return self.tokens
            


class LexerGenerator:
    def __init__(self):
        self.rules : List[TokenRule] = []
        self.ignores : List[TokenRule] = []

    # add a rule to the lexer generator it should follow
    def add(self, rule_name : str, rule_pattern : str) -> None:
        self.rules.append(TokenRule(rule_name, rule_pattern))

    # add a rule to the lexer generator it should ignore
    def ignore(self, rule_name : str, rule_pattern : str) -> None:
        self.ignores.append(TokenRule(rule_name, rule_pattern))

    # build the Lexer from the rules we want_to_use
    def build(self) -> Lexer:
        return Lexer(self.rules, self.ignores)
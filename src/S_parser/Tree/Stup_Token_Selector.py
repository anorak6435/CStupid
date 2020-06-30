import re
from S_parser.Tree.Stup_Rule import Rule
# this class will select the tokens to make an ast
class TokenSelector:
    def __init__(self, toks, entryPoint):
        self.rules = [] # a list of rules we found
        self.tokenIndex = 0 # the tokenIndex
        self.tokens = toks
        self.entryPoint = entryPoint
        # creating the tree
        self.tree = self.select()

    # match a token name It can not be anything else
    def expect_match_id(self, option):
        if self.tokenIndex >= len(self.tokens):
            raise SyntaxError("There are no more tokens to match the:'{}'\nYou Probably have to add text to the end of the grammar!".format(option))
        assert self.tokens[self.tokenIndex].name == option, "Tree builder expected a:{}\nBut got token:{}".format(option, self.tokens[self.tokenIndex])
        print("got Token!! by -> {}".format(option))
        return self.tokens[self.tokenIndex]

    # match a name agains possible options for that location
    def maybe_value(self, options, option):
        if self.tokenIndex >= len(self.tokens):
            raise SyntaxError("There are no more tokens to match an option:{}\nYou Probably have to add text to the end of the grammar!".format(options))
        if re.match(option, self.tokens[self.tokenIndex].name):
            return self.tokens[self.tokenIndex]
        else:
            return False

    # get's a list of options and see if one returns a value else return False
    def maybe_options(self, options):
        for option in options:
            if self.maybe_value(options, option):
                print("got option!! by -> {}".format(option))
                return self.maybe_value(options, option)

        return False
        # if none of the options match we throw a syntax error
        # raise SyntaxError("Tree builder could not match token out of:{}\nThe given token was:{}".format(options, self.tokens[self.tokenIndex]))

    def nextRule(self):
        # start on index 0
        self.tokenIndex = 0
        # I first expect a tag
        next_rule = Rule(self.expect_match_id("Tag"))
        self.tokenIndex += 1
        # the separator is the colon that token does not have to be stored
        self.expect_match_id("Colon")
        self.tokenIndex += 1

        rule_body = ["Tag", "String", "Regex", "LBrace", "RBrace", "Comma", "Plus", "Star"]
        # multiple options for the next part of the grammar.
        token = self.maybe_options(rule_body)
        while token and token.name != "SemiColon":
            next_rule.add_token(token)
            # get the next token
            self.tokenIndex += 1
            token = self.maybe_options(rule_body)

        # when out of the loop I expect an semicolon as the rule
        self.expect_match_id("SemiColon")
        self.tokenIndex += 1
        # if there are tokens left the parser expects there to be more tokens
        print("next_rule:")
        print(next_rule)
        # get the remaining tokens
        self.tokens = self.tokens[self.tokenIndex:]
        return next_rule

    def select(self):
        while len(self.tokens) > 0:
            self.rules.append(self.nextRule())

        print("Rules are found!")
        print(self.rules)
        if len(self.tokens) > 0:
            print("there were tokens left!")
            raise SyntaxError(self.tokens)
        print("Compile the rules:")
        # when there are lists of optional values
        # the syntax is partially checked again when compiling the tokens
        for i in range(len(self.rules)):
            self.rules[i].compile()

        print("after compilation!")
        for rule in self.rules:
            print(rule)
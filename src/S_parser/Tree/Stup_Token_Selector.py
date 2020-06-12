from S_parser.Tree.Stup_Gmatch import Goption
# this class will select the tokens to make an ast
class TokenSelector:
    def __init__(self, toks, entryPoint):
        self.rules = [] # a list of rules we found
        self.tokenIndex = 0 # the tokenIndex
        self.tokens = toks
        self.entryPoint = entryPoint
        self.rule_declar = [Goption("name", "Tag"), Goption("name", "SemiColon")]
        # creating the tree
        self.tree = self.select()

    def select(self):
        Found = True
        # when going through one iteration of the loop we will have found a rule.
        while Found:
            Found = False
            # track the index of the rule_declar
            ruleIndex = 0
            temp_tokens = []
            # check for rule declarations
            match = True
            while match:
                match = False
                if self.rule_declar[ruleIndex].selector == "name":
                    match = self.tokens[self.tokenIndex].match_name(self.rule_declar[ruleIndex].value)
                    # add tokens to the temporary storage to use in the declaration
                    temp_tokens.append(self.tokens[self.tokenIndex])
                elif self.rule_declar[ruleIndex].selector == "value":
                    match = self.tokens[self.tokenIndex].match_value(self.rule_declar[ruleIndex].value)
                # check if this part of the Grammar did match:
                if not match:
                    # did not match
                    raise SyntaxError("There was a mismatch in the grammar at:'{}'".format(self.rule_declar[ruleIndex]))
                # advance the rule an the tokenIndex
                ruleIndex += 1
                self.tokenIndex += 1
                if ruleIndex == len(self.rule_declar):
                    # make the declaration and add to self.rules
                    print("found a rule!")

    # check tokens against a checklist    
    def checklist(self, checklist):
        pass

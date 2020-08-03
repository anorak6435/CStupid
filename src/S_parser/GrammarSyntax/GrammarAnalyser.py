from .Data.Rule import Rule

class GrammarAnalyser: # syntax analyser
    def __init__(self, tokens):
        self.expectAnalyser = "Analyser Expected an {} in grammar on line:{} index: {}. Instead got:{}"
        self.tokens = tokens
        self.tokenIndex = 0
        self.tokenNameOptions = ["Tag", "String", "Or"]
        self.tokenNameOptionsNotOr = [op for op in self.tokenNameOptions if op != "Or"]
        
    def fetchRules(self):
        foundRules = []
        # check if there is at least one more token that is not yet parsed
        while self.tokenIndex < len(self.tokens)-1:
            # start checking for the rules in the tokens
            foundRules.append(self.validRuleInTokens())
        
        return foundRules

    # possibility to skip a token 
    def advanceToken(self, offset=1):
        self.tokenIndex += offset
        if self.tokenIndex >= len(self.tokens):
            raise SyntaxError("Missing the semicolon on the last rule")

    # this function returns a rule it found
    def validRuleInTokens(self):
        if self.tokenIndex > 0:
            self.advanceToken()
        # a rule must start with a Tag token This is the name of the rule
        returnRule = Rule(self.expectTokenName("Tag"))
        self.advanceToken()
        self.expectTokenName("Colon")
        self.advanceToken()
        while self.maybeTokenNameInList(self.tokenNameOptions):
            returnRule.addBodyElement(self.maybeTokenNameInList(self.tokenNameOptions))
            self.advanceToken()
            # if the last match was an or token the Analyser expects an not or token in the rule body
            if returnRule.body[-1].name == "Or":
                if self.expectTokenNameInList(self.tokenNameOptionsNotOr):
                    returnRule.addBodyElement(self.expectTokenNameInList(self.tokenNameOptionsNotOr))
                    self.advanceToken()
            
        self.expectTokenName("SemiColon")
        return returnRule

    # maybe the tokenName is in this list if not return None
    def maybeTokenNameInList(self, valueList):
        NoValueFound = True
        valueListIndex = 0
        returnValue = True
        while NoValueFound:
            NoValueFound = False
            if not self.tokens[self.tokenIndex].name == valueList[valueListIndex]:
                NoValueFound = True
                valueListIndex += 1
                if valueListIndex >= len(valueList):
                    returnValue = False
                    NoValueFound = False
        if returnValue:
            return self.tokens[self.tokenIndex]
        else:
            return False

    # expect the tokenName in this list if not raise error
    def expectTokenNameInList(self, valueList):
        NoValueFound = True
        valueListIndex = 0
        returnValue = True
        while NoValueFound:
            NoValueFound = False
            if not self.tokens[self.tokenIndex].name == valueList[valueListIndex]:
                NoValueFound = True
                valueListIndex += 1
                if valueListIndex >= len(valueList):
                    returnValue = False
                    NoValueFound = False
        if returnValue:
            return self.tokens[self.tokenIndex]
        else:
            raise SyntaxError("Grammar analyser expected one of these values:'{}' At line:'{}' index:'{}'. Instead got:{}".format(valueList, self.tokens[self.tokenIndex].line, self.tokens[self.tokenIndex].index, self.tokens[self.tokenIndex]))


    # expect the token.name to be a value if true return token
    def expectTokenName(self, value):
        assert self.tokens[self.tokenIndex].name == value, self.expectAnalyser.format(value, self.tokens[self.tokenIndex].line, self.tokens[self.tokenIndex].index, self.tokens[self.tokenIndex].name)
        return self.tokens[self.tokenIndex]
class Rule:
    def __init__(self, name):
        self.name = name # the Tag token with the name of the rule
        self.tokens = [] # A list of the tokens that are part of this rule
        self.reg_string = "" # A matchable string from the rules tokens

    # setup the rule for the user the
    def add_token(self, tok):
        self.tokens.append(tok)

    # compile the rules tokens into a string for regex
    def compile(self):
        print("compiling rule:'{}'".format(self.name))
        tokIndex = 0
        if self.tokens[tokIndex].name == "LBrace":
            tokIndex += 1
            optionList = []
            while self.tokens[tokIndex].name != "RBrace" and tokIndex < len(self.tokens):
                optionList.append(self.tokens[tokIndex])
                tokIndex += 1
            print("done with the options!")

        self.reg_string
    
    def __repr__(self):
        return "R(name:{}, toks:{}, String:{})".format(self.name, self.tokens, self.reg_string)
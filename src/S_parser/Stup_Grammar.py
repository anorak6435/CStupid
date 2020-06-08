class Grammar:
    def __init__(self, name, options):
        # list of the options that make up this gramatical rule
        self.name = name
        self.options = options

    def match(self, tokStream):
        # if the name of the expected option is the name of the token then we are good
        if self.options[0].name_match(tokStream[0].name):


    def __repr__(self):
        return "G({}:{})".format(self.name, self.options)

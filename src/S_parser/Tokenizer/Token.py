class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.line = 0
        self.index = 0

    def setLocation(self, line, index):
        self.line = line
        self.index = index

    def match_name(self, other):
        return other == self.name

    def match_value(self, other):
        return re.match(other, self.value)


    def __repr__(self):
        return "T({0}:{1}, L:{2}, i:{3})".format(self.name, self.value, self.line, self.index)

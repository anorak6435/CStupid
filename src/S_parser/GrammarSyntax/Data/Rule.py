class Rule:
    def __init__(self, _name):
        self.name = _name
        self.body = []

    # add an element to the body of the rule
    def addBodyElement(self, element):
        self.body.append(element)

    def __repr__(self):
        return "<Rule name:{}, body:{}/>".format(self.name, self.body)
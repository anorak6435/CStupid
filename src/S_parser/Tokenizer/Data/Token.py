class Token:
    def __init__(self, _name, _value, _line, _index, _fullMatch):
        self.name = _name
        self.value = _value
        self.line = _line
        self.index = _index
        self.fullMatch = _fullMatch

    def __repr__(self):
        return "<Token {}:{}, line:{}, index:{}/>".format(self.name, repr(self.value), self.line, self.index)
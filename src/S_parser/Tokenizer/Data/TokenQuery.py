class TokenQuery:
    def __init__(self, _tokenType, _value, _group=0):
        self.matchType = _tokenType
        self.matchValue = _value
        self.matchGroup = _group

    def getValue(self):
        return self.matchValue

    def getTokenType(self):
        return self.matchType
# the token object:
# this object is used to define what strings will be put into tokens and
# store strings in tokens.

class Token(object):
    def __init__(self, tok_type, value):
        self.tok_type = tok_type
        self.value = value

    def __repr__(self):
        return f"tok({self.tok_type}:{repr(self.value)})"

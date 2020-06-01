import re
# the options like rules for the grammar parser.

class Option:
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern

    # match the pattern to text.
    def match(self, raw):
        return re.match(self.pattern, raw)

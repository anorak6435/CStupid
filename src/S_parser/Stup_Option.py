import re
# the options like rules for the grammar parser.

class Option:
    def __init__(self, name, pattern=None, group=0):
        self.name = name
        self.pattern = pattern
        # the group I'm matching to will have a default of 0 unless defined
        self.group = group

    # match the pattern to text.
    def match(self, raw):
        return re.match(self.pattern, raw)

# a grammar object

# selector = name or value
# value = value to check against
class Goption:
    def __init__(self, _selector, val):
        self.selector = _selector
        self.value = val

    def __repr__(self):
        return "select:'{}' with value:'{}'".format(self.selector, self.value)

class Selector:
    def __init__(self, options):
        # the different options for the selector
        self.options = options

    # return the index of the first matched object.
    #   else return -1
    def select(self, raw):
        for x in range(len(self.options)):
            if self.options[x].match(raw):
                return x
        return -1
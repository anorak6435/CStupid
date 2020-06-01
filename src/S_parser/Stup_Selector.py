class Selector:
    def __init__(self, options):
        # the different options for the selector
        self.options = options

    # return the index of the first matched object.
    #   else return -1
    def select(self, raw):
        ret_val = -1
        for x in range(len(self.options)):
            if self.options[x].match(raw):
                ret_val = x
                break
        return ret_val

    # check that this number is inside the options range
    def verifyIndex(self, index):
        return index >= 0 and index < len(self.options)
class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return "T({0}:{1})".format(self.name, self.value)
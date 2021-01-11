# contains the Nodes of the syntax tree

class Node(object):
    pass

class VarDeclar(Node):
    def __init__(self, vartype, varname, value):
        self.type = vartype.getstr()
        self.name = varname.getstr()
        self.value = value

    def __repr__(self):
        return f"(VARDECLAR {self.type}:{self.name} := {self.value})"

class CNumber(Node):
    def __init__(self, value):
        self.value = int(value.getstr())

    def __repr__(self):
        return f"(CNumber {self.value})"
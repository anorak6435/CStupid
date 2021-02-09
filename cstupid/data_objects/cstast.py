# contains the Nodes of the syntax tree

class Node(object):
    pass

class VarDeclar(Node):
    def __init__(self, vartype, varname, value):
        self.type = vartype.value
        self.name = varname.value
        self.value = value

    def __repr__(self):
        return f"(VARDECLAR {self.type}:{self.name} := {self.value})"

class Output(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"(OUTPUT '{self.value}')"

class CLink(Node): # link to another part in the code
    def __init__(self, name):
        self.name = name.value
    
    def __repr__(self):
        return f"(CLINK '{self.name}')"

class CNumber(Node):
    def __init__(self, value):
        self.value = int(value.value)

    def __repr__(self):
        return f"(CNumber {self.value})"

class CString(Node):
    def __init__(self, value):
        self.value = str(value.value)
    
    def __repr__(self):
        return f"(CString {self.value})"
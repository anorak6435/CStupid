# contains the Nodes of the syntax tree

class Node(object):
    pass

class VarDeclar(Node):
    def __init__(self, vartype : str, varname : str, value : Node):
        self.type = vartype
        self.name = varname
        self.value = value

    def __repr__(self):
        return f"(VARDECLAR {self.type}:{self.name} := {self.value})"

class BinOp(Node):
    def __init__(self, operation : Node, left : Node, right : Node):
        self.op = operation
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"(BinOp {self.op} {self.left}, {self.right})"

class Comment(Node):
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"(COMMENT '{self.text}')"

class Output(Node):
    def __init__(self, to_print : Node):
        self.to_print = to_print # the value the node has to print

    def __repr__(self):
        return f"(OUTPUT '{self.to_print}')"

class CLink(Node): # link to another part in the code
    def __init__(self, name):
        self.name = name.value
    
    def __repr__(self):
        return f"(CLINK '{self.name}')"

class CBoolean(Node):
    def __init__(self, value : str):
        self.value = value

    def __repr__(self):
        return f"(CBoolean {self.value})"

class CNumber(Node):
    def __init__(self, value : str):
        self.value = int(value)

    def __repr__(self):
        return f"(CNumber {self.value})"

class CString(Node):
    def __init__(self, value : str):
        self.value = value
    
    def __repr__(self):
        return f"(CString {self.value})"
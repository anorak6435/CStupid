
# run the code for the parser.
from S_parser.Stupid_parser import Parser

grammar = '''<start> : [<echo>, <if>, <class>, <function>]+
<echo> : "\(" "echo" <string> ")"
<id> : "\w+"
<string> : '\"[^\"]+\"'
'''

p = Parser(grammar)
# run the code for the parser.
from S_parser.Stupid_parser import Parser

testGrammar = '''<start> : <echo> | <setVar>;
<echo> : "echo" <int>;
<identifier> : "[a-zA-Z_]\w*";
<int> : "[0-9]+";
<setVar> : "var" <type> <identifier> ":=" <int>;
'''

p = Parser(testGrammar)
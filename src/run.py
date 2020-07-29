# run the code for the parser.
from S_parser.Stupid_parser import Parser

testGrammar = '''<start> : <echo>;
<echo> : "echo" "[a-zA-Z_]\w*";
'''

p = Parser(testGrammar)
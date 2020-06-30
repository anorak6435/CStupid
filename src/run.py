# run the code for the parser.
from S_parser.Stupid_parser import Parser

# grammar = '''<start> : [<echo>, <if>, <class>, <function>]+;
# <echo> : "\(" "echo" <string> "\)";
# <id> : R/\w+/R;
# <string> : R/\".+?\"/R;
# '''

testG = '''<start> : [<echo>, <math>];
<echo> : "\(" "echo" "\)";
<math> : "(" ["+", "-", "*", "/"] <number> <number> ")";
<number> : R/\d+/R;
'''
# building the parser based on the grammar
p = Parser(testG)
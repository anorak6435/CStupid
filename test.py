# test all parts of the project

from cstupid.cstlexer import LexerGenerator, Lexer
from cstupid.cstparser import Parser
from cstupid.data_objects.cstrule import TokenRule
from cstupid.data_objects.cstast import VarDeclar, CString, CNumber, Comment, Node, Output
from cstupid.cst_const_tokens import *
import unittest

#############
# test data objects
#############

class TestTokenRule(unittest.TestCase):
    def test_variable_token_rule(self):
        rule = TokenRule("VARKEY", "var")
        self.assertIsInstance(rule, TokenRule)

    # check if the correct data was given to the Tokenrule
    def test_variable_data(self):
        rule = TokenRule("VARKEY", "var")
        self.assertEqual(rule.name, "VARKEY")
        self.assertEqual(rule.pattern, "var")

# the different parts of the abstract syntax tree
class TestAst(unittest.TestCase):
    def test_String_Vardeclar(self):
        node = VarDeclar("String", "Name", CString("Anorak"))
        self.assertIsInstance(node, Node)
    
    def test_Comment(self):
        node = Comment("// example of a comment")
        self.assertIsInstance(node, Node)

    def test_String_Output(self):
        node = Output(CString("Hello world!"))
        self.assertIsInstance(node, Node)
        self.assertIsInstance(node.to_print.value, str)

    def test_Int_Output(self):
        node = Output(CNumber("20"))
        self.assertIsInstance(node, Node)
        self.assertIsInstance(node.to_print.value, int)


#############
# test structures
#############

class TestLexerGenerator(unittest.TestCase):
    def test_create_lexer_generator(self):
        lg = LexerGenerator()
        self.assertIsInstance(lg, LexerGenerator)

    def test_add_rule_to_lexer_generator(self):
        lg = LexerGenerator()
        lg.add("VAR_KEY", "var")
        self.assertTrue(len(lg.rules) == 1)

    def test_add_rule_to_ignore(self):
        lg = LexerGenerator()
        lg.ignore("WHITESPACE",r"\s+")
        self.assertTrue(len(lg.ignores) == 1)

    def test_make_lexer_from_object(self):
        lg = LexerGenerator()
        lg.ignore(TT_NEWLINE, "\n")
        lg.ignore(TT_WHITESPACE, r"\s+")
        lg.add(TT_VARKEY, "var")
        lg.add(TT_ECHOKEY, "echo")
        lg.add(TT_ASSIGN, "=")
        lg.add(TT_NUMBER, r"\d+")
        lg.add(TT_LPAREN, "\(")
        lg.add(TT_RPAREN, "\)")
        lg.add(TT_SEMICOLON, ";")
        lg.add(TT_COLON, ":")
        lg.add(TT_STRING, "\".+?\"")
        lg.add(TT_COMMENT, r"//[^\n]*")
        lg.add(TT_IDENTIFIER, r"[a-zA-Z_][a-zA-Z0-9_]*")

        lexer_obj = lg.build()
        self.assertIsInstance(lexer_obj, Lexer) 

# TODO: parser generator


#############
# test example usages
#############

class TestStoriesWorkingExamples(unittest.TestCase):
    def setUp(self):
        lg = LexerGenerator()
        lg.ignore(TT_NEWLINE, "\n")
        lg.ignore(TT_WHITESPACE, r"\s+")
        lg.add(TT_VARKEY, "var")
        lg.add(TT_ECHOKEY, "echo")
        lg.add(TT_ASSIGN, "=")
        lg.add(TT_LPAREN, "\(")
        lg.add(TT_RPAREN, "\)")
        lg.add(TT_SEMICOLON, ";")
        lg.add(TT_COLON, ":")
        lg.add(TT_PLUS, "\+")
        lg.add(TT_MINUS, "-")
        lg.add(TT_PRODUCT, "\*")
        lg.add(TT_NUMBER, r"\d+")
        lg.add(TT_STRING, "\".+?\"")
        lg.add(TT_COMMENT, r"//[^\n]*")
        lg.add(TT_BOOLEAN, "(true)|(false)")
        lg.add(TT_IDENTIFIER, r"[a-zA-Z_][a-zA-Z0-9_]*")
        self.lexer = lg.build()
        self.parser = Parser()

    def test_one_comment_program(self):
        code = """//make one comment to parse"""
        ast = self.parser.parse(self.lexer.lex(code))

        self.assertEqual(len(ast), 1)
        self.assertIsInstance(ast[0], Comment)

    def test_two_comment_program(self):
        code = """//the first comment
        //the second comment"""
        ast = self.parser.parse(self.lexer.lex(code))

        self.assertEqual(len(ast), 2)
        for node in ast: # check that every node is a Comment
            self.assertIsInstance(node, Comment)

    def test_one_string_variable_program(self):
        code = """var name : String = "Anorak";
        """
        ast = self.parser.parse(self.lexer.lex(code))

        self.assertEqual(len(ast), 1)
        self.assertIsInstance(ast[0], VarDeclar)

    def test_one_int_variable(self):
        code = """var age : Int = 20;
        """
        ast = self.parser.parse(self.lexer.lex(code))
        self.assertEqual(len(ast), 1)
        self.assertIsInstance(ast[0], VarDeclar)

    def test_one_bool_variable(self):
        code = """var overFifty : Bool = false;
        """
        ast = self.parser.parse(self.lexer.lex(code))
        self.assertEqual(len(ast), 1)
        self.assertIsInstance(ast[0], VarDeclar)

    def test_one_int_math_variable(self):
        code = """var sum : Int = 15 + 5;
        """
        ast = self.parser.parse(self.lexer.lex(code))
        self.assertEqual(len(ast), 1)
        self.assertIsInstance(ast[0], VarDeclar)
        self.assertEqual(ast[0].name, "sum")
        self.assertEqual(ast[0].type, "Int")
        self.assertIsInstance(ast[0].value, Node)

    def test_two_variable_program(self):
        code = """var isWorking : Bool = true;
        var product : Int = 15 * 12;
        """
        ast = self.parser.parse(self.lexer.lex(code))

        self.assertEqual(len(ast), 2)
        self.assertIsInstance(ast[0], VarDeclar)
        self.assertEqual(ast[0].type, "Bool")
        self.assertIsInstance(ast[1], VarDeclar)
        self.assertEqual(ast[1].type, "Int")
        
    def test_one_string_echo_program(self):
        code = """echo("Hello world!");
        """
        ast = self.parser.parse(self.lexer.lex(code))
        self.assertEqual(len(ast), 1)
        self.assertIsInstance(ast[0], Output)

    def test_two_string_echo_program(self):
        code = """echo("first string!");
        echo("check second string working??");
        """
        ast = self.parser.parse(self.lexer.lex(code))
        self.assertEqual(len(ast), 2)
        self.assertIsInstance(ast[0], Output)
        self.assertIsInstance(ast[1], Output)

if __name__ == "__main__":
    unittest.main()
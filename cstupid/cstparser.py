from cstupid.data_objects.cstast import Comment, VarDeclar, Output, CNumber, Node, CString, CLink, CBoolean, BinOp
from cstupid.data_objects.cstrule import TokenRule, GrammarNode
from cstupid.data_objects.csttoken import Token
from cstupid.cst_const_tokens import *
from cstupid.cstlexer import Lexer
from typing import List, Iterator, Optional, Tuple

class Parser:
    def __init__(self) -> None:
        # have a switch for running the debug print statements on the parser
        self.debug_print = False
        # keep track of the token_index
        self.tok_idx = 0
        # keep track of the current token
        self.current_token : Token = Token("EMPTY", "EMPTY")
        # an abstract syntax tree made by the parser
        self.ast : List[Node] = []

    def advance(self) -> Tuple[Token, int, int]:
        idx = -1
        line = -1
        if self.tok_idx < len(self.stream):
            self.current_token, idx, line = self.stream[self.tok_idx]
            self.tok_idx += 1
        else:
            self.current_token = Token(TT_EOI, TT_EOI)
        if self.debug_print:
            print(f"ADVANCE({self.current_token, idx, line})")
        return (self.current_token, idx, line)

    # peek at the next token from the parser
    def peek(self) -> Tuple[Token, int, int]:
        idx = -1
        line = -1
        if self.tok_idx < len(self.stream):
            return_token, idx, line = self.stream[self.tok_idx]
        else:
            return_token = Token(TT_EOI, TT_EOI)
        if self.debug_print:
            print(f"PEEK({return_token, idx, line})")
        return (return_token, idx, line)

    # when a certain type is expected
    def expect_tok_type(self, type_name : str, error_msg : str) -> Token:
        tmp_token, idx, line = self.advance()
        assert tmp_token.name == type_name, error_msg.format(idx, line, tmp_token)
        return tmp_token

    # the variable declaration statement
    def var_declar(self) -> bool:
        if self.debug_print:
            print("check varkey tokentype")
        if self.current_token.name == TT_VARKEY: # from this line on I know the command has to be a variable declaration
            var_name = self.expect_tok_type(TT_IDENTIFIER, "Expected an identifier for the variable name in the variable declaration at position: index->{}, line->{} but found {}")
            self.expect_tok_type(TT_COLON, "Expected a colon for the variable name in the variable declaration at position: index->{}, line->{} but found {}")
            var_type = self.expect_tok_type(TT_IDENTIFIER, "Expected an identifier for the variable type in variable declaration at position: index->{}, line->{} but found {}")
            self.expect_tok_type(TT_ASSIGN, "Expected a assign symbol for the variable declaration at position: index->{}, line->{} but found {}")
            
            var_value, idx, line = self.advance()
            assert var_value.name in (TT_STRING, TT_NUMBER, TT_BOOLEAN), f"Expected a value for the variable declaration at position: index->{idx}, line->{line} but found {var_value}"
            if var_value.name == TT_STRING:
                node_value : Node = CString(var_value.value)
            elif var_value.name == TT_NUMBER:
                # check if there is a math operation that makes for a binary operation
                operation, idx, line = self.peek()
                
                if operation.name in (TT_PLUS, TT_PRODUCT, TT_MINUS):
                    operation, _, _ = self.advance()
                    right = self.expect_tok_type(TT_NUMBER, "Expected a Number in the operation at position: index->{}, line->{}, but found {}")
                    node_value = BinOp(operation, CNumber(var_value.value),CNumber(right.value))
                else:
                    node_value = CNumber(var_value.value)
            elif var_value.name == TT_BOOLEAN:
                node_value = CBoolean(var_value.value)
            else:
                raise Exception("No node value defined for the tokenType in variable declaration")

            self.expect_tok_type(TT_SEMICOLON, "Expected a semicolon for the variable declaration at position: index->{}, line->{} but found {}")
            if self.debug_print:
                print("variable declaration complete!")
            # add the value to the syntax tree
            self.ast.append(VarDeclar(var_type.value, var_name.value, node_value))
            return True
        return False

    # the output statement
    def output(self) -> bool:
        if self.debug_print:
            print("check output tokentype")
        if self.current_token.name == TT_ECHOKEY: # from this line on I know the command has to be a output statement
            self.expect_tok_type(TT_LPAREN, "Expected an left parentesis in the output statement at position: index->{}, line->{} but found {}")
            
            output_value, idx, line = self.advance()
            assert output_value.name in (TT_STRING, TT_IDENTIFIER), f"Expected a value for the output statement at position: index->{idx}, line->{line} but found {output_value}"

            if output_value.name == TT_STRING:
                node_value : Node = CString(output_value.value)
            elif output_value.name == TT_IDENTIFIER:
                node_value = CLink(output_value)
            else:
                raise Exception("No node value defined for the tokenType in the Output statement")

            self.expect_tok_type(TT_RPAREN, "Expected an right parentesis in the output statement at position: index->{}, line->{} but found {}")
            self.expect_tok_type(TT_SEMICOLON, "Expected a semicolon for the output statement at position: index->{}, line->{} but found {}")
            self.ast.append(Output(node_value))
            return True
        return False

    # a comment statement
    def comment(self) -> bool:
        if self.debug_print:
            print("check comment tokentype")
        if self.current_token.name == TT_COMMENT:
            self.ast.append(Comment(self.current_token.value[2:])) # use the [2:] to remove the // from the comment
            return True
        return False

    def term(self):
        pass

    def expression(self):
        pass


    def parse(self, stream : List[Tuple[Token, int, int]]) -> List[Node]: # for now, this will change to List[Node]
        # keep track of the token list from the lexer
        self.stream = stream
        # check if anything matched with the current token
        any_match = True
        # an ast created from the tokens
        self.ast = []
        while not self.current_token.name == TT_EOI and any_match:
            if self.debug_print:
                print("NEW parse loop!")
            self.advance()
            any_match = False
            if self.debug_print:
                print(self.current_token)
            # check if there is an output statement
            any_match = self.output()
            if any_match:
                continue
            # check if there is a variable_declaration
            any_match = self.var_declar()
            if any_match:
                continue
            # check if there is a comment
            any_match = self.comment()
            if any_match:
                continue
            
        
        # if there was no match in the parse loop
        if not self.current_token.name == TT_EOI and not any_match:
            raise Exception(f"There was no rule that matched: {self.stream[self.tok_idx]}")
        
        if self.debug_print:
            print("Syntax Tree:")
            print(self.ast)
        return self.ast
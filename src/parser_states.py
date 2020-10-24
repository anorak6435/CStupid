from CST_const_tokens import TOKEN_TYPES
import CST_parsers
class States:
    def start(izer):
        print("starting state called!")
        token = izer.next_token()
        ast = [] # the structure for the
        """
            start: (comment)+
        """
        while token.tok_type != TOKEN_TYPES.eof:
            if CST_parsers.comment.should_parse(token):
                ast = CST_parsers.comment.parse(token, ast)
            else:
                raise SyntaxError(f"The statemachine Could not parse the token:'{token}'")
            print("token:", token)
            print("peek:", izer.peek)
            token = izer.next_token() # get the next token for the state to evaluate
        return ast
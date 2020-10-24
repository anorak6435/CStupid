from CST_const_tokens import TOKEN_TYPES

class CST_parser(object):
    def should_parse():
        raise Exception("the should parse was not implemented")


# handle single and multiline comments
class comment(CST_parser):
    def should_parse(current_token, izer=None):
        return current_token.tok_type == TOKEN_TYPES.comment or current_token.tok_type == TOKEN_TYPES.multiline_comment
    
    def parse(current_token, ast, izer=None):
        ast.append({"type": current_token.tok_type, "value": current_token.value})
        return ast
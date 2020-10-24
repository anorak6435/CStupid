from CST_Token import Token

# the constant names given to tokens
class TOKEN_TYPES:
    comment = "COMMENT"
    eof = "EOF"
    whitespace = "WHITESPACE"
    multiline_comment = "MULTILINE_COMMENT"

# the tokens the tokenizer / parser will try to match
TOKENS = [
    Token(TOKEN_TYPES.multiline_comment, r"\/\/-->(.|\n)+<--\/\/"),
    Token(TOKEN_TYPES.comment, r"\/\/.*"),
    Token(TOKEN_TYPES.whitespace, r"\s+")
]
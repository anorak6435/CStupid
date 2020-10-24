import re
from CST_Token import Token
from CST_const_tokens import TOKEN_TYPES

class Tokenizer:
    def __init__(self, source, token_strings):
        self.source = source # the input text for the tokenizer
        self.source_index = 0 # where I am in the sourceCode
        self.token_strings = token_strings
        self.peek = None # I need to be able to peek one token ahead

    # check if there is source left
    def is_eof(self, source_stream):
        return len(source_stream) == 0

    def match_token_string_to_source_stream(self, tok_string, source_stream):
        return re.match(tok_string, source_stream)

    # check if the token_type is not whitespace
    def token_is_whitespace(self, token):
        return token.tok_type == TOKEN_TYPES.whitespace

    # get one token from the tokenizer
    def one_token(self):
        token_index = 0
        searching_match = True
        return_token = None

        # loop over the token_strings to match against the source_stream
        while token_index < len(self.token_strings) and searching_match:
            source_stream = self.source[self.source_index:]
            # check if there is anything to check against
            if self.is_eof(source_stream):
                return_token = Token(TOKEN_TYPES.eof, TOKEN_TYPES.eof)
                searching_match = False
            else:
                # there is source left to find a token in.
                match_value = self.match_token_string_to_source_stream(self.token_strings[token_index].value, source_stream)
                if match_value:
                    return_token = Token(self.token_strings[token_index].tok_type, match_value[0])
                    if not self.token_is_whitespace(return_token):
                        searching_match = False
                    else:
                        return_token = None
                        token_index = -1
                    
                    self.source_index += len(match_value[0])
                    
                token_index += 1
        
        if return_token:
            return return_token
        else:
            raise SyntaxError(f"Tokenizer did not find a token in the input stream:'{source_stream}'")

    # the general function for getting the next token
    def next_token(self):
        if self.peek == None: # only on the first call self.peek will still be none
            return_token = self.one_token()
            self.peek = self.one_token()
        else:
            return_token = self.peek
            self.peek = self.one_token()
        return return_token
        
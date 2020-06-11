# This file is not in use by other files
import re
class Rule:
    """
    the rule has an identifier that would match the Name of an Option / Token
    the value for the Rule is optional because the rule does not need to have
    a value if the id has to be matched
    
    optional values:
    when there are more than one value possible for a place in the rule the val
    in the constructor will be an array of Rules. Where the program will loop
    over the array and try to match every rule. ** the order is important **

    """
    def __init__(self, id, val=None, is_id=False):
        self.id = id
        self.value = val
        self.is_id = is_id
    
    # check if the given token matches this rule
    def match_token(self, tok):
        if self.is_id:
            return tok.name == self.id
        else:
            if isinstance(val, list):
                return self.match_list(tok)
            else:
                return re.match(self.value, tok.value)

    # return the first option in the list that matches the token
    def match_list(self, tok):
        for x in range(len(self.value)):
            m = self.match_token(self.value[x])
            if m:
                return m
        # If I went over the list and none of the values made a match
        # There is probably something wrong with the program that made
        # the tokenizer.
        return None
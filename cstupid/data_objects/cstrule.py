# this file will contain the data the parser needs when parsing a grammar

import re
from typing import List

class Rule:
    def __init__(self, name : str, pattern : str) -> None:
        self.name = name
        self.pattern = pattern

    # check if i can parse some input with the pattern inside this rule
    def canParse(self, test_input : str) -> bool:
        return bool(re.match(self.pattern, test_input))


# A Tag is made for the parser to contain a list of rules
class Tag:
    def __init__(self, name : str) -> None:
        self.name = name
        self.pattern : List[Rule]

    # check if all consecutive rules match the input string
    def canParse(self, in_string : str) -> bool:
        patternIndex = 0
        # track what rules were matched
        matched_rules : List[bool] = []
        while patternIndex < len(self.pattern):
            matched_rules.append(self.pattern[patternIndex].canParse(in_string))
            # TODO when a pattern rule matched the in_string has to be updated for the next rule in the list
            patternIndex += 1
        return all(matched_rules)

    def __repr__(self) -> str:
        return f"(TAG '{self.name}'::'{self.pattern}')"
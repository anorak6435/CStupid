# setting up a state machine that could handle parsing a token stream into a syntax tree. following a grammar
from typing import Dict

class State(object):
    def on_event(self, event : Dict):
        # this function handles the different possibilities for incomming tokens
        raise Exception("No on_event function defined for a state!")

    def __repr__(self):
        return self.__str__()

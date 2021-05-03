# setting up a state machine that could handle parsing a token stream into a syntax tree. following a grammar
from typing import Tuple
from .statemachine import State

# the machine that uses the grammar to parse language rules
class CstMachine:
    def __init__(self, grammar : str = "") -> None:
        self.grammar = grammar
        self.state = Start()

    def on_event(self, event):
        """
        incomming tokens from the grammar are given as events 
        to the state machine to be handled.
        """
        self.state.on_event(event)

    def run_grammar(self):
        # run the grammar from the language to change the state of the machine 
        pass



# The states the machine can be in.
class Start(State):
    def __init__(self):
        pass
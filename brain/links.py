# Links between ideas.
# Type of links defined in linktypes.py
from brain.linktypes import types

class Link():
    def __init__(self, link_type, cons=[]):
        self.link_type = link_type
        
        # From -------> To #
        self.from_idea = from_idea
        self.to_idea = to_idea
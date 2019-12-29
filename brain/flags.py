# Special flags for ideas that allow for faster interactions
class Flag():
    NOUN =  0xb00000001
    VERB =  0xb00000010
    ADJ =   0xb00000100
    ADV =   0xb00001000
    PREP =  0xb00010000
    CONJ =  0xb00100000
    ART =   0xb01000000
    INT =   0xb10000000
    def __init__(self, flags):
        self.flags = flags
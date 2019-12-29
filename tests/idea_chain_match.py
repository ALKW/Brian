# Test capabilities of the idea_chain.py file
import sys
import os
sys.path.insert(0, os.getcwd() + "/..")
from brain.idea_chain import IdeaChain
from brain.idea import Idea

# Create dummy ideas to add
i1 = Idea("idea1", temp=True)
i2 = Idea("idea2", temp=True)
i3 = Idea("idea3", temp=True)
i4 = Idea("idea4", temp=True)

############ MATCHING TESTS ###########
# Tests for matching similar chains
# Add Ideas to the head of the list
# i4 - i3 - i2 - i1
icm = IdeaChain()
icm.add_to_head(i1)
icm.add_to_head(i2)
icm.add_to_head(i3)
icm.add_to_head(i4)

icm2 = IdeaChain()
icm2.add_to_head(i1)
icm2.add_to_head(i2)
icm2.add_to_head(i3)
icm2.add_to_head(i4)
print(icm.matches(icm2))
''':-
True
'''

# Tests for matching different chains
# Chain is a contiguous subset of the other
# Add Ideas to the head of the list
# i4 - i3 - i2 - i1
icm = IdeaChain()
icm.add_to_head(i1)
icm.add_to_head(i2)
icm.add_to_head(i3)
icm.add_to_head(i4)

icm2 = IdeaChain()
icm2.add_to_head(i1)
icm2.add_to_head(i2)
icm2.add_to_head(i3)
print(icm.matches(icm2))
''':-
False
'''

# Tests for matching different chains
# Chain is different and same length
# Add Ideas to the head of the list
# i4 - i3 - i2 - i1
icm = IdeaChain()
icm.add_to_head(i1)
icm.add_to_head(i2)
icm.add_to_head(i3)
icm.add_to_head(i4)

icm2 = IdeaChain()
icm2.add_to_head(i1)
icm2.add_to_head(i2)
icm2.add_to_head(i3)
icm2.add_to_head(i3)
print(icm.matches(icm2))
''':-
False
'''
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

############# TEST ADDING ################
# Add Ideas to the head of the list
ic = IdeaChain()
ic.add_to_head(i1)
ic.add_to_head(i2)
ic.add_to_head(i3)
ic.add_to_head(i4)
# i4 - i3 - i2 - i1
print(ic)
''':-
Name: idea4 | ID: idea4temp - Head
Name: idea3 | ID: idea3temp
Name: idea2 | ID: idea2temp
Name: idea1 | ID: idea1temp - Tail
'''

# Add ideas to the tail of the list
ic = IdeaChain()
ic.add_to_tail(i1)
ic.add_to_tail(i2)
ic.add_to_tail(i3)
ic.add_to_tail(i4)
# i1 - i2 - i3 - i4
print(ic)
''':-
Name: idea1 | ID: idea1temp - Head
Name: idea2 | ID: idea2temp
Name: idea3 | ID: idea3temp
Name: idea4 | ID: idea4temp - Tail
'''

# Add Ideas to the head and tail of the list
ic = IdeaChain()
ic.add_to_head(i1)
ic.add_to_tail(i2)
ic.add_to_head(i3)
ic.add_to_tail(i4)
# i3 - i1 - i2 - i4
print(ic)
''':-
Name: idea3 | ID: idea3temp - Head
Name: idea1 | ID: idea1temp
Name: idea2 | ID: idea2temp
Name: idea4 | ID: idea4temp - Tail
'''
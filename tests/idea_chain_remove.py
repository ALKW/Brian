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

############# TEST REMOVING ################
# Remove idea from chain length greater than 1 and from the middle
ic = IdeaChain()
ic.add_to_head(i1)
ic.add_to_head(i2)
ic.add_to_head(i3)
ic.add_to_head(i4)
ic.remove(i3)
# i4 - i2 - i1
print(ic)
''':-
Name: idea4 | ID: idea4temp - Head
Name: idea2 | ID: idea2temp
Name: idea1 | ID: idea1temp - Tail
'''

# Remove idea from chain length greater than 1 and from the head
ic = IdeaChain()
ic.add_to_head(i1)
ic.add_to_head(i2)
ic.add_to_head(i3)
ic.add_to_head(i4)
ic.remove(i4)
# i4 - i2 - i1
print(ic)
''':-
Name: idea3 | ID: idea3temp - Head
Name: idea2 | ID: idea2temp
Name: idea1 | ID: idea1temp - Tail
'''

# Remove idea from chain length greater than 1 and from the tail
ic = IdeaChain()
ic.add_to_head(i1)
ic.add_to_head(i2)
ic.add_to_head(i3)
ic.add_to_head(i4)
ic.remove(i1)
# i4 - i2 - i1
print(ic)
''':-
Name: idea4 | ID: idea4temp - Head
Name: idea3 | ID: idea3temp
Name: idea2 | ID: idea2temp - Tail
'''

# Remove idea from chain length of 1
ic = IdeaChain()
ic.add_to_head(i1)
ic.remove(i1)
print(ic)
''':-
'''

# Remove idea from chain length of 2 at head
ic = IdeaChain()
ic.add_to_head(i1)
ic.add_to_head(i2)
ic.remove(i1)
# i2
print(ic)
''':-
Name: idea2 | ID: idea2temp - Head and Tail
'''

# Remove idea from chain length of 2 at tail
ic = IdeaChain()
ic.add_to_head(i1)
ic.add_to_head(i2)
ic.remove(i2)
# i1
print(ic)
''':-
Name: idea1 | ID: idea1temp - Head and Tail
'''
# Linked list of ideas to form a relational chain to form complex ideas
# Gives information about other ideas

import brain.settings as settings
from brain.idea import Idea

class IdeaChain():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        # Resulting string
        res_str = ""

        # If the chain is empty print the empty chain
        if self.head == None:
            return res_str

        # If the chain contains 1 element print special format
        if self.head == self.tail:
            return str(self.head) + " - Head and Tail\n"

        # add the head
        res_str += str(self.head) + " - Head\n"

        # add all the contents except the head and the last element
        curr = self.head.next
        while curr != None:
            if curr.next == None:
                break
            else:
                res_str += str(curr) + "\n"
                curr = curr.next

        # add the tail
        res_str += str(self.tail) + " - Tail\n"

        return res_str
    
    def add_to_head(self, idea):
        idea_chain_link = IdeaChainLink(idea)
        # If there are no objects in the list, set the head and tail to the new item
        if self.head == None:
            self.head = idea_chain_link
            self.tail = idea_chain_link
        # Otherwise point the idea to the head then point the head to the new idea
        else:
            idea_chain_link.next = self.head
            self.head = idea_chain_link
        self.length += 1

    def add_to_tail(self, idea):
        idea_chain_link = IdeaChainLink(idea)
        # If there are no objects in the list, set the head and tail to the new item
        if self.head == None:
            self.head = idea_chain_link
            self.tail = idea_chain_link
        # Otherwise point the idea to the head then point the head to the new idea
        else:
            self.tail.next = idea_chain_link
            self.tail = idea_chain_link

        self.length += 1

    # Remove an idea from the chain if it exists
    def remove(self, idea_to_rem):
        curr = self.head
        prev = curr
        while curr != None: 
            # If we find the idea, remove it
            if curr.idea.get_id() == idea_to_rem.get_id():
                # If we are removing both the head and tail
                if curr.idea.get_id() == self.head.idea.get_id() and curr.idea.get_id() == self.tail.idea.get_id():
                    self.head = None
                    self.tail = None

                # If we are remving the head adjust the head pointer
                elif curr.idea.get_id() == self.head.idea.get_id():
                    self.head = self.head.next

                # If we are removing the tail adjust the tail
                elif curr.idea.get_id() == self.tail.idea.get_id():
                    self.tail = prev
                    prev.next = None

                else:
                    # Set the previous to point past the current to the currents next element
                    prev.next = curr.next
                return

            prev = curr
            curr = curr.next

        # If we reach here without returning, the idea is not in the chain
        settings.printe("Idea doesnt exist in chain")


    # Determines if an idea chain matches another idea chain
    def matches(self, other_chain):
        self_curr = self.head
        other_curr = other_chain.head

        while self_curr != None or other_curr != None:
            if self_curr.idea.get_id() != other_curr.idea.get_id():
                return False
            self_curr = self_curr.next
            other_curr = other_curr.next

        return True

class IdeaChainLink():
    def __init__(self, idea):
        self.idea = idea
        self.next = None

    def __str__(self):
        return str(self.idea)
# Anything
# Nouns, adjectives, verbs, etc
# Related by connections to other ideas
import brain.settings as s

class Idea():
    def __init__(self, idea, idea_chains=[], links=[], temp=False):
        self.idea_name = idea
        self.chains = idea_chains

        # If it is a temporary Idea (for testing or conversation)
        # Dont set a storage file and set its id to name plus temp
        if temp:
            self.id = s.create_id(self) + "temp"
            self.file = None
        else:
            self.id = s.create_id(self)
            self.file = s.create_storage(self)

        # Add the idea to the global dictionary of ideas
        s.add_idea(self)

    def __str__(self):
        return "Name: " + self.idea_name + " | ID: " + self.id

    ######## GETTERS ########
    def get_idea_name(self):
        return self.idea_name

    def get_id(self):
        return self.id
    
    def get_chains(self):
        return self.chains

    def get_file(self):
        return self.file

    ######## SETTERS #########
    # Add an idea chain to the idea
    def add_chain(self, idea_chain):
        self.chains.append(idea_chain)

    # Remove an idea chain
    def remove_chain(self, idea_chain_to_rem):
        # Look for the chain in the ideas chain list
        for chain in self.chains:
            # If we find a mathcing chain, remove it
            if chain.matches(idea_chain_to_rem):
                self.chains.remove(chain)
                return

        s.printe("Idea chain does not exist")
    
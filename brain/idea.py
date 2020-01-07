# Anything
# Nouns, adjectives, verbs, etc
# Related by connections to other ideas
import brain.settings as s

class Idea():
    def __init__(self, idea, idea_chains=[], temp=False, identifier=None, filename=None):
        self.idea_name = idea
        self.chains = idea_chains
        self.next_avail_id_num = 0

        # If it is a temporary Idea (for testing or conversation)
        # Dont set a storage file and set its id to name plus temp
        if temp:
            self.id = s.create_id(self) + "temp"
            self.file = None
        else:
            # Create an identifier for the file
            if identifier == None:
                self.id = s.create_id(self)
            else:
                self.id = identifier
            
            # Create the storage for the file, unless it is lready created
            if filename == None:
                self.file = s.create_storage(self)
            else:
                self.file = filename

        # Add the idea to the global dictionary of ideas
        s.add_idea(self)

    def __str__(self):
        return "Name: " + self.idea_name + " | ID: " + self.id                    

    def contains_chain_by_id(self, chain_id):
        for chain in self.chains:
            if chain_id == chain.id:
                return True
        return False

    def assign_next_id_num(self):
        # Get the next available ID number
        id_num = self.get_next_id_num()

        # Increment the next available ID number
        self.next_avail_id_num += 1
        return id_num

    ######## GETTERS ########
    def get_idea_name(self):
        return self.idea_name

    def get_id(self):
        return self.id
    
    def get_chains(self):
        return self.chains

    def get_file(self):
        return self.file

    def get_next_id_num(self):
        return self.next_avail_id_num

    ######## SETTERS #########
    # Add an idea chain to the idea
    def add_chain(self, idea_chain, ):
        # Create the unique ID for the chain
        idea_chain.id = str(self.get_id()) + str(self.assign_next_id_num())

        # Add the idea chain to the file if required
        with open(self.get_file, "w+") as f:
            # Write the chain ID
            f.write(idea_chain.id)

            # Write each idea's id
            for idea_id in idea_chain.to_list_of_ids():
                f.write(" " + idea_id)

        # Add the idea chain to the list of idea chains for the idea
        self.chains.append(idea_chain)

        return s.SUCCESS

    # Remove an idea chain
    def remove_chain(self, idea_chain_to_rem):
        # Look for the chain in the ideas chain list
        for chain in self.chains:
            # If we find a matching chain, remove it
            if chain.matches(idea_chain_to_rem):
                # Remove the chain
                self.chains.remove(chain)

                # Remove the chain from the associated file
                with open(self.get_file(), "w+") as f:
                    pass

                return s.SUCCESS

        s.printe("Idea chain does not exist")
        return s.DNE_ERR

    # Replace an existing chain with another chain
    def replace_chain(self, idea_chain_to_rem, idea_chain_to_add):
        # Remove the chain
        self.remove_chain(idea_chain_to_rem)

        # Add the other chain
        self.add_chain(idea_chain_to_add)


    
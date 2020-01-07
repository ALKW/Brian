# Builds from the files located in storage

import os
import brain.settings as s
from brain.idea import Idea
from brain.idea_chain import IdeaChain, IdeaChainLink

def build_brain():
    # Create the ideas
    create_ideas()

    # Create the chains
    create_chains()

# Creates each idea from the file without any idea chains attached
def create_ideas():
    # Run through the list of files (one file per idea)
    for filename in os.listdir("."):
        # Create the idea from the file
        with open(filename, "r+") as f:
            # Idea_name should be the first line
            idea_name = f[0].strip()

            # Remove the file ending for the id
            idea_id = filename.replace(".brn", "")

            # Create the idea by passing in the idea and the idea_id
            curr_idea = Idea(idea_name, identifier=idea_id, filename=filename)

# Create the idea chains, should only be called after the ideas are created
def create_chains():
    # Run through the list of files (one file per idea)
    for filename in os.listdir("."):
        # Create the chains for the idea from the file
        with open(filename, "r+") as f:
            # The main idea_id should be the file name minus the file ending
            main_idea_id = filename.replace(".brn", "")

            # Skip the first line as it is the idea and build from the remainder
            idea = s.ideas[main_idea_id]

            # each line contains an idea chain
            for line in f[1:]:
                # Split the line into tokens
                tokens = line.split()

                # The chain id is the first token in the list
                chain_id = tokens[0]
                idea_chain = IdeaChain(identifier=chain_id)

                # Build each idea chain from the remaining tokens
                for idea_id in tokens[1:]:
                    idea_chain.add_to_tail(s.ideas[idea_id])

                # Add the idea chain to the idea
                idea.add_chain()


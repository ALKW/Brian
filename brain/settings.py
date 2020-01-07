# Helper functions and global variables across the system

import sys

# Maintains all the ideas
# Ensures no idea is repeated
# The is a dictionary of ideas
# Key: idea name
# Value: idea link object {idea, idea chains it is apary of}
ideas = dict()

# SUCCESS CODES
SUCCESS = 0

# ERROR CODES
DNE_ERR = 1

# Print Toggle
PRINT = True

############ PRINTING ############
# Wrapper function that allows toggling printing with just a global variable
def printe(*values, sep=' ', end='\n', file=sys.stdout, flush=False):
    if PRINT:
        # Append all the values together
        print_str = ""
        for value in values:
            print_str += str(value)

        # Print the resulting string
        print(print_str, sep=sep, end=end, file=file, flush=flush)


############ IDEA INITIALIZATION ##############
# Creates a globally unique id for the idea
def create_id(idea):
    # Get the base of the name
    idea_name = idea.get_idea_name()

    # Append numbers to the name to differentiate ideas with the same name
    idea_id = idea_name

    # Keep incrementing the counter until we find an index that hasnt been used yet
    counter = 0
    while idea_id in ideas.keys():
        idea_id = idea_name + str(counter)
        counter += 1

    return idea_id

# Creates a file and tracker for an idea in order to store it
# also makes ideas globally unique    
def create_storage(idea):
    # Get the id of the idea
    file_name = idea.get_idea_id()

    # Create the file based on the name
    with open(file_name + ".brn", "w+") as f:
        # Write the idea to the file initially
        f.write(idea.get_idea_name())

    return file_name

######## IDEAS ##########
# Add the idea to the global dictionary of ideas. Key is by id
def add_idea(idea):
    idea_key = idea.get_id()
    ideas[idea_key] = idea

# Remove a group of ideas
def remove_ideas(ideas):
    for idea in ideas:
        remove_idea(idea)

# Remove a single idea:
# - Remove all idea chains that contain the idea
# - Remove it from the global index
# - Remove its file from the storage
def remove_idea(idea):
    pass

# Find an idea by its name
def find_idea_by_name(idea_name_to_find):
    if idea_name_to_find in ideas.keys():
        return ideas[idea_name_to_find]
    else:
        printe("Idea name does not exist")
        return 
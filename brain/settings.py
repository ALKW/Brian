# Maintains all the ideas
# Ensures no idea is repeated
ideas = []

# SUCCESS CODES
SUCCESS = 0

# ERROR CODES
DNE_ERR = 1

######## IDEAS ##########
# Add an idea
def add_idea(idea):
    pass

# Remove a group of ideas
def remove_ideas(ideas):
    for idea in ideas:
        remove_idea(idea)

# Remove a single idea
# Adjust all the links going into it
def remove_idea(idea):
    pass

# Find an idea by its name
def find_idea_by_name(idea_name_to_find):
    for idea in ideas:
        if idea.name == idea_name_to_find:
            return ideas[ideas.index(idea)]
    return None
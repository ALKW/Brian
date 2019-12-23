# Anything
# Nouns, adjectives, verbs, etc
# Related by links
import brain.settings as settings

class Idea():
    def __init__(self, idea, links=[]):
        self.idea = idea 
        self.out_links = out_links
        self.in_links = in_links
        self.name = name
        self.file = settings.create_storage()

    # Add a link to another idea
    def add_link_to(self, idea, link):
        pass

    # Remove a group of links
    def remove_links(self, links):
        for link in links:
            self.remove_link(link)

    # Remove a single link
    def remove_link(self, link):
        if link in self.out_links:
            self.out_links.remove(link)
        elif link in self.in_links:
            self.in_links.remove(link)
        else:
            print("Link already deleted")

    # Remove a link to an idea based on the idea
    def remove_link_to(self, idea):
        pass
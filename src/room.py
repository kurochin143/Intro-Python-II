# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    name: str
    description: str
    n_to = None
    e_to = None
    w_to = None
    s_to = None
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
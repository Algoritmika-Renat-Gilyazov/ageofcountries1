class Region:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.army = []

class Country:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources
        self.diplomacy = {}
        self.army = []
items = []

class Item:
    def __init__(self, name, description):
        self.id = len(items) + 1
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

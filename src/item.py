
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_pick(self):
        print(f"You've picked up {self.name:s}")
        print(f"-{self.description:s}")

    def on_drop(self):
        print(f"You dropped {self.name:s}")
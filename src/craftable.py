class Craftable:
    def __init__(self, name):
        self.name = name
        self.infoboxes = []
        self.recipes = []

    def add_infobox(self, infobox):
        self.infoboxes.append(infobox)

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def to_dict(self):
        return {"name": self.name,
                "infobox": self.infoboxes,
                "recipe": self.recipes}

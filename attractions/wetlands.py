from .attraction import Attraction

class Wetlands(Attraction):
    def __init__(self, name):
        super().__init__(name)
        self.description = "Here be dragons and their ilk. (This is the wetlands, by the way.)"
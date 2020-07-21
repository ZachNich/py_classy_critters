from .attraction import Attraction

class SnakePit(Attraction):
    def __init__(self, name):
        super().__init__(name)
        self.description = "Snakes do bite, but they also lick. It's a 50/50."
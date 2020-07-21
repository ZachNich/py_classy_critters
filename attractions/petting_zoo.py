from .attraction import Attraction

class PettingZoo(Attraction):
    def __init__(self, name):
        super().__init__(name)
        self.description = "Pet lil creatures at your own risk."
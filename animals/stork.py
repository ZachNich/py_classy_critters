from .animal import Animal
from movements import Flying

class Stork(Animal, Flying):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Flying.__init__(self)

    def feed(self):
      print(f"Looks like {self.name} just finished eating one of the fishes. You decide to not feed her today.")
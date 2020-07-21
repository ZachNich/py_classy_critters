from .animal import Animal
from movements import Flying

class Parakeet(Animal, Flying):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Flying.__init__(self)
from .animal import Animal
from movements import Walking, Swimming, Flying

class Duck(Animal, Walking, Swimming, Flying):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        Swimming.__init__(self)
        Flying.__init__(self)
        self.shift = shift
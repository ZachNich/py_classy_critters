from .animal import Animal
from movements import Swimming, Walking

class Frog(Animal):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)

    def feed(self):
      print(f"{self.name} doesn't need your help. He nips a fly from the air with his agile tongue whenever he is hungry.")
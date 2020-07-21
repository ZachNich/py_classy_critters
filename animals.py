from datetime import date

class Animal: 
    def __init__(self, name, species, food, chip_num):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.food = food
      self.__chip_num = chip_num

    @property
    def chip_num(self):
      return self.__chip_num

    @chip_num.setter
    def chip_num(self, num):
      pass

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
      return f"{self.name} is a {self.species}"

class Lizard(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
        
class Donkey(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

class Llama(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift
    
class Frog(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
      print(f"{self.name} doesn't need your help. He nips a fly from the air with his agile tongue whenever he is hungry.")

class Goat(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

class Snake(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Duck(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

class Fish(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

class Bull(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

class Pigeon(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.flying = True

class Stork(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.flying = True

    def feed(self):
      print(f"Looks like {self.name} just finished eating one of the fishes. You decide to not feed her today.")


class Rabbit(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

class Snail(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Parakeet(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.flying = True
    
class Rhino(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift
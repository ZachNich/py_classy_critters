class PettingZoo:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "Pet lil creatures at your own risk."
        self.animals = []
    
    def addAnimals(self, *animal):
        for each in animal:
            self.animals.append(each)
    
    @property
    def last_animal_added(self):
        return self.animals[-1]

    

class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "Snakes do bite, but they also lick. It's a 50/50."
        self.animals = []
    
    def addAnimals(self, *animal):
        for each in animal:
            self.animals.append(each)
                
    @property
    def last_animal_added(self):
        return self.animals[-1]

class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "Here be dragons and their ilk. (This is the wetlands, by the way.)"
        self.animals = [] 
    
    def addAnimals(self, *animal):
        for each in animal:
            self.animals.append(each)
                
    @property
    def last_animal_added(self):
        return self.animals[-1]
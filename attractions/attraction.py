class Attraction:
    def __init__(self, name):
        self.attraction_name = name
        self.animals = []
    
    def addAnimals(self, *animal):
        for each in animal:
            self.animals.append(each)
                
    @property
    def last_animal_added(self):
        return self.animals[-1]
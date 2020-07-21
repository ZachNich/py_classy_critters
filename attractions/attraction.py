class Attraction:
    def __init__(self, name):
        self.attraction_name = name
        self.animals = []
    
    def addAnimals(self, *animal):
        for each in animal:
            self.animals.append(each)

    def removeAnimals(self, *animal):
        for each in animal:
            self.animals.remove(each)

    def __str__(self):
        return f'{self.name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)
                
    @property
    def last_animal_added(self):
        return self.animals[-1]
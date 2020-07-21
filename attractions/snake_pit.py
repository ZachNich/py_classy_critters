from .attraction import Attraction

class SnakePit(Attraction):
    def __init__(self, name):
        super().__init__(name)
        self.description = "Snakes do bite, but they also lick. It's a 50/50."

    def addAnimals(self, *animal):
        for each in animal:
            try:
                if animal.slither_speed > -1:
                    self.animals.append(each)
            except AttributeError as ex:
                print(f"{animal} doesn\'t slither too good. It'd be a shame for them to get all slithered on. Try another attraction.")    
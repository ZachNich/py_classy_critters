from .attraction import Attraction

class Wetlands(Attraction):
    def __init__(self, name):
        super().__init__(name)
        self.description = "Here be dragons and their ilk. (This is the wetlands, by the way.)"

    def addAnimals(self, *animal):
        for each in animal:
            try:
                if animal.swim_speed > -1 or animal.fly_speed > -1:
                    self.animals.append(each)
            except AttributeError as ex:
                print(f"{animal} doesn\'t swim or fly. Doesn't seem to be nothing special about this one. Try another attraction.")
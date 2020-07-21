from .attraction import Attraction

class PettingZoo(Attraction):
    def __init__(self, name):
        super().__init__(name)
        self.description = "Pet lil creatures at your own risk."

    def addAnimals(self, *animal):
        for each in animal:
            try:
                if animal.walk_speed > -1:
                    self.animals.append(each)
            except AttributeError as ex:
                print(f"{animal} doesn\'t walk too good. It'd be a shame for them to get stepped all over. Try another attraction.")


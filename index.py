from animals import Lizard, Donkey, Llama, Frog, Goat, Snake, Duck, Fish, Bull, Pigeon, Stork, Rabbit, Snail, Parakeet, Rhino
from attractions import PettingZoo, SnakePit, Wetlands

kenny = Lizard('Kenny', 'lizard', 'manflesh', 69420)
jenny = Donkey('Jenny', 'donkey', 'midnight', 'manflesh', 1337)
penny = Llama('Penny', 'llama', 'dusk', 'manflesh', 808)
benny = Frog('Benny', 'frog', 'manflesh', 8675309)
lenny = Goat('Lenny', 'goat', 'dusk', 'manflesh', 123)
vinny = Snake('Vinny', 'snake', 'mouseflesh', 324)
connie = Duck('Connie', 'duck', 'dawn', 'gooseflesh', 909)
johnny = Fish('Johnny', 'fish', 'fishflesh', 9)
ronnie = Bull('Ronnie', 'bull', 'midnight', 'manflesh', 1011)
lonny = Pigeon('Lonny', 'pigeon', 'anything', 666)
yonni = Stork('Yonni', 'stork', 'fishflesh', 2244)
donnie = Rabbit('Donnie', 'rabbit', 'dusk', 'carrotflesh', 42)
bonnie = Snail('Bonnie', 'snail', 'unknown', 1307)
keeter = Parakeet('Keeter', 'parakeet', 'snailflesh', 789)
reeter = Rhino('Reeter', 'rhino', 'dusk', 'manflesh', 2)

eatin_good = PettingZoo('Eatin Good')
baller_crawler = SnakePit('Baller Crawler')
wetty_already = Wetlands('Wetty Already')

eatin_good.addAnimals(jenny, penny, lenny, ronnie, donnie, reeter)
baller_crawler.addAnimals(kenny, benny, vinny, bonnie)
wetty_already.addAnimals(connie, johnny, lonny, yonni, keeter)

for animal in eatin_good.animals:
    print(f"{animal.name} is a good {animal.species} in {eatin_good.attraction_name}")

for animal in baller_crawler.animals:
    print(f"{animal.name} is a good {animal.species} in {baller_crawler.attraction_name}")

for animal in wetty_already.animals:
    print(f"{animal.name} is a good {animal.species} in {wetty_already.attraction_name}")

yonni.feed()
benny.feed()
donnie.feed()
bonnie.slither()
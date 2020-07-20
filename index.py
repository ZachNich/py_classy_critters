from animals import Lizard, Donkey, Llama, Frog, Goat, Snake, Duck, Fish, Bull, Pigeon, Stork, Rabbit, Snail, Parakeet, Rhino
from attractions import PettingZoo, SnakePit, Wetlands

kenny = Lizard('Kenny', 'lizard', 'manflesh')
jenny = Donkey('Jenny', 'donkey', 'midnight', 'manflesh')
penny = Llama('Penny', 'llama', 'dusk', 'manflesh')
benny = Frog('Benny', 'frog', 'manflesh')
lenny = Goat('Lenny', 'goat', 'dusk', 'manflesh')
vinny = Snake('Vinny', 'snake', 'mouseflesh')
connie = Duck('Connie', 'duck', 'gooseflesh')
johnny = Fish('Johnny', 'fish', 'fishflesh')
ronnie = Bull('Ronnie', 'bull', 'midnight', 'manflesh')
lonny = Pigeon('Lonny', 'pigeon', 'anything')
yonni = Stork('Yonni', 'stork', 'fishflesh')
donnie = Rabbit('Donnie', 'rabbit', 'dusk', 'carrotflesh')
bonnie = Snail('Bonnie', 'snail', 'unknown')
keeter = Parakeet('Keeter', 'parakeet', 'snailflesh')
reeter = Rhino('Reeter', 'rhino', 'dusk', 'manflesh')

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
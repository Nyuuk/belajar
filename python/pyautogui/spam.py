import pyautogui as pt
from time import sleep

list_an = """Canidae
Felidae
Cat
Cattle
Dog
Donkey
Goat
Guinea pig
Horse
Pig
Rabbit
Fancy rat varieties
laboratory rat strains
Sheep breeds
Water buffalo breeds
Chicken breeds
Duck breeds
Goose breeds
Pigeon breeds
Turkey breeds
Aardvark
Aardwolf
African buffalo
African elephant
African leopard
Albatross
Alligator
Alpaca
American buffalo (bison)
American robin
Amphibian
list
Anaconda
Angelfish
Anglerfish
Ant
Anteater
Antelope
Antlion
Ape
Aphid
Arabian leopard
Arctic Fox
Arctic Wolf
Armadillo
Arrow crab
Asp
Ass (donkey)
Baboon
Badger
Bald eagle
Bandicoot
Barnacle
Barracuda
Basilisk
Bass
Bat
Beaked whale
Bear
list
Beaver
Bedbug
Bee
Beetle
Bird
list
Bison
Blackbird
Black panther
Black widow spider
Blue bird
Blue jay
Blue whale
Boa
Boar
Bobcat
Bobolink
Bonobo
Booby
Box jellyfish
Bovid
Buffalo, African
Buffalo, American (bison)
Bug
Butterfly
Buzzard
Camel
Canid
Cape buffalo
Capybara
Cardinal
Caribou
Carp
Cat
list
Catshark
Caterpillar
Catfish
Cattle
list
Centipede
Cephalopod
Chameleon
Cheetah
Chickadee
Chicken
list
Chimpanzee
Chinchilla
Chipmunk
Clam
Clownfish
Cobra
Cockroach
Cod
Condor
Constrictor
Coral
Cougar
Cow
Coyote
Crab
Crane
Crane fly
Crawdad
Crayfish
Cricket
Crocodile
Crow
Cuckoo
Cicada
Damselfly
Deer
Dingo
Dinosaur
list
Dog
list
Dolphin
Donkey
"""

sleep(10)
for i in list_an.split('\n'):
    var = "Inay adalah " + i
    pt.typewrite(var)
    pt.press('Enter')

def add_animal_in_family(species, animal, family):
    if family not in species:
        species[family] = set()
    species[family].add(animal)

species = {}
print(add_animal_in_family(species, 'cat', 'felidae'))


import collections

def add_animal_in_family_short(species, animal, family):
    species[family].add(animal)

species = collections.defaultdict(set)
print(add_animal_in_family_short(species, 'cat', 'felidae'))

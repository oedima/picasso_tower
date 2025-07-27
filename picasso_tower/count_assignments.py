from itertools import permutations
from picasso_tower.hints import Hint
from picasso_tower.primitives import Animal, Color, Floor


FLOORS = list(Floor)
ANIMALS = list(Animal)
COLORS = list(Color)

ANIMAL_PERMS = list(permutations(ANIMALS))
COLOR_PERMS = list(permutations(COLORS))

ANIMAL_ASSIGNMENTS = [
    dict(zip(animal_perm, FLOORS)) for animal_perm in ANIMAL_PERMS
]

COLOR_ASSIGNMENTS = [
    dict(zip(color_perm, FLOORS)) for color_perm in COLOR_PERMS
]


def count_assignments(hints: list[Hint]) -> int:
    count = 0

    for animal_to_floor in ANIMAL_ASSIGNMENTS:
        for color_to_floor in COLOR_ASSIGNMENTS:
            if all(hint.satisfied_with(animal_to_floor, color_to_floor) for hint in hints):
                count += 1

    return count
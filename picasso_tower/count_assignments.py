from itertools import permutations
from picasso_tower.hints import AbsoluteHint, NeighborHint, RelativeHint
from picasso_tower.primitives import Animal, Color, Floor


def count_assignments(hints):
    floors = list(Floor)
    all_animals = list(Animal)
    all_colors = list(Color)

    count = 0
    for animal_perm in permutations(all_animals):
        for color_perm in permutations(all_colors):
            
            animal_to_floor = {animal_perm[i]: floors[i] for i in range(5)}
            color_to_floor = {color_perm[i]: floors[i] for i in range(5)}

            if all(hint.satisfies(animal_to_floor, color_to_floor) for hint in hints):
                count += 1

    return count



HINTS_EX1 = [
    AbsoluteHint(Animal.Rabbit, Floor.First),
    AbsoluteHint(Animal.Chicken, Floor.Second),
    AbsoluteHint(Floor.Third, Color.Red),
    AbsoluteHint(Animal.Bird, Floor.Fifth),
    AbsoluteHint(Animal.Grasshopper, Color.Orange),
    NeighborHint(Color.Yellow, Color.Green),
]

HINTS_EX2 = [
    AbsoluteHint(Animal.Bird, Floor.Fifth),
    AbsoluteHint(Floor.First, Color.Green),
    AbsoluteHint(Animal.Frog, Color.Yellow),
    NeighborHint(Animal.Frog, Animal.Grasshopper),
    NeighborHint(Color.Red, Color.Orange),
    RelativeHint(Animal.Chicken, Color.Blue, -4)
]

HINTS_EX3 = [
    RelativeHint(Animal.Rabbit, Color.Green, -2)
]


def test():
    assert count_assignments(HINTS_EX1) == 2, 'Failed on example #1'
    assert count_assignments(HINTS_EX2) == 4, 'Failed on example #2'
    assert count_assignments(HINTS_EX3) == 1728, 'Failed on example #3'
    print('Success!')


if __name__ == '__main__':
    test()

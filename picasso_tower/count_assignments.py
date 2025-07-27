from itertools import permutations
from picasso_tower.hints import Hint
from picasso_tower.primitives import Animal, Color, Floor


# Predefined lists of enum values
FLOORS = list(Floor)
ANIMALS = list(Animal)
COLORS = list(Color)

# Precompute all possible permutations of animals and colors
ANIMAL_PERMS = list(permutations(ANIMALS))
COLOR_PERMS = list(permutations(COLORS))

# Precompute all valid animal-to-floor mappings
ANIMAL_ASSIGNMENTS = [
    dict(zip(animal_perm, FLOORS)) for animal_perm in ANIMAL_PERMS
]

# Precompute all valid color-to-floor mappings
COLOR_ASSIGNMENTS = [
    dict(zip(color_perm, FLOORS)) for color_perm in COLOR_PERMS
]


def count_assignments(hints: list[Hint]) -> int:
    """
    Counts the number of valid assignments of animals and colors to floors
    that satisfy all provided hints.

    This function evaluates all 5! x 5! (14,400) combinations of animal-to-floor
    and color-to-floor assignments, using cached permutations and dictionaries.

    Args:
        hints (list[Hint]): A list of Hint objects representing constraints 
                            that must be satisfied by a valid assignment.

    Returns:
        int: The number of satisfying assignments.
    """
    count = 0

    for animal_to_floor in ANIMAL_ASSIGNMENTS:
        for color_to_floor in COLOR_ASSIGNMENTS:
            if all(hint.satisfied_with(animal_to_floor, color_to_floor) for hint in hints):
                count += 1

    return count
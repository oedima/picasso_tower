from picasso_tower.count_assignments import count_assignments
from picasso_tower.hints import AbsoluteHint, NeighborHint, RelativeHint
from picasso_tower.primitives import Animal, Color, Floor


def test_count_assignments_example_1():
    hints = [
        AbsoluteHint(Animal.Rabbit, Floor.First),
        AbsoluteHint(Animal.Chicken, Floor.Second),
        AbsoluteHint(Floor.Third, Color.Red),
        AbsoluteHint(Animal.Bird, Floor.Fifth),
        AbsoluteHint(Animal.Grasshopper, Color.Orange),
        NeighborHint(Color.Yellow, Color.Green),
    ]
    assert count_assignments(hints) == 2


def test_count_assignments_example_2():
    hints = [
        AbsoluteHint(Animal.Bird, Floor.Fifth),
        AbsoluteHint(Floor.First, Color.Green),
        AbsoluteHint(Animal.Frog, Color.Yellow),
        NeighborHint(Animal.Frog, Animal.Grasshopper),
        NeighborHint(Color.Red, Color.Orange),
        RelativeHint(Animal.Chicken, Color.Blue, -4),
    ]
    assert count_assignments(hints) == 4


def test_count_assignments_example_3():
    hints = [
        RelativeHint(Animal.Rabbit, Color.Green, -2),
    ]
    assert count_assignments(hints) == 1728


def test_count_assignments_empty_hints():
    # No constraints – all permutations valid
    assert count_assignments([]) == 120 * 120  # 5! * 5!


def test_count_assignments_unsatisfiable():
    hints = [
        AbsoluteHint(Animal.Frog, Floor.First),
        AbsoluteHint(Animal.Frog, Floor.Second),  # Contradiction
    ]
    assert count_assignments(hints) == 0


def test_count_assignments_minimal_single_match():
    hints = [
        AbsoluteHint(Animal.Frog, Floor.First),
        AbsoluteHint(Color.Red, Floor.First),
        AbsoluteHint(Animal.Rabbit, Floor.Second),
        AbsoluteHint(Color.Blue, Floor.Second),
        AbsoluteHint(Animal.Grasshopper, Floor.Third),
        AbsoluteHint(Color.Yellow, Floor.Third),
        AbsoluteHint(Animal.Bird, Floor.Fourth),
        AbsoluteHint(Color.Green, Floor.Fourth),
        AbsoluteHint(Animal.Chicken, Floor.Fifth),
        AbsoluteHint(Color.Orange, Floor.Fifth)
    ]
    # Just one exact configuration satisfies all constraints
    assert count_assignments(hints) == 1


def test_count_assignments_relative_zero_diff():
    # Attribute and floor must match
    hints = [
        RelativeHint(Animal.Frog, Floor.First, difference=0)
    ]
    assert count_assignments(hints) == 120 * 120 // 5  # Only 1 of 5 matches for Animal.Frog == Floor.First

from picasso_tower.hints import AbsoluteHint, RelativeHint, NeighborHint
from picasso_tower.primitives import Floor, Animal, Color


def test_absolute_hint_true():
    hint = AbsoluteHint(Animal.Frog, Color.Green)
    animal_to_floor = {Animal.Frog: Floor.Second}
    color_to_floor = {Color.Green: Floor.Second}
    assert hint.satisfied_with(animal_to_floor, color_to_floor)


def test_absolute_hint_false():
    hint = AbsoluteHint(Animal.Bird, Color.Yellow)
    animal_to_floor = {Animal.Bird: Floor.Fourth}
    color_to_floor = {Color.Yellow: Floor.Second}
    assert not hint.satisfied_with(animal_to_floor, color_to_floor)


def test_relative_hint_true():
    hint = RelativeHint(Animal.Rabbit, Color.Red, difference=1)
    animal_to_floor = {Animal.Rabbit: Floor.Fourth}
    color_to_floor = {Color.Red: Floor.Third}
    assert hint.satisfied_with(animal_to_floor, color_to_floor)


def test_relative_hint_false_wrong_diff():
    hint = RelativeHint(Animal.Rabbit, Color.Red, difference=2)
    animal_to_floor = {Animal.Rabbit: Floor.Fourth}
    color_to_floor = {Color.Red: Floor.Third}
    assert not hint.satisfied_with(animal_to_floor, color_to_floor)


def test_relative_hint_false_missing_attr():
    hint = RelativeHint(Animal.Chicken, Color.Blue, difference=1)
    animal_to_floor = {}  # no mapping for Chicken
    color_to_floor = {Color.Blue: Floor.Second}
    assert not hint.satisfied_with(animal_to_floor, color_to_floor)


def test_neighbor_hint_true():
    hint = NeighborHint(Color.Orange, Animal.Grasshopper)
    animal_to_floor = {Animal.Grasshopper: Floor.Third}
    color_to_floor = {Color.Orange: Floor.Second}
    assert hint.satisfied_with(animal_to_floor, color_to_floor)


def test_neighbor_hint_false_not_adjacent():
    hint = NeighborHint(Color.Yellow, Animal.Bird)
    animal_to_floor = {Animal.Bird: Floor.First}
    color_to_floor = {Color.Yellow: Floor.Third}
    assert not hint.satisfied_with(animal_to_floor, color_to_floor)


def test_neighbor_hint_false_missing_attr():
    hint = NeighborHint(Color.Red, Animal.Frog)
    animal_to_floor = {}
    color_to_floor = {}
    assert not hint.satisfied_with(animal_to_floor, color_to_floor)

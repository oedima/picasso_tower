from picasso_tower.primitives import Floor, Animal, Color


class Hint:
    def satisfies(self, animal_to_floor, color_to_floor):
        raise NotImplementedError


class AbsoluteHint(Hint):
    def __init__(self, attr1, attr2):
        self._attr1 = attr1
        self._attr2 = attr2

    def satisfies(self, animal_to_floor, color_to_floor):
        return get_floor_of_attr(self._attr1, animal_to_floor, color_to_floor) == \
               get_floor_of_attr(self._attr2, animal_to_floor, color_to_floor)


class RelativeHint(Hint):
    def __init__(self, attr1, attr2, difference):
        self._attr1 = attr1
        self._attr2 = attr2
        self._difference = difference

    def satisfies(self, animal_to_floor, color_to_floor):
        f1 = get_floor_of_attr(self._attr1, animal_to_floor, color_to_floor)
        f2 = get_floor_of_attr(self._attr2, animal_to_floor, color_to_floor)
        return f1 is not None and f2 is not None and (f1 - f2 == self._difference)


class NeighborHint(Hint):
    def __init__(self, attr1, attr2):
        self._attr1 = attr1
        self._attr2 = attr2

    def satisfies(self, animal_to_floor, color_to_floor):
        f1 = get_floor_of_attr(self._attr1, animal_to_floor, color_to_floor)
        f2 = get_floor_of_attr(self._attr2, animal_to_floor, color_to_floor)
        return f1 is not None and f2 is not None and abs(f1 - f2) == 1
    

def get_floor_of_attr(attr, animal_to_floor, color_to_floor):
    if isinstance(attr, Floor):
        return attr
    elif isinstance(attr, Animal):
        return animal_to_floor.get(attr)
    elif isinstance(attr, Color):
        return color_to_floor.get(attr)
    return None

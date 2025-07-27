from abc import ABC, abstractmethod
from picasso_tower.primitives import Floor, Animal, Color


class Hint(ABC):    
    def __init__(self, attr1, attr2):
        self._attr1 = attr1
        self._attr2 = attr2

    @abstractmethod
    def satisfied_with(self, 
                       animal_to_floor: dict[Animal, Floor], 
                       color_to_floor: dict[Color, Floor]) -> bool:
        pass
    
    
    def _get_floor_of_attr(self, attr, animal_to_floor, color_to_floor):
        if isinstance(attr, Floor):
            return attr
        elif isinstance(attr, Animal):
            return animal_to_floor.get(attr)
        elif isinstance(attr, Color):
            return color_to_floor.get(attr)
        return None


class AbsoluteHint(Hint):
    def __init__(self, attr1, attr2):
        super().__init__(attr1, attr2)

    def satisfied_with(self, animal_to_floor, color_to_floor):
        return self._get_floor_of_attr(self._attr1, animal_to_floor, color_to_floor) == \
               self._get_floor_of_attr(self._attr2, animal_to_floor, color_to_floor)


class RelativeHint(Hint):
    def __init__(self, attr1, attr2, difference):
        super().__init__(attr1, attr2)
        self._difference = difference

    def satisfied_with(self, animal_to_floor, color_to_floor):
        f1 = self._get_floor_of_attr(self._attr1, animal_to_floor, color_to_floor)
        f2 = self._get_floor_of_attr(self._attr2, animal_to_floor, color_to_floor)
        return f1 is not None and f2 is not None and (f1 - f2 == self._difference)


class NeighborHint(Hint):
    def __init__(self, attr1, attr2):
        super().__init__(attr1, attr2)

    def satisfied_with(self, animal_to_floor, color_to_floor):
        f1 = self._get_floor_of_attr(self._attr1, animal_to_floor, color_to_floor)
        f2 = self._get_floor_of_attr(self._attr2, animal_to_floor, color_to_floor)
        return f1 is not None and f2 is not None and abs(f1 - f2) == 1
    


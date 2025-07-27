from abc import ABC, abstractmethod
from picasso_tower.primitives import Floor, Animal, Color


class Hint(ABC):
    """
    Abstract base class for all hint types. A hint describes a constraint
    on the relationship between two attributes (animals, colors, or floors).
    """

    def __init__(self, attr1, attr2):
        """
        Initializes a Hint with two attributes to be compared.

        Raises:
            ValueError: If both attributes are of the same type.
        """
        if type(attr1) == type(attr2):
            raise ValueError(
                f"Hint cannot compare two attributes of the same type: {type(attr1).__name__}"
            )

        self._attr1 = attr1
        self._attr2 = attr2

    @abstractmethod
    def satisfied_with(self, 
                       animal_to_floor: dict[Animal, Floor], 
                       color_to_floor: dict[Color, Floor]) -> bool:        
        """
        Determines whether the hint is satisfied under the given floor assignments.

        Args:
            animal_to_floor: A mapping of each Animal to its assigned Floor.
            color_to_floor: A mapping of each Color to its assigned Floor.

        Returns:
            True if the constraint defined by the hint is satisfied, False otherwise.
        """
        pass
    


    def _get_floor_of_attr(self, attr, animal_to_floor, color_to_floor) -> Floor | None:
        """
        Resolves the floor of a given attribute by consulting the relevant mapping.

        Args:
            attr: The attribute to resolve (Floor, Animal, or Color).
            animal_to_floor: Mapping from Animal to Floor.
            color_to_floor: Mapping from Color to Floor.

        Returns:
            The resolved Floor, or None if the attribute is not found.
        """
        if isinstance(attr, Floor):
            return attr
        elif isinstance(attr, Animal):
            return animal_to_floor.get(attr)
        elif isinstance(attr, Color):
            return color_to_floor.get(attr)
        return None


class AbsoluteHint(Hint):
    """
    A hint that requires two attributes to be located on the same floor.
    """

    def __init__(self, attr1, attr2):
        """
        Initializes an AbsoluteHint requiring equality between two attributes.
        """
        super().__init__(attr1, attr2)

    def satisfied_with(self, animal_to_floor, color_to_floor):
        return self._get_floor_of_attr(self._attr1, animal_to_floor, color_to_floor) == \
               self._get_floor_of_attr(self._attr2, animal_to_floor, color_to_floor)


class RelativeHint(Hint):
    """
    A hint that requires the first attribute to be a fixed number of floors above the second.
    """

    def __init__(self, attr1, attr2, difference: int):
        """
        Initializes a RelativeHint requiring a fixed floor difference between two attributes.

        Args:
            difference: attr1.floor - attr2.floor must equal this value.
        """
        super().__init__(attr1, attr2)
        self._difference = difference

    def satisfied_with(self, animal_to_floor, color_to_floor):
        f1 = self._get_floor_of_attr(self._attr1, animal_to_floor, color_to_floor)
        f2 = self._get_floor_of_attr(self._attr2, animal_to_floor, color_to_floor)
        return f1 is not None and f2 is not None and (f1 - f2 == self._difference)


class NeighborHint(Hint):
    """
    A hint that requires two attributes to be on adjacent floors.
    """

    def __init__(self, attr1, attr2):
        """
        Initializes a NeighborHint requiring a floor difference of 1 between two attributes.
        """
        super().__init__(attr1, attr2)

    def satisfied_with(self, animal_to_floor, color_to_floor):
        f1 = self._get_floor_of_attr(self._attr1, animal_to_floor, color_to_floor)
        f2 = self._get_floor_of_attr(self._attr2, animal_to_floor, color_to_floor)
        return f1 is not None and f2 is not None and abs(f1 - f2) == 1
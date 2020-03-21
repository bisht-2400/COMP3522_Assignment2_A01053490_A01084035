from item import Item


class StuffedAnimal(Item):
    def __init__(self, name, description, product_id, stuffing, size, fabric):
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric
        super().__init__( name,  description, product_id)


class DancingSkeleton(StuffedAnimal):
    def __init__(self, name, description, product_id, stuffing, size, fabric, has_glow=True):
        self._has_glow = has_glow
        super().__init__(name, description, product_id, stuffing, size, fabric)


class Reindeer(StuffedAnimal):
    def __init__(self, name, description, product_id, stuffing, size, fabric, has_glow=True):
        self._has_glow = has_glow
        super().__init__(name, description, product_id, stuffing, size, fabric)


class EasterBunny(StuffedAnimal):
    def __init__(self, name, description, product_id, stuffing, size, fabric, color):
        self._color = color
        super().__init__(name, description, product_id, stuffing, size, fabric)

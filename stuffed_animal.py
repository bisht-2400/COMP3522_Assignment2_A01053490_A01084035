from store_item import StoreItem

from Stuffing import Stuffing
from Fabric import Fabric


class StuffedAnimal(StoreItem):
    def __init__(self, stuffing, size, fabric, **kwargs):
        super().__init__(**kwargs)
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric


class Reindeer(StuffedAnimal):
    def __init__(self, **kwargs):
        super().__init__(stuffing=Stuffing.WOOL, fabric=Fabric.COTTON, **kwargs)


class DancingSkeleton(StuffedAnimal):
    def __init__(self, **kwargs):
        super().__init__(stuffing=Stuffing.POLYESTER_FIBERFILL, fabric=Fabric.ACRYLIC, **kwargs)


class EasterBunny(StuffedAnimal):
    def __init__(self, color, **kwargs):
        super().__init__(stuffing=Stuffing.POLYESTER_FIBERFILL, fabric=Fabric.LINEN, **kwargs)
        self.color = color
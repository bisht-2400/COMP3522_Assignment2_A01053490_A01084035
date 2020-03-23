from store_item import StoreItem

from Stuffing import Stuffing
from Fabric import Fabric


class StuffedAnimal(StoreItem):
    """
    Stuffed Animal item: Inherits from StoreItem.
    """

    def __init__(self, stuffing, size, fabric, **kwargs):
        """
        Initializer for the Stuffed Animal class.
        :param stuffing: String
        :param size: String
        :param fabric: String
        :param kwargs: Other StoreItem Attributes.
        """
        super().__init__(**kwargs)
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric


class Reindeer(StuffedAnimal):
    """
    Reindeer: Inherits from Stuffed Animal class.
    """

    def __init__(self, **kwargs):
        """
        Initializer for the Reindeer class.
        :param kwargs: Other StoreItem Attributes.
        """
        super().__init__(stuffing=Stuffing.WOOL, fabric=Fabric.COTTON, **kwargs)


class DancingSkeleton(StuffedAnimal):
    """
    DancingSkeleton: Inherits from Stuffed Animal class.
    """

    def __init__(self, **kwargs):
        """
        Initializer for the DancingSkeleton class.
        :param kwargs: Other StoreItem Attributes.
        """
        super().__init__(stuffing=Stuffing.POLYESTER_FIBERFILL, fabric=Fabric.ACRYLIC, **kwargs)


class EasterBunny(StuffedAnimal):
    """
    EasterBunny: Inherits from the Stuffed Animal class.
    """

    def __init__(self, color, **kwargs):
        """
        Initializer for the EasterBunny class.
        :param color: String
        :param kwargs: Other StoreItem Attributes.
        """
        super().__init__(stuffing=Stuffing.POLYESTER_FIBERFILL, fabric=Fabric.LINEN, **kwargs)
        self.color = color

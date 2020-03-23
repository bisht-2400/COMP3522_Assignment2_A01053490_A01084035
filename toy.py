from store_item import StoreItem


class Toy(StoreItem):
    """
    Toy item: Inherits from the StoreItem class.
    """
    def __init__(self, battery_operated, min_age, **kwargs):
        """
        Initializer for the Toy class.
        :param battery_operated: Boolean
        :param min_age: int
        :param kwargs: Other StoreItem Attributes.
        """
        super().__init__(**kwargs)
        self._battery_operated = battery_operated
        self._min_age = min_age


class SantaWorkshop(Toy):
    """
    SantaWorkshop: Inherits from the Toy class.
    """
    def __init__(self, width, height, num_of_rooms, **kwargs):
        """
        Initializer for the SantaWorkshop class.
        :param width: int
        :param height: int
        :param num_of_rooms: int
        :param kwargs: Other StoreItem Attributes.
        """
        super().__init__(battery_operated=False, **kwargs)

        self._width = width
        self._height = height
        self._num_of_rooms = num_of_rooms


class RCSpider(Toy):
    """
    RCSprider: Inherits from the Toy class.
    """
    def __init__(self, speed, jump_height, does_glow, type, **kwargs):
        """
        Initializer for the RCSpider class.
        :param speed: int
        :param jump_height: int
        :param does_glow: Boolean
        :param type: String
        :param kwargs: Other StoreItem Attributes.
        """
        super().__init__(battery_operated=True, **kwargs)
        self._speed = speed
        self._jump_height = jump_height
        self._does_glow = does_glow
        self._type = type


class RobotBunny(Toy):
    """
    RobotBunny: Inherits from the Toy class.
    """
    def __init__(self, num_of_sound, color, **kwargs):
        """
        Initializer for the RobotBunny class.
        :param num_of_sound: int
        :param color: String
        :param kwargs: Other StoreItem Attributes.
        """
        super().__init__(battery_operated= True,**kwargs)
        self._num_of_sound = num_of_sound
        self._color = color



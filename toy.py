from store_item import StoreItem


class Toy(StoreItem):
    def __init__(self, battery_operated, min_age, **kwargs):
        super().__init__(**kwargs)
        self._battery_operated = battery_operated
        self._min_age = min_age


class SantaWorkshop(Toy):
    def __init__(self, width, height, num_of_rooms, **kwargs):
        super().__init__(battery_operated=False, **kwargs)

        self._width = width
        self._height = height
        self._num_of_rooms = num_of_rooms


class RCSpider(Toy):
    def __init__(self, speed, jump_height, does_glow, type, **kwargs):
        super().__init__(battery_operated=True, **kwargs)
        self._speed = speed
        self._jump_height = jump_height
        self._does_glow = does_glow
        self._type = type


class RobotBunny(Toy):
    def __init__(self, num_of_sound, color, **kwargs):
        super().__init__(battery_operated= True,**kwargs)
        self._num_of_sound = num_of_sound
        self._color = color



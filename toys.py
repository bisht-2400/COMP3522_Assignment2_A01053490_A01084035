from item import Item


class Toy(Item):
    def __int__(self, has_batteries, min_age, name, description, product_id, stock):
        self._has_batteries = has_batteries
        self._min_age = min_age
        super().__init__(name, description, product_id)


class DollHouse(Toy):
    def __init__(self, min_age, name, description, product_id, dimensions, num_rooms, has_batteries):
        self._dimensions = dimensions
        self._num_rooms = num_rooms
        super().__int__(has_batteries, min_age, name, description, product_id)


class RCSpider(Toy):
    def __init__(self, has_batteries, min_age, name, description, product_id, speed, jump_height, glow, spider_type):
        self._speed = speed
        self._jump_height = jump_height
        self._glow = glow
        self._spider_type = spider_type
        super().__int__(has_batteries, min_age, name, description, product_id)


class RobotBunny(Toy):
    def __init__(self, has_batteries, min_age, name, description, product_id, num_sounds, color):
        self._num_sounds = num_sounds
        self._color = color
        super().__int__(has_batteries, min_age, name, description, product_id)
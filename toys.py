from item import Item


class Toy(Item):
    def __int__(self, battery, age, name, desc, prodID, stock):
        self._battery = battery
        self._age = age
        super().__init__( name, stock, desc, prodID)


class DollHouse(Toy):
    def __init__(self, battery, age, name, desc, prodID, stock, dimens, numRooms):
        self._dimens = dimens
        self._numRooms = numRooms
        super().__int__(battery, age, name, desc, prodID, stock)


class RCSpider(Toy):
    def __init__(self, battery, age, name, desc, prodID, stock, speed, jHeight, glow, type):
        self._speed = speed
        self._jHeight = jHeight
        self._glow = glow
        self._type = type
        super().__int__(battery, age, name, desc, prodID, stock)


class RobotBunny(Toy):
    def __init__(self, battery, age, name, desc, prodID, stock, numSounds, color):
        self._numSounds = numSounds
        self._color = color
        super().__int__(battery, age, name, desc, prodID, stock)
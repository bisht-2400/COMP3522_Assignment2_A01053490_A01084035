from item import Item


class StuffedAnimals(Item):
    def __init__(self, name, stock, desc, prodID, stuff, size, fabric):
        self._stuff = stuff
        self._size = size
        self._fabric = fabric
        super().__init__( name, stock, desc, prodID)


class DancingSkeleton(StuffedAnimals):
    def __init__(self, name, stock, desc, prodID, stuff, size, fabric, glow = True):
        self._glow = glow
        super().__init__(name, stock, desc, prodID, stuff, size, fabric)


class Reindeer(StuffedAnimals):
    def __init__(self, name, stock, desc, prodID, stuff, size, fabric, glowNose =True):
        self._glow = glowNose
        super().__init__(name, stock, desc, prodID, stuff, size, fabric)


class EasterBunny(StuffedAnimals):
    def __init__(self, name, stock, desc, prodID, stuff, size, fabric, color):
        self._color = color
        super().__init__(name, stock, desc, prodID, stuff, size, fabric)

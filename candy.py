from item import Item


class Candy(Item):
    def __init__(self,  name, stock, desc, prodID, lactose, nuts):
        self._lactose = lactose
        self._nuts = nuts
        super().__init__(name, stock, desc, prodID)


class PumpkinCaramelToffee(Candy):
    def __init__(self, name, stock, desc, prodID, lactose, nuts, variety):
        self._variety = variety
        super().__init__(name, stock, desc, prodID, lactose, nuts)


class CandyCanes(Candy):
    def __init__(self, name, stock, desc, prodID, lactose, nuts, stripes):
        self._stripes = stripes
        super().__init__(name, stock, desc, prodID, lactose, nuts)


class CremeEggs(Candy):
    def __init__(self, name, stock, desc, prodID, lactose, nuts, packSize):
        self._packSize = packSize
        super().__init__(name, stock, desc, prodID, lactose, nuts)

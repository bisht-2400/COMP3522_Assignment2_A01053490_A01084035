class Item:

    def __init__(self, name, stock, desc, prodID):
        self._desc = desc
        self._prodID = prodID
        self._name = name
        self._stock = stock

    def getName(self):
        return self._name

    def getStock(self):
        if self._stock == 0:
            return "Out of Stock"
        if 0 < self._stock < 3:
            return "Very Low"
        if 3 <= self._stock < 10:
            return "Low"
        if self._stock >= 10:
            return "In Stock"

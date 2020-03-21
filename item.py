class Item:

    def __init__(self, name, description, product_id):
        self._description = description
        self._product_id = product_id
        self._name = name

    def getName(self):
        return self._name

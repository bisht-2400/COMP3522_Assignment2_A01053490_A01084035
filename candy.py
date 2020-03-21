from item import Item


class Candy(Item):
    def __init__(self,  name, description, product_id, has_lactose, has_nuts):
        self._has_lactose = has_lactose
        self._has_nuts = has_nuts
        super().__init__(name, description, product_id)


class PumpkinCaramelToffee(Candy):
    def __init__(self, name, description, product_id, has_lactose, has_nuts, variety):
        self._variety = variety
        super().__init__(name, description, product_id, has_lactose, has_nuts)


class CandyCane(Candy):
    def __init__(self, name, description, product_id, has_lactose, has_nuts, stripes):
        self._stripes = stripes
        super().__init__(name, description, product_id, has_lactose, has_nuts)


class CremeEgg(Candy):
    def __init__(self, name, description, product_id, has_lactose, has_nuts, pack_size):
        self._pack_size = pack_size
        super().__init__(name, description, product_id, has_lactose, has_nuts)

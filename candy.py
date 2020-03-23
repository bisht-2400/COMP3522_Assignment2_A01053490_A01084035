from store_item import StoreItem


class Candy(StoreItem):
    def __init__(self, contain_nut, lactose_free, **kwargs):
        super().__init__(**kwargs)
        self._contain_nut = contain_nut
        self._lactose_free = lactose_free


class CandyCane(Candy):
    def __init__(self, stripe_color, **kwargs):
        super().__init__(contain_nuts=False, lactose_free=True, **kwargs)
        self._stripe_color = stripe_color


class CremeEgg(Candy):
    def __init__(self, pack_size, **kwargs):
        super().__init__(contain_nuts=False, lactose_free=True, **kwargs)
        self._pack_size = pack_size


class PumpkinCaramelToffee(Candy):
    def __init__(self, variety, **kwargs):
        super().__init__(contain_nut=True, lactose_free=False, **kwargs)
        self._variety = variety

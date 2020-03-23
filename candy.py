from store_item import StoreItem


class Candy(StoreItem):
    """
    Candy item: Inherits StoreItem.
    """
    def __init__(self, contain_nut, lactose_free, **kwargs):
        """
        Initializes the Candy class.
        :param contain_nut: Boolean
        :param lactose_free: Boolean
        :param kwargs: Other StoreItem Attributes.
        """
        super().__init__(**kwargs)
        self._contain_nut = contain_nut
        self._lactose_free = lactose_free


class CandyCane(Candy):
    """
    CandyCane: Inherits from Candy.
    """
    def __init__(self, stripe_color, **kwargs):
        """
        Initializes the CandyCane class.
        :param stripe_color: String
        :param kwargs: Other StoreItem Attributes.
        """
        super().__init__(contain_nuts=False, lactose_free=True, **kwargs)
        self._stripe_color = stripe_color


class CremeEgg(Candy):
    """
    CremeEgg: Inherits from Candy.
    """
    def __init__(self, pack_size, **kwargs):
        """
        Initializes the CremeEgg class.
        :param pack_size: int
        :param kwargs:  Other StoreItem Attributes.
        """
        super().__init__(contain_nuts=False, lactose_free=True, **kwargs)
        self._pack_size = pack_size


class PumpkinCaramelToffee(Candy):
    """
    PumpkinCaramelToffee: Inherits from Candy.
    """
    def __init__(self, variety, **kwargs):
        """
        Initializes the PumpkinCaramelToffee class.
        :param variety: String
        :param kwargs:  Other StoreItem Attributes.
        """
        super().__init__(contain_nut = True, lactose_free=False, **kwargs)
        self._variety = variety

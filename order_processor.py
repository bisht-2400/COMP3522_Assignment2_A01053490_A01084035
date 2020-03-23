import pandas as pd

from store_item_factory import ChristmasItemFactory
from store_item_factory import EasterItemFactory
from store_item_factory import HalloweenItemFactory
from order import Order


class OrderProcessor:
    def __init__(self):
        self._order_lst = []
        self._orders = []
        self._column = []

    def sent_order(self, filename):
        self.get_orders(filename)
        return self._orders

    def get_orders(self, filename):
        data = pd.read_excel(filename + ".xlsx")
        self._column = data.columns

        for row in data.iterrows():
            self._order_lst.append(row[1])

        self.process_order()

    def check_corrupted(self, d):
        if d['holiday'] == 'Halloween' and d['item'] == 'Toy':
            if d['spider_type'] != 'nan' and d['spider_type'] != 'Tarantula' and d['spider_type'] != 'Wolf Spider':
                return False, "Halloween toy should have spider type only Tarantula and Wolf spider "

        elif d['holiday'] == 'Halloween' and d['item'] == 'Toy':
            if d['colour'] != 'Orange' and d['colour'] != 'Blue' and d['colour'] != 'Pink' and d['colour'] != 'nan':
                return False, "Halloween Toy should have only these colors: Orange, Blue, Pink"
            else:
                return True, "None"

        elif d['item'] == 'StuffedAnimal':
            if not (d['fabric'] == 'Linen' or d['fabric'] == 'Acrylic' or d['fabric'] == 'Cotton'):
                return False, "Stuffing can only by Linen, Acrylic, and Cotton"

            elif not (d['size'] == 'S' or d['size'] == 'L' or d['size'] == 'M'):
                return False, "Stuffing can have only these size : S, L, M"

            elif not (d['stuffing'] == 'Polyester Fibrefill' or d['stuffing'] == 'Wool'):
                return False, "stuffing can only by polyester Fibrefill and wool"

            else:
                return True, "None"

        elif d['item'] == 'Candy' and d['holiday'] == 'Halloween':
            if not (d['variety'] == 'Sea Salt' or d['variety'] == 'Regular' or d['variety'] == 'nan'):
                return False, "Halloween candy can only have variety by Sea Salt and Regular"
            elif d['has_lactose'] != "Y":
                return False, "Halloween candy should have lactose"
            elif d['has_nuts'] != "Y":
                return False, "Halloween candy should have nuts"
            else:
                return True, "None"

        elif d['item'] == 'Candy' and d['holiday'] == 'Christmas':
            if not (d['colour'] == 'Red' or d['colour'] == 'Green'):
                return False, "Christmas candy can only have colour of Red and Green"
            elif d['has_lactose'] == "Y":
                return False, "Christmas candy should not have lactose"
            elif d['has_nuts'] == "Y":
                return False, "Christmas candy should not have nuts"
            else:
                return True, "None"

        elif d['item'] == 'Candy' and d['holiday'] == 'Easter':
            if d['has_lactose'] != "Y":
                return False, "Halloween candy should have lactose"
            elif d['has_nuts'] != "Y":
                return False, "Halloween candy should have nuts"
            else:
                return True, "None"

        else:
            return True, "None"

    def process_order(self):
        factory_mapper = FactoryMapping()
        d = {}

        for detail in self._order_lst:
            i = 0
            for value in detail:
                d[self._column[i]] = value
                i = i + 1

            if d['holiday'] == "Christmas":
                factory = factory_mapper.map(1)
            elif d["holiday"] == "Halloween":
                factory = factory_mapper.map(2)
            else:
                factory = factory_mapper.map(3)

            corrupted = self.check_corrupted(d)[0]
            corrupted_reason = self.check_corrupted(d)[1]
            self._orders.append(Order(ord_num=d["order_number"], product_id=d["product_id"],
                                      item_type=d["item"], name=d["name"], prod_detail=dict(d), factory_obj=factory,
                                      corrupted=corrupted, corrupted_reason=corrupted_reason))


class FactoryMapping:
    def __init__(self):
        self.factory_mapping = {
            1: ChristmasItemFactory,
            2: HalloweenItemFactory,
            3: EasterItemFactory
        }

    def map(self, choice):
        return self.factory_mapping.get(choice, None)()

import pandas as pd
import factory_pattern_constructors


class Order:
    def __init__(self, factory, order_number, item, quantity, **kwargs):
        self.order_num = order_number
        self.factory = factory
        self.item = item
        self.quantity = quantity
        self.attributes = {key: kwargs[key] for key in kwargs if pd.notna(kwargs[key])}


class FactoryMapper:
    @staticmethod
    def factory_mapper(holiday):
        if holiday == 'christmas':
            return factory_pattern_constructors.ChristmasInventoryFactory
        elif holiday == 'halloween':
            return factory_pattern_constructors.HalloweenInventoryFactory
        else:
            return factory_pattern_constructors.EasterInventoryFactory


class ProcessWebOrders:
    @staticmethod
    def generate_orders():
        excel_file = "C:\\Users\\Kshitiz Bisht\\Desktop\\BCIT\\Term-3\\ObjectOriented\\Assignment_2\\orders.xlsx"
        for row in pd.read_excel(excel_file).iterrows():
            factory = FactoryMapper.factory_mapper(row[1]['holiday'])()
            order = Order(factory=factory, **row[1])
            del order.attributes['holiday']
            yield order


for i in ProcessWebOrders.generate_orders():
    print(i.order_num)

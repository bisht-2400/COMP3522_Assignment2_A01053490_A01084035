import pandas as pd
import factory_pattern_constructors


class Order:
    def __init__(self, factory, is_valid, order_number, item, quantity, **kwargs):
        self.order_num = order_number
        self.is_valid = is_valid
        self.factory = factory
        self.item = item
        self.quantity = quantity
        self.attributes = {key: kwargs[key] for key in kwargs if pd.notna(kwargs[key])}
        # for key in kwargs:
        #     print(key, type(kwargs[key]))


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
    def helper_check_y_or_n(field):
        if field == "Y" or "N" or "nan":
            return True
        return False

    @staticmethod
    def generate_orders():
        excel_file = "C:\\Users\\Kshitiz Bisht\\Desktop\\BCIT\\Term-3\\ObjectOriented\\Assignment_2\\orders.xlsx"
        for row in pd.read_excel(excel_file).iterrows():
            factory = FactoryMapper.factory_mapper(row[1]['holiday'])()
            is_valid = ProcessWebOrders.check_valid_order(row[1])
            order = Order(factory=factory, is_valid=is_valid, **row[1])
            del order.attributes['holiday']
            yield order

    @staticmethod
    def check_valid_order(order):
        if ProcessWebOrders.helper_check_y_or_n(order['has_batteries']) and ProcessWebOrders.helper_check_y_or_n(order['has_glow']) and ProcessWebOrders.helper_check_y_or_n(order['has_lactose']) and ProcessWebOrders.helper_check_y_or_n(order['has_nuts']):
            if order['variety'] == 'Sea Salt' or 'Regular' or 'nan':
                if order['stuffing'] == 'Polyester Fiberfill' or 'Wool' or 'nan':
                    if order['fabric'] == 'Linen' or 'Cotton' or 'Acrylic' or 'nan':
                        if order['size'] == 'Small' or 'Medium' or 'Large' or 'nan':
                            return True
        else:
            return False

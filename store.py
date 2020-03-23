from datetime import datetime

from inventory import Inventory
from order_processor import OrderProcessor


class Store:
    """
    Store class: Handles all the queries received.
    """

    def __init__(self):
        """
        Initializes the Store.
        """
        self._orders = []
        self._inventory = Inventory()

    def get_inventory(self):
        """
        Accessor for the inventory.
        :return: Inventory Object
        """
        return self._inventory

    def get_orders(self, filename):
        """
        Accessor for the orders.
        :param filename: String
        """
        self._orders = OrderProcessor().set_order(filename)
        self.update_inventory()

    def update_inventory(self):
        """
        Updates the inventory: changes the quantity of the product.
        """
        for i in self._orders:
            if i.get_corrupted():
                i_quantity = i.get_prod_detail()['quantity']
                if self._inventory.find_item(i.get_name()):
                    if self._inventory.get_item_count(i.get_name())[0] <= i_quantity:
                        self._inventory.add_item(i.get_name(), 100)
                        self._inventory.remove_item(i.get_name(), i.get_prod_detail()['quantity'])
                    else:
                        self._inventory.remove_item(i.get_name(), i.get_prod_detail()['quantity'])
                else:
                    i_holiday = i.get_prod_detail()['holiday']
                    i_item = i.get_prod_detail()['item']
                    self._inventory.initial_item(i.get_name(), 100, i_holiday, i_item)
                    self._inventory.remove_item(i.get_name(), i.get_prod_detail()['quantity'])

        self._inventory.get_print()

    def create_dtr(self):
        """
        Creates the Daily transaction report.
        """
        print("____ STORE - DAILY TRANSACTION REPORT (DTR)")
        time = datetime.now()
        print(time.strftime("%d-%m-%Y %H:%I"))
        print('\n')
        for order in self._orders:
            if order.get_corrupted():
                print("Order ", order.get_order_num(), ", Item ", order.get_item_type(), ", Product ID ",
                      order.get_product_id(), " Name ", order.get_name(), ", Quantity ", order.get_quantity())

        print("\nThese orders have a problem\n")
        for order in self._orders:
            if not order.get_corrupted():
                print("Order ", order.get_order_num(), "Could not process order data was corrupted", order.get_order_num(),
                      order.get_corrupted_reason())


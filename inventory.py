class Inventory:
    """
    Inventory class: Handles all the tasks related
    to the inventory of all the products of the Store.
    """
    def __init__(self):
        """
        Initializes the Inventory class.
        """
        self._inventory = {}

    def get_inventory(self):
        """
        Accessor for the inventory.
        :return: dict
        """
        return self._inventory

    def initial_item(self, item_name, amount, holiday, type):
        """
        Sets the initial items in the inventory dictionary.
        :param item_name: String
        :param amount: int
        :param holiday: String
        :param type: Item Object type: String
        """
        self._inventory[item_name] =[amount, holiday, type]

    def add_item(self, item_name, amount):
        """
        Increments the stock of an item
        :param item_name: String
        :param amount: int
        """
        self._inventory[item_name][0] += amount

    def find_item(self, item_name):
        """
        Finds the item in the inventory.
        :param item_name: String
        :return: Boolean
        """
        for i in self._inventory:
            if i == item_name:
                return True
        return False

    def find_item_with_holiday_type(self, holiday, item):
        """
        Finds the item with the holiday type given.
        :param holiday: String
        :param item: String
        """
        return [i for i, v in self._inventory.items() if v[1] == holiday and v[2] == item]

    def remove_item(self, item_name, amount):
        """
        Decrements the stock of the item.
        :param item_name: String
        :param amount: int
        """
        self._inventory[item_name][0] -= amount

    def get_item_count(self, item_name):
        """
        Accessor for the item_Count.
        :param item_name: String
        :return: int
        """
        return self._inventory[item_name]

    def get_print(self):
        """
        Prints all the items in the inventory.
        """
        for item, value in self._inventory.items():
            print(item, " : ", value)


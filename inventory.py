class Inventory:
    def __init__(self):
        self._inventory = {}

    def get_inventory(self):
        return self._inventory

    def initial_item(self, item_name, amount, holiday, type):
        self._inventory[item_name] =[amount, holiday, type]

    def add_item(self, item_name, amount):
        self._inventory[item_name][0] += amount

    def find_item(self, item_name):
        for i in self._inventory:
            if i == item_name:
                return True
        return False

    def find_item_with_holiday_type(self, holiday, item):
        return [i for i, v in self._inventory.items() if v[1]==holiday and v[2]==item]

    def remove_item(self, item_name, amount):
        self._inventory[item_name][0] -= amount

    def get_item_count(self, item_name):
        return self._inventory[item_name]

    def get_print(self):
        for i,v in self._inventory.items():
            print(i," : ",v)


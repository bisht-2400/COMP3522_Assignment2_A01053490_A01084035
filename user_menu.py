from store import Store
from inventory import Inventory


class UserMenu:
    def __init__(self):
        self._store = Store()

    def main_menu(self):
        user_input=None
        while user_input != 3:
            print("\nWelcome to the GB Store! ")
            print("-----------------------")
            print("1. Process Web Order  2. View Inventory  3. Quit")
            string_input = input("Please enter your choice (1-3)\n")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            # try catch in case that user input other character not integer
            try:
                user_input = int(string_input)
            except ValueError:
                print("Please enter a valid number")

            if user_input == 1:
                print("\nProceeding your web order")
                self.process_web_order()
            elif user_input == 2:
                print("\nShowing inventory\nWhich inventory are you looking for?\n")
                self.check_inventory()

            elif user_input == 3:
                self._store.create_dtr()
                print("Thank you for choosing GB Store!.")
            else:
                print("INVALID! Please enter a number from 1 - 3.")

    def process_web_order(self):
        filename = input("Please enter filename\n")
        try:
            self._store.get_orders(filename)
        except FileNotFoundError:
            print("No such file found!")

    @staticmethod
    def check_inventory(number):
        if number >= 10:
            return "In Stock"
        elif 3 <= number < 10:
            return "Low"
        elif 1 <= number < 3:
            return "Very Low"
        else:
            return "Out of Stock"

    def decrement_count(self, specific_item, current_inventory):
        if len(specific_item) != 0:
            print("Please check the inventory")
            for i in specific_item:
                get_item_inventory = current_inventory.get_item_count(i)[0]
                print(i, get_item_inventory, UserMenu.check_inventory(get_item_inventory))
            print("\n")
        else:
            print("No such items found in this inventory\n")

    def check_inventory(self):
        current_inventory=self._store.get_inventory()
        while True:
            print("1. Santa's Workshop "
                  "2. RC Spider "
                  "3. Robot Bunny \n"
                  "4. Dancing Skeleton "
                  "5. Reindeer "
                  "6. Easter Bunny \n"
                  "7. Pumpkin Caramel Toffee "
                  "8. Candy Canes "
                  "9. Creme Eggs \n"
                  "10. Total Items "
                  "11. Quit \n")
            opt = input("Please select and item to view the current stock\n")
            try:
               opt = int(opt)
            except ValueError:
                print("Please input integer number")
                continue
            if opt == 1:
                specific_item=current_inventory.find_item_with_holiday_type("Christmas", "Toy")
                self.decrement_count(specific_item, current_inventory)

            elif opt == 2:
                specific_item=current_inventory.find_item_with_holiday_type("Halloween", "Toy")
                self.decrement_count(specific_item, current_inventory)

            elif opt == 3:
                specific_item=current_inventory.find_item_with_holiday_type("Easter", "Toy")
                self.decrement_count(specific_item, current_inventory)

            elif opt == 4:
                specific_item = current_inventory.find_item_with_holiday_type("Christmas", "StuffedAnimal")
                self.decrement_count(specific_item, current_inventory)

            elif opt == 5:
                specific_item = current_inventory.find_item_with_holiday_type("Halloween", "StuffedAnimal")
                self.decrement_count(specific_item, current_inventory)

            elif opt == 6:
                specific_item = current_inventory.find_item_with_holiday_type("Easter", "StuffedAnimal")
                self.decrement_count(specific_item, current_inventory)

            elif opt == 7:
                specific_item = current_inventory.find_item_with_holiday_type("Christmas", "Candy")
                self.decrement_count(specific_item, current_inventory)

            elif opt == 8:
                specific_item = current_inventory.find_item_with_holiday_type("Halloween", "Candy")
                self.decrement_count(specific_item, current_inventory)

            elif opt == 9:
                specific_item = current_inventory.find_item_with_holiday_type("Easter", "Candy")
                self.decrement_count(specific_item, current_inventory)

            elif opt == 10:
                specific_item = current_inventory.get_inventory()
                self.decrement_count(specific_item, current_inventory)

            elif opt == 11:
                break
            else:
                print("INVALID! Please enter a number from 1 - 11.\n")


if __name__ == "__main__":
    userMenu = UserMenu()
    userMenu.main_menu()


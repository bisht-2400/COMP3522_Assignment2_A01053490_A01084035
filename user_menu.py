from item import Item


class UserMenu:

    def __init__(self, item_list):
        self._item_list = item_list

    def menu(self):
        """
        Displaying the User menu.
        """

        user_input = None
        while user_input != 3:
            print("Press 1 to process Web Order ")
            print("Press 2 for Check Inventory")
            print("Press 3 to Exit")

            string_input = input("Please enter your choice (1-3)")

            # handle user pressing only enter in menu

            if string_input == '':
                continue

            user_input = int(string_input)
            if user_input == 1:
                print("1 pressed")
            if user_input == 2:
                print("Please enter the item name")
                item = input()
                for items in self._item_list:
                    if items.getName() == item:
                        print(items.getStock())






def generate_test_books():
    """
    Return a list of books with dummy data.
    :return: a list
    """
    item_list = [
        # Item("Harry", 2,,,
        # Item("Hello", 5,,,
        # Item("Potter", 7,,,
        # Item("Bye", 3,,
    ]
    return item_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    item_list = generate_test_books()
    c = UserMenu(item_list)
    c.menu()


if __name__ == '__main__':
    main()
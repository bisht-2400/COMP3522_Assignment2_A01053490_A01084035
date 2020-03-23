class StoreItem:
    """
    Base class for the items in the Store.
    """
    def __init__(self, name, description, product_id):
        """
        Initializer for the StoreItem: Common Attributes.
        :param name: String
        :param description: String
        :param product_id: String
        """
        self._name = name
        self._description = description
        self._product_id = product_id

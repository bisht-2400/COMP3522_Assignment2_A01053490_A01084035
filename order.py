class Order:
    """
    Order Class: Instantiating the Order object
    """

    def __init__(self, ord_num, product_id, item_type, name, prod_detail, factory_obj, corrupted, corrupted_reason):
        """
        Initializes the Order class.
        :param ord_num: int
        :param product_id: String
        :param item_type: String
        :param name: String
        :param prod_detail: String
        :param factory_obj: String
        :param corrupted: Boolean
        :param corrupted_reason: String
        """
        self._ord_num = ord_num
        self._product_id = product_id
        self._item_type = item_type
        self._name = name
        self._prod_detail = prod_detail
        self._factory_obj = factory_obj
        self._corruptedOrNot = corrupted
        self._corrupted_reason = corrupted_reason

    def get_order_num(self):
        """
        Accessor for the order number.
        :return: int
        """
        return self._ord_num

    def get_item_type(self):
        """
        Accessor for the item type.
        :return: String
        """
        return self._item_type

    def get_name(self):
        """
        Accessor for the name.
        :return: String
        """
        return self._name

    def get_prod_detail(self):
        """
        Accessor for the details of the product.
        :return: String
        """
        return self._prod_detail

    def get_quantity(self):
        """
        Accessor for the quantity of the product.
        :return: int
        """
        return self._prod_detail["quantity"]

    def get_product_id(self):
        """
        Accessor for the product Id.
        :return: String
        """
        return self._product_id

    def get_corrupted(self):
        """
        Accessor if the Order if corrupted
        :return: Boolean
        """
        return self._corruptedOrNot

    def get_corrupted_reason(self):
        """
        Accessor for the reason of corrupted data.
        :return: String
        """
        return self._corrupted_reason

    def set_corrupted_reason(self, corrupted_reason):
        """
        Mutator for the reason of corrupted data.
        :param corrupted_reason: String
        """
        self._corrupted_reason = corrupted_reason

    def __str__(self):
        """
        Prints the Order number
        :return: String
        """
        return f"orderNo: {self._ord_num}"

class Order:

    def __init__(self, ord_num, product_id, item_type, name, prod_detail, factory_obj, corrupted, corrupted_reason):
        self._ord_num = ord_num
        self._product_id = product_id
        self._item_type = item_type
        self._name = name
        self._prod_detail = prod_detail
        self._factory_obj = factory_obj
        self._corruptedOrNot=corrupted
        self._corrupted_reason = corrupted_reason

    def get_order_num(self):
        return self._ord_num

    def get_item_type(self):
        return self._item_type

    def get_name(self):
        return self._name

    def get_prod_detail(self):
        return self._prod_detail

    def get_quantity(self):
        return self._prod_detail["quantity"]

    def get_product_id(self):
        return self._product_id

    def get_corrupted(self):
        return self._corruptedOrNot

    def get_corrupted_reason(self):
        return self._corrupted_reason

    def set_corrupted_reason(self, corrupted_reason):
        self._corrupted_reason=corrupted_reason

    def __str__(self):
        return f"orderNo: {self._ord_num}"
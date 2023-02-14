import desserts


class Customer():
    def __init__(self, customer_name="Robert"):
        self._customer_name = customer_name
        self._customer_id = 3748327
        self.order_history = []
        self.total_orders = 0


    @property
    def customer_id(self):
        return self.customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value

    def add2history(self, order):
        self.order_history.append(order)
        return self




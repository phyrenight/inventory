class Inventory(object):
    """Keeps track of all products """
    invent = []
    total_inventory = 0
    inventory_value = 0
	
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_space = capacity

    def add_inventory(self, id, price, quantity):
        """ used to add items to inventory and 
            decrease the amount of space available in inventory
        """
        self.invent.append = product(id, price, quantity)
        self.available_space -= quantity
        self.total_inventory += quantity

    def reorder(self, id, how_much):
	    """
	       used to reorder products and for products
	       return by customers.
	    """
        for i in invent:
            if i == id:
                i.refill_product(how_much)

    def print_inventory(self):
	    """
            prints out all of the inventory( id, price, quantity)
        """
         for i in invent:
             print i

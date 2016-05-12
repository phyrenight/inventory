from product import Product
class Inventory(object):
    """Keeps track of all products """
    name = ""
    invent = []
    total_inventory = 0
    inventory_value = 0
	
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.available_space = capacity

    def add_inventory(self, id, price, quantity):
        """ used to add items to inventory and 
            decrease the amount of space available in inventory
        """
        self.invent.append(Product(id, price, quantity))
        self.available_space -= quantity
        self.total_inventory += quantity

    def reorder(self, id, how_much):
        """
           used to reorder products and for products
           return by customers.
        """
        for i in self.invent:
            if i == id:
                i.refill_product(how_much)

    def print_inventory(self):
        """
            prints out all of the inventory( id, price, quantity)
        """
        for i in self.invent:
            print i.id
            print i.price
            print i.quantity
        print "Current available space in this warehouse is {}.".format(self.available_space)
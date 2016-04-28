class Product(object):
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity

    def product_sold(self):
        self.quantity -= 1

    def refill_product(self, how_much):
        self.quantity += how_much
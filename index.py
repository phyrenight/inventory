import product
from inventory import Inventory

def addWarehouse(warehouses):
    """ 
        args: warehouses a list that stores all the warehouses

        function: gets data for the warehouse from the user.

        returns: none
    """
    storage = {}
    print "Enter a name for the warehouse:"
    storage['name'] = raw_input("> ")
    print "Enter the max capacity of the warehouse:"
    storage['capacity'] = int(raw_input("> "))
    warehouses.append(Inventory(storage['name'], storage['capacity']))


def showAllWarehouses(warehouses):
    """
        args: warehouses stores all current warehouses
        function: prints name and capacity for each warehouse
    """
    if len(warehouses) < 1:
        print "There are no warehouses to show."
    else:
        for i in warehouses:
            print "Name: {} capacity: {}".format(i.name, i.capacity)



def test():
    warehouses = []
    showAllWarehouses(warehouses)
    addWarehouse(warehouses)
    warehouses.append(Inventory('two',90))
    showAllWarehouses(warehouses)

test()


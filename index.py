import product
import inventory

def addWarehouse(warehouses):
    """ 
        args: warehouses a list that stores all the warehouses

        function: gets data for the warehouse from the user.

        returns: a dictionary
    """
    storage = {}
    print "Enter a name for the warehouse:"
    storage['name'] = raw_input("> ")
    print "Enter the max capacity of the warehouse:"
    storage['capacity'] = int(raw_input("> "))
    warehouses.append(inventory.Inventory(storage['name'], storage['capacity']))

def main():
    warehouses = []
    addWarehouse(warehouses)
    print warehouses[0].name
    print warehouses[0].capacity 

main()

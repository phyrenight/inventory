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
            print "Warehouse name: {}, Total capacity: {}".format(i.name, i.capacity)


#think about turning findPlace() into a decorator
def findPosition(lst, item_name):
    """
       args: lst will be any list
       function: search through the list for the warehouse/product
       returns: an int this will be the place in the list the 
       warehouse/product is
    """
    count = 0
    for i in lst:
        if i.name == item_name:
        	return count
        else:
            count += 1

# try removing user input to another function and let this function just 
# do the alterations
def renameWarehouse(warehouses):
    """
        args: warehouse list of warehouse.

       changes the name of a warehouse
    """
    showAllWarehouses(warehouses)
    print "what warehouse would you like to rename: \n"
    choice = raw_input("> ") # what if a warehouse is not in the list
    id = findPosition(warehouses, choice)
    
    print "What is the new name for the warehouse: "
    newName = raw_input("> ")
    warehouses[id].name = newName


def deleteWarehouse(warehouses):
    """
        args: warehouses list of warehouses
        funct: deletes a warehouse
    """
    showAllWarehouses(warehouses) # what if there are more warehouse than space on the page
    print "What warehouse would you like to delete:"
    name = raw_input(">")# what if a warehouse entered is not in the list
    id = findPosition(warehouses, name)
    warehouses.pop(id)
    showAllWarehouses(warehouses)
    

def addProduct(warehouses):
    print "What warehouse would you like to add a product to:"
    name = raw_input("> ")
    id = findPosition(warehouses, name)
    warehouse


def test():
    warehouses = []
    showAllWarehouses(warehouses)
    addWarehouse(warehouses)
    warehouses.append(Inventory('two',90))
    warehouses.append(Inventory('North',200))
    showAllWarehouses(warehouses)
    place = findPosition(warehouses, 'North')
    print warehouses[2].name
    showAllWarehouses(warehouses)
    deleteWarehouse(warehouses)



test()


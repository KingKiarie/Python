# Create a simple inventory management system. This project would cover several key concepts, such as object-oriented programming, file I/O, and data manipulation. Here are the requirements for the project:
# Create a class for the inventory item, with the following attributes: name, quantity, and price.
# Create a class for the inventory management system, with the following methods:
# add_item: allows the user to add a new item to the inventory
# remove_item: allows the user to remove an item from the inventory
# update_item: allows the user to update the quantity or price of an item
# display_inventory: displays the current inventory
# Allow the user to load and save the inventory from/to a CSV file

import csv

class inventory:
    def __init__(Item,name,quantity,price):
        Item.name = name
        Item.quantity = quantity
        Item.price = price

class InventorySys:
    def __init__(Item):
        Item.inventory = [] 
    
    def add_item(Item,name,quantity,price):
        item = inventory(name,quantity,price)
        Item.inventory.append(item)
    
    def remove_item(Item,name):
        for item in Item.inventory:
            if item.name == name:
                Item.inventory.pop()
    def update_item(Item,name, quantity_new =None,price_new=None):
        for item in Item.inventory:
            if Item.name ==name:
                if quantity_new != None:
                    Item.quantity = quantity_new
                if Item.price != None:
                    Item.price = price_new
    def display_inventory(Item):
        for item in Item.inventory:
            print(item.name, item.quantity,item.price )
    def write(Item):
        with open('Inventory.csv','w',newline='')as lib:
            writer = csv.writer(lib)
            writer.writerow(['name','quantity','price'])
            for item in Item.inventory:
                writer.writerow([item.name,item.quantity,item.price])
    def read(Item):
        with open('Inventory.csv','r') as lib:
            reader = csv.DictReader(lib)
            for row in reader:
                Item.add_item(row['name'], int(row['quantity']), float(row['price']))

Inventory_function = InventorySys()
Inventory_function.add_item('Kiwi',20,60)
Inventory_function.add_item('Fruits',4,100)
Inventory_function.add_item('Phones',20,12360)
Inventory_function.add_item('Milta',400,7000)
Inventory_function.display_inventory()
Inventory_function.write()
Inventory_function.read()
Inventory_function.remove_item('phones')
Inventory_function.display_inventory()
            
        


     

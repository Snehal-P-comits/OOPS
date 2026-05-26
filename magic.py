class Item:

    def __init__(self, name, value):

        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} worth {self.value} gold"
    '''__str__ method is a special method that is called when we try to convert an object to a string'''

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value

    '''__add__ method is a special method that is called when we try to add two objects together using the + operator
    it takes two parameters: self and other'''
    def __add__(self, other):
        return self.value + other.value
'''            ^              ^
               |              |
               |              |
               |            other: other Item object that we are adding to self
               |
               self: the first item object that we are adding'''
    


sword = Item("Sword", 100)

print(sword)
'''if run without the __str__ method, OP would print the memory address of the sword object which is not very useful
but with the __str__ method defined, it will print the name and value of the sword in a nice format when we print the sword object
the __str__ method is a special method that is called when we try to convert an object

now print(sword) will call the __str__ method and will behave like sword.__str__()
'''

shield = Item("Shield", 150)

print(sword + shield)
#running this directly will give a type error because the + operator does not know how to add two Item objects together
#we define a __add__ method in the Item class to specify how to add two Item objects together
# now sword+shield will call the __add__ method and will behave like sword.__add__(shield)

sword1 = Item("Sword", 100)

sword2 = Item("Sword", 100)

print(sword1 == sword2)
#this will return false because by default, the == operator compares the memory addresses of the two objects, and sword1 and sword2 are two different objects in memory
#we can define a __eq__ method in the Item class to specify how to compare two Item objects for equality

class Inventory:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        print(f"Adding {item} to inventory")
        self.items.append(item)

    def __len__(self):
        return len(self.items)

inventory = Inventory()

inventory.add_item(sword)
'''
Nice
'''

inventory.add_item(shield)

print(f"Inventory has {len(inventory)} items")
#dispite the fact that Inventory has a list of items, it does not have a __len__ method defined,
#because the Len function does not know how to calculate the length of an Inventory object, it will raise a TypeError
#we can define a __len__ method in the Inventory class to specify how to calculate the length of an Inventory object

'''
so,
    the big picture of magic methods is that they 
    allow us to define how our custom classes should behave with built-in functions and operators,
    such as print, +, ==, len, etc. by defining these magic methods,
    we can make our custom classes more intuitive and easier to use,
    and we can also make them work seamlessly with other parts of the Python language.

'''
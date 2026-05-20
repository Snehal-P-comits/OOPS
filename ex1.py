'''
# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code in a way that models real-world entities and their interactions.
# In OOP, we define classes that serve as blueprints for creating objects, which are instances of those classes.
# Each class can have attributes (data) and methods (functions) that define the behavior of the objects created from that class.
# In Python, we can define a class using the class keyword, followed by the name of the class and a colon.
# The body of the class contains the attributes and methods that define the behavior of the objects created from the class.
# In this code, we are defining a class called Character that has a constructor to initialize the character's attributes, a method to display the character's stats,
# and a method to simulate an attack on another character. We then create instances of the Character class and call the attack and display_stats methods to demonstrate how the class works.
'''
#class is a blueprint for creating objects (a particular data structure), providing initial values for state 
# (member variables or attributes), and implementations of behavior (member functions or methods).
# In Python, we define a class using the class keyword, followed by the name of the class and a colon. The body of the class contains the attributes and methods that define the behavior of the objects created from the class.
class Character:
    # Constructor to initialize the character's attributes
    # __init__ is a special method in Python that is called when an object is created from a class
    # and allows the class to initialize the attributes of the object.
    # self is a reference to the current instance of the class 
    # and is used to access variables that belong to the class or methods.
    # In this case,self.<attribute_name> is used to assign the values passed as parameters to the instance variables of the class.
    def __init__(self, name, health, attack_power):
        self.name = name 
        # say there's another variable called name outside the class,
        # self.name refers to the instance variable of the class,
        # while name refers to the parameter passed to the constructor.
        self.health = health
        self.attack_power = attack_power

    # Method to display the character's stats under the same class definition 
    # based on the attributes defined in the constructor
    # here self refers to the instance of the class that is calling the method,
    # allowing us to access the attributes of that specific instance and display them.
    def display_stats(self):
        print("Name:", self.name)
        print("Health:", self.health)
        print("Attack Power:", self.attack_power)

    # Method to simulate an attack on another character
    # The attack method takes another character (target) as an argument
    # and reduces the target's health by the attacker's attack power.
    # target is a parameter that represents the charecter being attacked
    # this parameter isnt defined in the constructor but is used in the attack method to specify which character is being attacked and to access its health attribute to reduce it by the attacker's attack power.
    def attack(self, target):
        target.health -= self.attack_power
        print(self.name, "attacked", target.name)
        print(target.name, "health is now", target.health)

# Create instances of the Character class based on the constructor defined in the class
hero = Character("Knight", 100, 50)
enemy = Character("Goblin", 50, 10)

hero.attack(enemy)

hero.display_stats()
enemy.display_stats()

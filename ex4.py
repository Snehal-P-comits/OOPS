class Character:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    #base attack method defined in the character class which is inherited by all the subclasses
    def attack(self, target):
        print(self.name, "attacks normally")

    #display_stats method defined in the character class which is inherited by all the subclasses
    def display_stats(self):
        print("Name:", self.name)
        print("Health:", self.health)

    def speak(self):
        print(self.name, "says: H!")

class Knight(Character):

    def attack(self, target):

        damage = 20

        target.health -= damage

        #method being overriden to a different attack method for the knight class
        print(self.name, "slashes", target.name)

    def speak(self):
       print(self.name, "says: Hello There! *slashes light saber*")
        


class Wizard(Character):

    def attack(self, target):

        damage = 35

        target.health -= damage

        #method being overriden to a different attack method for the wizard class
        print(self.name, "casts fireball on", target.name)

    def speak(self):
        print(self.name, "says: YOU SHALL NOT PASS! *just casts a spell*")

class Archer(Character):

    def attack(self, target):

        damage = 15

        target.health -= damage

        #method being overriden to a different attack method for the archer class
        print(self.name, "shoots arrow at", target.name)

    def speak(self):
        print(self.name, "says: Oi!.. Up here *shoots an arrow*")

#DUCK TYPING EXAMPLE
def character_speak(character):
    # The speak method is different for each character class because they are overridden in each subclass
    # This is called method overriding
    character.speak()
    # This is an example of Duck Typing in puthon
'''
NICE

POLYMORPHISM:
    Polymorphism is a programming concept that allows objects of different classes to be treated as objects
    of a common superclass. It allows for the use of a single interface to represent different types of objects,
    and it is achieved through method overriding in Python.

METHOD OVERRIDING:
    Method overriding is a feature of object-oriented programming that allows a subclass to provide a specific implementation

DUCK TYPING:
    Duck typing is a programming concept in Python that allows for dynamic typing and flexibility in code.
    In python, we perform polymorphism using a func and that func only sees what the func is calling
    and what it does but not what it is, as long as it has the method that is being called in the func, it will work.
    This is often summarized by the phrase 
        "If it looks like a duck and quacks like a duck, then it is a duck."
'''
# Creating instances for each class
knight = Knight("Obi Wan Kenobi", 100)
wizard = Wizard("Gandalf", 80)
archer = Archer("Hood", 70)
Sith = Wizard("Darth Sidious", 90)

# a list of a few characters
characters = [knight, wizard, archer]

# an itterating loop to call the attack method for each character in the list of characters
for character in characters:
    # The attack method is different for each character class because they are overridden in each subclass
    # This is called method overriding
    # Its exactly what we did in the previous exercise while looking at inheritance
    character.attack(Sith)
    
    character_speak(character)
    print(" ")
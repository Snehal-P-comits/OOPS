#parent class
class Character:

    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def display_stats(self):
        print("Name:", self.name)
        print("Health:", self.health)
        print("Attack:", self.attack_power)

    def attack(self, target):
        target.health -= self.attack_power

        print(self.name, "attacked", target.name)

'''
#child class inheriting from parent class
# here charecter class isnt being passed as an argument to the constructor of the Knight class 
 because it is being inherited from the Character class,
# which means that the Knight class has access to all the attributes and methods of the Character class 
 without needing to explicitly call the constructor of the Character class.'''
#child class inheriting from parent class
class Knight(Character): 
    '''
    # now becouse of this knight class can acess all the attributes and methods of the character class 
     without needing to define them again in the knight class,
     and it can also have its own unique attributes and methods that are specific to the knight class,
     allowing us to create a more specialized version of the character class 
     that has all the functionality of the character class 
     plus any additional functionality that we want to add to the knight class.
     '''
    pass

#similarly this class is also inheriting from character class like the knight class
class Wizard(Character):

    # here we are defining a constructor for the wizard class that takes an additional parameter mana,
    # which is specific to the wizard class and is not inherited from the character class.
    def __init__(self, name, health, attack_power, mana):

        # super() allows us to call the constructor of the parent class from the child class
        # this is necessary because the wizard class is inheriting from the character class,
        # and we need to call the constructor of the character class to initialize the attributes defined in the character class 
        # (name, health, attack_power) for instances of the wizard class.
        super().__init__(name, health, attack_power)
        # you could ask why we didn't use it in knight class
        # because the knight class doesn't have any additional attributes that need to be initialized in its constructor

        # this is the new attribute that is specific to the wizard class and is not inherited from the character class
        self.mana = mana

    # But wizard class has its own unique method unique to the wizard class
    # this method is specific to the wizard class and is not inherited from the character class,
    # which means that it can only be called on instances of the wizard class and not on the ones of the other classes
    def cast_spell(self, target):
        target.health -= 40

        print(self.name, "cast a spell on", target.name)

    #Method overriding
    '''
    # This method is also specific to the wizard class and is not inherited from the character class
    # Dispite the fact that it has the same name as the attack method in the character class
    # This method will override the attack method in the character class for instances of the wizard class
     which means that when we call the attack method on an instance of the wizard class,
NICE
    # It will execute this method instead of the one defined in the character class,
     allowing us to have different behavior for the attack method in the wizard class compared to the character class,
     while still being able to use the attack method defined in the character class for instances of the any other class that inherits from the character class.
    '''
    def attack(self, target):

        target.health -= self.attack_power + 10

        print(self.name, "used magical attack on", target.name)

# here we are creating a new class called witch that inherits from the wizard class,
# which means that the witch class has access to all the attributes and methods of the wizard class
# as well as all the attributes and methods of the character class 
# (since the wizard class inherits from the character class),
# allowing us to create a more specialized version of the wizard class that has all the functionality of the wizard class
# plus any additional functionality that we want to add to the witch class.
class Witch(Wizard):

    def __init__(self, name, health, attack_power, mana, potion_power):
        # super() is being used to create a constructor for the witch class
        # to add the new attribute potion_power to the witch class while still
        super().__init__(name, health, attack_power, mana)
        #new attribute specific to witch class and is not inherited from the wizard class
        self.potion_power = potion_power

    #this method is exclusive for the witch class
    def potion(self, target):
        target.health += self.potion_power
        print(self.name, "used a potion on", target.name)

    # cst_spell method is a method specific to wizard class but 
    # since witch class inherits from wizard class, it can also use the cast_spell method
    # But in this case WE ARE OVERRIDING THIS WITCH
    def cast_spell(self, target):
        target.health -= 69
        print(self.name, "cast a powerful spell on", target.name)
        print("which is more powerful than the spell casted by the wizard class")


# here we are creating an instance of the Knight class
# knight class inherits the constructor and methods from the character class
# so we can do all this without defining the constructor and display_stats method in the knight class
knight = Knight("John Snow", 100, 20)
knight.display_stats()

wizard = Wizard("Potter", 80, 30,100)
wizard.display_stats()

witch = Witch("Hermione", 70, 25,150,10)
witch.display_stats()

wizard.cast_spell(knight)
print(wizard.name, "cast a spell on", knight.name)

print(knight.name, "'s health after wizard's spell:", knight.health)

wizard.attack(knight)
print(wizard.name, "used magical attack on", knight.name)

print(knight.name, "'s health after wizard's attack:", knight.health)

print(wizard.name, "'s mana:", wizard.mana)

witch.attack(wizard)
print(wizard.name, "'s health after witch's spell:", wizard.health)

witch.cast_spell(wizard)
print(wizard.name, "'s health after witch's spell:", wizard.health)

witch.potion(wizard)
print(wizard.name, "'s health after witch's spell:", wizard.health)

witch.cast_spell(wizard)
print(wizard.name, "'s health after witch's spell:", wizard.health)

'''
WHY INHERITANCE?
1. Code Reusability: Inheritance allows us to reuse code from the parent class in the child class
2. Modularity: Inheritance allows us to create a modular code structure where we can define common attributes 
    and methods in a parent class and then create child classes that inherit from the parent class 
    and add their own unique attributes and methods.
3. Polymorphism: Inheritance allows us to use polymorphism, 
    which means that we can use a child class object wherever a parent class object is expected,
    allowing for more flexible and extensible code.
4. Extensibility: Inheritance allows us to extend the functionality of a parent class by creating child classes
    that inherit from the parent class and add their own unique attributes and methods,
    allowing us to create more specialized versions of the parent class 
    without having to modify the original code of the parent class.
'''


'''
Method overriding is technically a form of polymorphism, 
but it is not the same as method overloading. 
Method overriding allows a subclass to provide a specific implementation of a method 
that is already defined in its superclass, 
we'll get to overloading later on
'''
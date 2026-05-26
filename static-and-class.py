class Player:
    total_players = 0 #class variable shared by all instances of the class
    def __init__(self, name, health):
        self.name = name
        self.health = health
        Player.total_players += 1 #basically every time we create a new player, we increment the total_players class variable by 1

    def display(self):
        print(self.name, self.health)

    '''
    @classmethod is a decorator that indicates that the method that follows is a class method
    A class method is a method that is bound to the class and not the instance of the class
    it takes a parameter cls which refers to the class itself, and not the instance of the class
    we can call a class method using the class name, and we can also call it using an instance of the class
    but it will always refer to the class and not the instance'''
    @classmethod
    def show_total_players(cls):
        print("Total Players:", cls.total_players)

    '''
    A class method can also be used as a factory method to create instances of the class with some default values
    for example, we can define a class method called create_default_player that creates a player with a default name and health
    and we can call this class method to create a new player with the default values
    '''
    @classmethod
    def create_default_player(cls):
        return cls("Default", 100)
    
    '''
    @staticmethod is a decorator that indicates that the method that follows is a static method
    A static method is a method that does not take any parameters and is not bound to the class or the instance of the class
    
    it is basically a regular function that is defined inside the class,
    and we can call it using the class name or an instance of the class
    but it does not have access to the class or instance attributes or methods,
    it is just a regular function that is defined inside the class for organizational purposes
    we can use static methods to define utility functions that are related to the class but do not need access to the class or instance
    
    this method does NOT use object data and does NOT use class data but logically belongs to Player system
    and hence is related to the player class, so we define it as a static method inside the class
    '''
    @staticmethod
    def calculate_damage(base, multiplier):
        return base * multiplier

p1 = Player("SPOP", 100)
p2 = Player("Ayrus", 50)


p1.display()
'''
like here we are calling the display method that passes self as its parameter 
and self refers to the object that we are calling the method on,
which is p1 in this case, so it will print the name and health of p1
'''
p2.display()

'''
now we can call the class method to create a new player,
it created a new object of the Player class with the default name and health,
and we can call the display method on this new player object to see its name and health
'''
p3 = Player.create_default_player()
p3.display()

Player.show_total_players()
'''
Nice

show_total_players is a class method that we can call using the class name Player
and it will print the total number of players that have been created so far, which is 3 in this case

attributes like:
        p1.name
        p1.health
    are object attributes that are specific to each instance of the class,

while total_players is a class attribute that is shared by all instances of the class

at the same time Class methods can CREATE objects.
they are called Alternative Constructor or Factory Method
they are used to create objects with some default values or to create objects in a specific way that is different from the regular constructor
'''

'''
calculate_damage is a static method that does NOT use object data and does NOT use class data but logically belongs to Player system
'''
damage = Player.calculate_damage(10, 5)
print(damage)

'''
so,
    the big picture of class methods and static methods is that they allow us to define methods that are related to the class but do not need access to the class or instance attributes or methods,
    class methods are used to define methods that are related to the class and can access class attributes and can also be used as factory methods to create instances of the class with some default values,
    while static methods are used to define utility functions that are related to the class but do not need access to the class or instance attributes or methods.
    by using class methods and static methods, we can organize our code better and make it more modular and easier to maintain.
'''
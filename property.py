class Character:

    def __init__(self, name, health):

        self.name = name
        self._health = health

    '''
    def get_health(self):
        return self._health

    def set_health(self, value):

        if value < 0:
            self._health = 0

        else:
            self._health = value

    this is the traditional way of creating getter and setter methods for the health attribute
    but this code is comparively not so clean and it is not so easy to use as well
    Python gives a cleaner solution in the form of property decorators
    '''
    @property
    def health(self): #getter method for the health attribute

        return self._health

    @health.setter
    def health(self, value): #setter method for the health attribute decorated with the health property's setter decorator

        if value < 0: #Health cant be a -ve value
            self._health = 0

        elif value > 100:#Health cant be more than 100
            self._health = 100

        else: #Health can be set to the value assigned to it
            self._health = value

    '''here we have defined the health attribute as a property and we have defined the getter and setter methods
    for it using the @property and @health.setter decorators respectively
    now we can use the health attribute as if it were a normal attribute
    but it will still have the validation in the setter method to make sure that the health is not a -ve value
    
    it differs from the traditional way of creating getter and setter methods 
    in that we can access the health attribute directly without having to call the getter and setter methods explicitly
    this makes the code cleaner and easier to use

    so @property decorator is used to define a property 
    and the @health.setter decorator is used to define the setter method for the health property
    so when we access the health attribute it will call the getter method and when we assign a value to the health attribute, 
    it will call the setter method
    so this property is directly linked to the attribute _health 
    and we can access it directly without having to call the getter and setter methods explicitly
'''

hero = Character("SPOP", 100)
hero.health = -9999
'''without validation the health would be set as -9999 which is not possible
so we need a validation in the setter method to make sure that the health is not a -ve value'''

print(hero.health)

hero.health = 200

print(hero.health)

'''
This property decorator is useful when we want to add validation or any logic directly to the attribute

Why use property decorators?
lets take this same example
if we didnt use property and we used a function to set the value of health then 
    the health attribute can be set to any value without any validation 
    if we dont use the setter method and directly set the value to the health attribute
    like instead of using the set_health method we can directly use hero.health = -9999
    then the health attribute would be set to -9999 which is not possible and this would lead to bugs in the code
'''
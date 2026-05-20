'''
 we are importing the ABC module to create an abstract base class
    base class which is not meant to be instantiated but only to be inherited by other classes
 The ABC module provides a way to define abstract base classes in Python,
    which are classes that cannot be instantiated and are meant to be inherited by other classes.
 Abstract base classes are used to define a common interface for a group of related classes,
    and they can contain abstract methods that must be implemented by the subclasses.
 In this code, we are importing the ABC module to create an abstract base class for our character classes,
    which will allow us to define a common interface for all our character classes and ensure that they
    implement the necessary methods for our understanding.
'''
from abc import ABC, abstractmethod

"""
    ABC is a helper class that provides a standard way to create an ABC using inheritance.
"""

# we are creating an abstract base class called PaymentMethod
# this class will be inherited by other classes that will implement the pay method
# abstract base class is a class that cannot be instantiated and is meant to be inherited by other classes
class PaymentMethod(ABC):

    # abstract method is a method that is declared but contains no implementation
    # it is meant to be implemented by the subclasses that inherit from the abstract base class
    # it is used to define a common interface for a group of related classes and 
    # ensure that they implement the necessary methods for our understanding
    @abstractmethod
    #@abstractmethod means that Every child class MUST implement this method.
    # its a decorator that is used to indicate that a method is abstract 
    # and must be implemented by the subclasses that inherit from the abstract base class
    def pay(self, amount):
        pass
    ''' This class is NOT meant to create objects. It is ONLY a rule/template for subclasses. '''

#child class inheriting from the abstract base class PaymentMethod
class CreditCardPayment(PaymentMethod):
    # here we are implementing the pay method that is declared in the abstract base class PaymentMethod
    # this method is specific to the CreditCardPayment class and is not inherited from the PaymentMethod class,
    # which means that it can only be called on instances of the CreditCardPayment class 
    # and not on the ones of the other classes that inherit from the PaymentMethod class.
    def pay(self, amount):

        print("Paid", amount, "using Credit Card")

class UPIPayment(PaymentMethod):
    # same goes for this class as the CreditCardPayment class,
    # we are implementing the pay method that is declared in the abstract base class PaymentMethod
    # this method is specific to the UPIPayment class and is not inherited from the Payment
    def pay(self, amount):

        print("Paid", amount, "using UPI")

#remove ''' in the begining and in the ending of this comment to see the error

'''
class CryptoPayment(PaymentMethod):
    pass

#Creating instances for CryptoPayment class
crypto = CryptoPayment()

#if you run this with this bit of code,
#  TypeError: Can't instantiate abstract class CryptoPayment without an implementation for abstract method 'pay'

#This error occurs because the CryptoPayment class is inheriting from the PaymentMethod abstract base class,
#    but it does not implement the pay method that is declared in the PaymentMethod class as an abstract method.
#Since the CryptoPayment class does not provide an implementation for the pay method, it cannot be instantiated 
#    and will raise a TypeError when we try to create an instance of the CryptoPayment class.
#NICE
#This is one of the main purposes of using abstract base classes and abstract methods: 
#    to ensure that subclasses implement the necessary methods and to prevent the instantiation of classes that do not provide implementations for those methods.
'''

#Creating instances for each class
card = CreditCardPayment()
upi = UPIPayment()

#paying with the pay fuc of each class
card.pay(500)
upi.pay(1000)
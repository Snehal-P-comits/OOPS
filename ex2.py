class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        # The double underscore before balance (__balance) 
        # is a convention in Python to indicate that this variable is intended to be private 
        # and should not be accessed directly from outside the class.
        # This is a way to encapsulate the data and protect it from unintended access or modification.
        # This attribute can only be accessed and modified through the methods defined in the class,
        # which allows us to control how the balance is accessed and modified, ensuring that it remains in a valid state.
        # It cant even be inherited by subclasses, making it truly private to the class it is defined in.
        self.__balance = balance

    # Method to get the balance of the account
    # This method allows us to access the balance of the account 
    # without directly accessing the private variable __balance.
    def get_balance(self):
        return self.__balance
    
    # Method to deposit money into the account
    # This method allows us to add money to the account 
    # without directly modifying the private variable __balance.
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    # Method to withdraw money from the account
    # This method allows us to withdraw money from the account
    # without directly modifying the private variable __balance.
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    # Method to transfer money from one account to another
    # This method allows us to transfer money from one account to another
    # without directly modifying the private variable __balance of either account.
    def transfer(self,target,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            target.__balance += amount
            print("Transferred:", amount)
        else:
            print("Insufficient balance")


account1 = BankAccount("Snehal", 5000)
account2 = BankAccount("SPOP", 69420)

# running the below line will raise an AttributeError
# because __balance is a private variable and cannot be accessed directly from outside the class.
# because it is a private variable,
# it can only be accessed through the get_balance method defined in the class, 
# which is the intended way to access the balance of the account.
'''print(account1.__balance)'''

# To access the balance,
# we should use the get_balance method instead of trying to access the __balance variable directly.
print(account1.get_balance())

# To modify the balance, we should use the deposit and withdraw methods defined in the class,
# which will allow us to add or subtract from the balance 
# while still keeping the __balance variable private and protected from direct access.
"""NICE"""
account1.deposit(2000)

# After depositing 2000, the balance should now be 7000 (5000 + 2000).
print(account1.get_balance())

# calling the withdraw method to withdraw 1000 from the account,
# without directly accessing the __balance variable
account1.withdraw(1000)

# After withdrawing 1000, the balance should now be 6000 (7000 - 1000).
print(account1.get_balance())

print("account2 balance before transfer:", account2.get_balance())
# calling the transfer method to transfer 2000 from account1 to account2,
# without directly accessing the __balance variable of either account
account1.transfer(account2, 2000)

# After the transfer, account1 balance should now be 4000 (6000 - 2000)
print("account1 balance after transfer:", account1.get_balance())
# After the transfer, account2 balance should now be 71420 (69420 + 2000)
print("account2 balance after transfer:", account2.get_balance())


# Even if we try to directly modify the private variable __balance from outside the class
account1.__balance = -999999
# Even though we have assigned a new value to account1.__balance,
# it does not change the actual balance of the account,
# because __balance is a private variable and cannot be accessed or modified directly from outside the class
print(account1.get_balance())




"""WHY USE PRIVATE VARIABLES?
1. Encapsulation: Private variables help to encapsulate the internal state of an object, 
   preventing external code from directly accessing and modifying it. 
   This allows the class to control how its data is accessed and modified, 
   ensuring that it remains in a valid state.

   2. Data Integrity: By making variables private, you can enforce data integrity by controlling how they are accessed and modified.
   This can help prevent bugs and unintended side effects that may arise from direct access to the variables.

   3. Abstraction: Private variables allow you to hide the implementation details of a class from the outside world,
   providing a clear and simple interface for interacting with the class.
   This can make it easier to use and understand the class,
   as well as allowing you to change the implementation without affecting external code that relies on the class.

   4. Security: Private variables can help to improve the security of your code 
   by preventing unauthorized access to sensitive data.
   By making variables private, you can ensure that only authorized code can access and modify them,
   reducing the risk of data breaches and other security issues.

   """


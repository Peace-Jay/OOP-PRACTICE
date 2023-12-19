#PRACTICE ON OOP
#1. CLASS AND OBJECT
class Food:
    def __init__(self, rice, fruit):
        self.rice = rice
        self.fruit = fruit

    def display_info(self):
        print("peace ordered",  self.rice,"rice", "with", self.fruit, "fruit")

#object creation
order1 = Food("jollof", "orange")
order2 = Food("fried", "apple")

#accessing object attributes and methods
order1.display_info()
order2.display_info()

#2.INHERITANCE
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"

#object creation
dog = Dog("Hilda")
cat = Cat("Whiskers")

#accessing method
print("dogs barks",  dog.speak())
print("cat cries",  cat.speak())

#3.ENCAPSULATION
class BankAccount:
    def __init__(self, account_owner, account_balance=0):
        self.owner = account_owner
        self.__balance = account_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self.__balance

    def display_info(self):
        print("Account owner:", self.owner)
        print("Balance:", self.__balance)

#Object creation
account = BankAccount("Peace Jay")

#accesing
account.deposit(5000)
account.deposit(2000)

account.display_info()

#4.CLASS METHODS
class BankAccount:
    total_accounts = 0

    def __init__(self, account_holder, balance=0):
        self._account_holder = account_holder
        self.__balance = balance
        BankAccount.total_accounts += 1

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

#Created Bank Instance
account1 = BankAccount("Peace")
account2 = BankAccount("Favour")

print(BankAccount.get_total_accounts())
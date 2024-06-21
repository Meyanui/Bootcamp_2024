import datetime
class Car():
    # Initializer / Instance Attributes
    def __init__(self, name, price):
        self.name = name
        self.price = price

first_car = Car("Toyota", 2000)
second_car = Car("Mercedes", 15000)
third_car = Car("Nissan", 7000) 

print(f"\nThe name of my first car is {first_car.name} and the price is {first_car.price}\n")
#*************************************************************************************************

# Analyse the code below. What will be the ouput ?
# Explain the goal of the `__init__()` method

# class Point():
#     def __init__(self, 3, 4):
#       self.x = 3
#       self.y = 4

#*******************************************************************************

#The INSTANCE MEthod
class Car():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def rename_Car(self, new_name):
        self.name = new_name

    def presentation_car(self):
        print(f"\nMy name is {self.name} and my price is ${self.price}")

    #Reduce price
    def reduce_price(self, percentage):
        self.price = (self.price - (self.price * percentage)/100)
        return self.price    
    
    def print_my_name(self):
        print(f"\nMy name is {self.name}\n")
        

    def print_my_price(self):
        print(f"\nMy price is {self.price}\n")

  

first_car = Car("Toyota", 2000)
second_car = Car("Mercedes", 15000)
third_car = Car("Nissan", 7000)

# print(f"\nThe name of my first car is {first_car.name} and the price is {first_car.price}\n")
# first_car.rename_Car("Range Rover")
# print(f"\nThe name of my first car is {first_car.name}")

second_car.print_my_price()
second_car.reduce_price(50)
second_car.print_my_price()
#************************************************************************************

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print("Hello my name is " + self.name)

first_person = Person("John", 36)
first_person.show_details()
#********************************************************************************************

class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount} day: {datetime.date.today()} hour : {datetime.datetime.now()}\n")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)

my_account = BankAccount(12345,000)

my_account.deposit(60000)
my_account.view_balance()
my_account.withdraw(30000)
my_account.view_transactions()


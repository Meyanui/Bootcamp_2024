print ("Hello world")
x = (9+9)
print("our answer is:",x)
print("Addition", 5+10)
print("Subtraction", 20-5)
print("Division", 30/3)
print("Product", 15*2)
print("Modulo", 30 % 3)

x = 10
print(type(x))

y = 10.8
print(type(y))

z = False
print(type(z))

a = "yeah bro"
print(type(a))

print("hello men, how was your day? \n ")
print("hello men, how was your day?" .capitalize())
print("hello men, how was your day?" .upper())
print("HELLO MEN, HOW WAS YOUR DAY?" .lower())


# In the python shell, Create a variable called my_age, use python to know how old you will be in 123879 years
my_age = 30
future = 123879
print(my_age + future)

# convert integer to strings
my_age = 15
print(my_age, type(my_age))

my_age_converted_to_string = str(my_age)
print(my_age_converted_to_string, type(my_age_converted_to_string))

# concatinate
print("ma" + "ma")
print("ma" * 2)
# print("ma" + 2)
print(("ma" + " " + "ma"))


# In the python shell, Create a variable called first_name 
# and a variable called last_name, and then print your full name 
# using those two variables

first_name = "Josmingo"
last_name = "Bandema"
print(first_name + " " + last_name)
print(first_name, last_name )
print(first_name + last_name)

# comparing operators
x = 10
y = 20 
print(x<=y)


#Increment a variable
number = 2
number += 5
print("\n the new number is : " ,number)

#decrement a variable
number = 2
number -= 5
print("\n the new number is : ",number)

# string formating
car_name = "BMW"
model = "1ER 2024"
Car = f"{car_name} {model}"
my_message = f"Tycoons only drive {Car.upper()} cars"
my_message_ = f"Tycoons only drive {Car.upper()} cars, and they are good"
print(my_message_)


#conditional statements
a = 33
b = 200

if a>b:
  print("a es plus petit que b")
else:
  print("a es plus petit que b")


marks = float(input("Enter your score : "))
if marks < 8:
  print("\nyou are very weak!!!")
elif marks > 8 and marks < 12:
  print("\nyou are weak!!!")
elif marks > 12 and marks < 15:
  print("\nyou are Average!!!")
elif marks > 15 and marks <= 20:
  print("\nyou are Excellent!!!")
else:
  print("\nEnter a valid value!!!")
  










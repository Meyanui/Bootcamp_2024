# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world

# print("Hello world\n" * 4, end="")
print("meyanui valentino\n".capitalize() * 5)

# Ex 2
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

result = (99 ** 3) * 8
# print(result)

# Ex 3 
# Predict the output of the following code snippets:
x = 5 < 3
print(x)

n = 3 == 3
print(n)

o = 3 == "3"
print(o)

# q = "3" > 3
# print(q)

# r = "Hello" == "hello"
# print(r)

# Ex 4
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = "Hp Envy X360" 
print(f"I have an {computer_brand} Computer")

# Ex 5
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = "Meyanui Val"
age = 50
shoe_size = 42.4
info = f"My name is {name}, I am {age} years old, and my shoe size is {shoe_size}."
print(info)


# Ex 6 : A & B
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

a = 5
b = 10
if a > b:
  print("Hello World")
else:
  print("Try again")


# Ex 7 : Odd Or Even
# Write code that asks the user for a number and determines whether this number is odd or even.
# Ask the user for a number
number = int(input("Enter a number: "))

# Determine if the number is odd or even
if number % 2 == 0:         # (If the number is divisible by 2)
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
  

# Ex 8 : What’s Your Name ?
# Write code that asks the user for their name and determines whether 
# or not you have the same name, print out a funny message based on the outcome.

# Define your name
my_name = "Josiane"

# Ask the user for their name
# user_name = str(input("Enter a name: ")) or

user_name = input("What's your name? ")

# Determine if the names match and print a funny message
if user_name == my_name:
    print(f"Wow, we have the same name, {user_name}! Are you my long-lost twin?")
else:
    print(f"Nice to meet you, {user_name}! But sorry, the world only knows one {my_name}.")

# Ex 9 : 
    # Tall Enough To Ride A Roller Coaster
# Write code that will ask the user for their height in centimeters.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

height = int(input("Please enter your height in centimeters: "))

if height > 145:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride.")




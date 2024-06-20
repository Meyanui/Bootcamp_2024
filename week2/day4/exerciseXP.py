#Exercise 1 : What Are You Learning ?
# Write a function called display_message() that prints one sentence telling 
# everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message():
  print("\nHello, everybody. I am currently learning FUNCTIONS in Python")
display_message()
#**********************************************************************************

# Exercise 2: What’s Your Favorite Book?
  # Write a function called favorite_book() that accepts one parameter called title.
  # The function should print a message, such as "One of my favorite books is <title>".
  # For example: “One of my favorite books is Alice in Wonderland”
  # Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
  print(f"\nOne of my favorite books is {title}.")

favorite_book("Alice in Wonderland")
#**********************************************************************************

# Exercise 3 : Some Geography
  # Write a function called describe_city() that accepts the name of a city and its country as parameters.
  # The function should print a simple sentence, such as "<city> is in <country>".
  # For example “Reykjavik is in Iceland”
  # Give the country parameter a default value.
  # Call your function.

def describe_city(name, country = "Ghana"):
  print(f"{name} is in {country}")

describe_city("Yaounde", "Cameroon")
#*************************************--------------***************************************************

# Exercise 4 : Random
  # Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
  # Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random
def game(number):
  if number <=1 or number >= 100:
    print("\nPlease Enter a number between 1 and 100\n")
    return number
  else:
    random_number = random.randint(1, 100)
    if random_number == number:
      print("Congratulations! You have found the number")
    else:
      print("Oh No! You missed the number ", random_number)

number = int(input("Enter a number between 1 and 100: "))
game(number)
#**************************************************************************************

# Exercise 5 : Let’s Create Some Personalized Shirts!
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().
# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size = "large", message = "I love python"):
  print(f"\nThe size of the shirt is {size} and the text is {message}\n")

make_shirt("Large")
make_shirt("medium")

make_shirt(size="Small", message="Python is awesome!")
#**************************************************************************************************

# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# def show_magicians(magicians):
#   for magician in magicians:
#     print(magician)

# show_magicians(magician_names)

# def make_great(magicians):
#   for i in range(len(magicians)):
#     magicians[i] = f"{magicians[i]} the Great"

# make_great(magician_names)
# show_magicians(magician_names)
#****************************************************************************************

# List of magician names
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    #Print the name of each magician in the list.
    for magician in magicians:
        print(magician)

def make_great(magicians):
  return [f"{magician} the Great" for magician in magicians]

# Call the function to get the modified list
great_magicians = make_great(magician_names)

# Call the function to display the modified list
show_magicians(great_magicians)




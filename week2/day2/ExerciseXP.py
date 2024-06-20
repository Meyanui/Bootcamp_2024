# Exercise 1 : Favorite Numbers
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.


# my_fav_numbers = {1,3,7,12,18}
my_fav_numbers = {21, 34, 55, 89, 144}
# Add two new numbers to the set
my_fav_numbers.add(29)
my_fav_numbers.add(42)

# To remove the last number
my_fav_numbers.pop()

# Create a set called friend_fav_numbers with your friend's favorite numbers
friend_fav_numbers = {5, 10, 15, 20}

# Concatenate variables 
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers) #OR
our_fav_numbers = my_fav_numbers | friend_fav_numbers #OR
# our_fav_numbers = set.union(my_fav_numbers, friend_fav_numbers) #OR


print("\nMy Favorite Numbers: \n", my_fav_numbers)
print("\nFriend's Favorite Numbers: \n", friend_fav_numbers)
print("\nOur Favorite Numbers: \n", our_fav_numbers)

#*************************************************************
#Exercise 2: Tuple
# Given a tuple which value is integers, 
# is it possible to add more integers to the tuple?

tuple = (2, 6, 9, 14)
tuple_1 = (17, 19)
new_tuple = (tuple + tuple_1)
print(f"\n our New tuple is: {new_tuple}, \n")

#*****************************************************************
#Exercise 3: List
#Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# Initial list
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove elements from the list
basket.remove("Banana")
basket.remove("Blueberries") 

basket.append("Kiwi") # Add "Kiwi" to the end of the list

basket.insert(0, "Apples") # Add "Apples" to the beginning of the list
apple_count = basket.count("Apples") # Count how many apples are in the basket
basket.clear() # Empty the basket

print(basket)  
print(apple_count)  
#******************************************************************************

#Exercise 4: Floats
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 
# (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?
                # (Using a While Loop method)

sequence = []
value = 1.5
while value <= 5:
    sequence.append(value)
    value += 0.5

print(sequence) 
#***********************************************************************************

# Exercise 5: For Loop
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), 
# print out every element which has an even index.

for number in range(1, 21): #Indices start from 0. When dealing with the range from 1 to 20, we need to consider the 0-based indexing
    print(number)
#********************************************************************************************

# Exercise 6 : While Loop
# Replace 'YourName' with your actual name
# Write a while loop that will continuously ask the user for their name, 
# unless the input is equal to your name.

my_name = "Valentino"

while True:
    user_name = input("Please enter your name: ")
    if user_name == my_name:
        print(f"Hello, {my_name}!")
        break
# ****************-----------------------****************************************

# Exercise 7: Favorite Fruits
    # Ask the user to input their favorite fruit(s) (one or several fruits).
    # Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
    # Store the favorite fruit(s) in a list (convert the string of words into a list of words).
    # Now that we have a list of fruits, ask the user to input a name of any fruit.
    # If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
    # If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# Ask the user to input their favorite fruit(s)
favorite_fruits_input = input("Kindly enter your favorite fruits, separated by a single space (e.g., 'apple mango cherry'): ")

# Convert the string of fruits into a list of words
favorite_fruits_list = favorite_fruits_input.split()

# Ask the user to input the name of any fruit
chosen_fruit = input("Please enter the name of any fruit: ")

# Check if the chosen fruit is in the list of favorite fruits
if chosen_fruit in favorite_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")
# ****************-----------------------****************************************

# Exercise 8: Who Ordered A Pizza ?
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings = []
price_per_topping = 2.5
base_price = 10

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"I'll add {topping} to your pizza.")

total_price = base_price + len(toppings) * price_per_topping
print(f"\nToppings on your pizza: {', '.join(toppings)}")
print(f"Total price: ${total_price:.2f}")
# ****************-----------------------****************************************

# Exercise 9: Cinemax

# Given ticket prices
ticket_prices = {
    "child": 0,
    "adult": 10,
    "senior": 15
}

# Ask for family members' ages
def get_age():
    try:
        age = int(input("Enter age: "))
        return age
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        return get_age()

def calculate_total_cost():
    total_cost = 0
    family_size = int(input("Enter the number of family members: "))

    for _ in range(family_size):
        age = get_age()
        if age < 3:
            continue
        elif 3 <= age <= 12:
            total_cost += ticket_prices["adult"]
        else:
            total_cost += ticket_prices["senior"]

    print(f"Total cost for the family: ${total_cost:.2f}")

# Call the function
calculate_total_cost()

#****************==================*********************************************************************

# Exercise 10 : Sandwich Orders

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
        # I made your tuna sandwich
        # I made your avocado sandwich
        # I made your egg sandwich
        # I made your chicken sandwich


sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

        # Remove all occurrences of "Pastrami sandwich"
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

        # Prepare the finished sandwiches
finished_sandwiches = []
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich.lower()}")

# Alternatively, - list comprehension for creating finished_sandwiches:
# finished_sandwiches = [sandwich for sandwich in sandwich_orders]

# Print the final list of made sandwiches
print("\nFinal list of made sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)


# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# zipping the values
zipped_values = zip(keys, values)
print(zipped_values)

# converting the values into a dictionary
dictionary = dict(zipped_values)
print(dictionary)

# **********************************************************************************************
#  Exercise 2 : Cinemax #2
# A movie theater charges different ticket prices depending on a person’s age.
  # if a person is under the age of 3, the ticket is free.
  # if they are between 3 and 12, the ticket is $10.
  # if they are over the age of 12, the ticket is $15.

# Given the following object:

    # family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

def get_ticket_price(age):
    if age < 3: # if a person is under the age of 3, the ticket is free.
        return 0  
    elif 3 <= age <= 12: # if they are between 3 and 12, the ticket is $10.
        return 10  
    else:
        return 15  # if they are over the age of 12, the ticket is $15.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

print("Individual costs:")      # How much does each family member have to pay ?
for name, age in family.items():
    price = get_ticket_price(age)
    total_cost += price
    print(f"{name.capitalize()}: ${price}")

print(f"\nTotal cost for the family: ${total_cost}")
# -----*******************************************************************************----------------

# Exercise 3: Zara

# Creating the brand dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Changing the number of stores to 2
brand["number_stores"] = 2

# A sentence that explains who Zara's clients are
print(f"Zara's clients are men, women, children, and those looking for home products.")

# key called country_creation with a value of Spain
brand["country_creation"] = "Spain"

# To verify if the key international_competitors is in the dictionary, adding the store Desigual.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Delete the information about the date of creation
del brand["creation_date"]

# Printing the last international competitor
print(f"The last international competitor is {brand['international_competitors'][-1]}.")

# Print the major clothes colors in the US
print(f"The major clothes colors in the US are {', '.join(brand['major_color']['US'])}.")

# Print the amount of key value pairs (i.e., length of the dictionary)
print(f"The number of key-value pairs in the brand dictionary is {len(brand)}.")

# Print the keys of the dictionary
print("The keys of the brand dictionary are:", list(brand.keys()))

# Create another dictionary called more_on_zara with additional details
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# Adding 'more_on_zara' to the dictionary brand
brand.update(more_on_zara)

# value of the key number_stores
print(f"The number of stores is now {brand['number_stores']}.")
# -----------------*******************************************************---------------------------

# Exercise 4 : Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# Recreate disney_users_A using a for loop
disney_users_A = {user: idx for idx, user in enumerate(users)}

# Recreate disney_users_B using a for loop
disney_users_B = {idx: user for idx, user in enumerate(users)}

# Recreate disney_users_C using a method that sorts the dictionary alphabetically
disney_users_C = {user: idx for idx, user in enumerate(sorted(users))}

# Recreate disney_users_A for characters with names containing the letter "i"
disney_users_A_i = {user: idx for idx, user in enumerate(users) if 'i' in user}

# Recreate disney_users_A for characters with names starting with the letter "m" or "p"
disney_users_A_mp = {user: idx for idx, user in enumerate(users) if user[0].lower() in ['m', 'p']}

# Print the results to verify
print("disney_users_A:", disney_users_A)
print("disney_users_B:", disney_users_B)
print("disney_users_C:", disney_users_C)
print("disney_users_A (names containing 'i'):", disney_users_A_i)
print("disney_users_A (names starting with 'm' or 'p'):", disney_users_A_mp)





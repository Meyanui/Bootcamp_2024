# Ask the user for a number and a length.
# Create a program that prints a list of multiples 
# of the number until the list length reaches length.

# # Ask the user for a number and a length
# number = int(input("Enter a number: "))
# length = int(input("Enter the length of the list: "))

# # Initialize an empty list to store the multiples
# multiples = []

# # Use a for loop to generate the multiples
# for i in range(1, length + 1):
#     multiples.append(number * i)

# # Print the list of multiples
# print("The list of multiples is:", multiples)


# OR*****************
# number = int(input("Enter your number"))
# length = int(input("Enter the length in the list"))

# nb = number
# my_liste = []
# while len(my_liste) < length:
#   my_liste.append(nb)
#   nb += number
# print(f"\n{my_liste}\n")
# **************************************************************************************

# Ex. 2
# Write a program that asks a string to the user, 
# and display a new string with any duplicate consecutive letters removed.

# def remove_consecutive_duplicates(input_string):
#     if not input_string:
#         return ""
    
#     result = [input_string[0]]  # Initialize the result list with the first character
    
#     for char in input_string[1:]:
#         if char != result[-1]:  # Compare with the last character in the result list
#             result.append(char)
    
#     return ''.join(result)

# # Ask the user for a string
# user_input = input("Enter a string: ")

# # Display the new string with consecutive duplicates removed
# print("Result:", remove_consecutive_duplicates(user_input))

# OR*****************
user_word = input("\nEnter your word\n")
result = ''
for i in user_word:
  if i not in result:
    result = result + i
print(result)




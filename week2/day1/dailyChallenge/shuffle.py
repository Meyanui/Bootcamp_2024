import random
# Define the string you want to shuffle
my_string = input("Type the word to be shuffled: ")

# Convert the string to a list of characters
char_list = list(my_string)

# Use the shuffle method to shuffle the list of characters
random.shuffle(char_list)

# Convert the shuffled list of characters back to a string
shuffled_string = ''.join(char_list)

# Print the newly jumbled string
print(shuffled_string)
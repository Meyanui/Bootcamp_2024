# Defining the string to construct
my_string =  input("What is your Name: ")

# Initializing an empty string to hold the constructed string
constructed_string = ""

# Use a for loop to iterate over each character in the string
for char in my_string:
    
    # Adding current character to the constructed string
    constructed_string += char

    # Print the constructed string so far
    print(constructed_string)
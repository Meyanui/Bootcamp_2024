# python check_string_length
def check_string_length():
   # Ask the user for a string
    user_string = input("Please enter a string: ")

    # Check the length of the string
    if len(user_string) < 10:
        print("string not long enough")
    elif len(user_string) > 10:
        print("string too long")

    else:
        print("perfect string")

        # Continue the exercise by printing the first and last characters
        print(f"The first character is: {user_string[0]}")
        print(f"The last character is: {user_string[-1]}")

        # Main function to run the script
if __name__ == "__main__":
    check_string_length()
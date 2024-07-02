# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.
# Download this word list
# Save it in your development directory.
# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

#####################################################################################
import random

def get_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return words

def get_random_sentence(words, length):
    random_words = random.sample(words, length)
    sentence = ' '.join(random_words).lower()
    return sentence

def main():
    print("This program generates a random sentence based on a specified length.")
    try:
        length = int(input("Enter the length of the sentence (an integer between 2 and 20): "))
        if length < 2 or length > 20:
            print("Error: Length must be between 2 and 20.")
            return
        
        words = get_words_from_file('/mnt/data/word_list.txt')
        sentence = get_random_sentence(words, length)
        print(f"Generated sentence: {sentence}")
    
    except ValueError:
        print("Error: Please enter a valid integer between 2 and 20.")

if __name__ == "__main__":
    main()

# Challenge 1 : Sorting
# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Accept a comma-separated sequence of words as input

def sort_words_alphabetically():
    # Accept a comma-separated sequence of words as input
    input_sequence = input("Enter a comma-separated sequence of words: ")

    # Split the input string into a list of words and sort them alphabetically
    sorted_words = sorted([word.strip() for word in input_sequence.split(",")])

    # Join the sorted list back into a comma-separated sequence
    output_sequence = ",".join(sorted_words)
    print(output_sequence)

sort_words_alphabetically()

#################################################################################

# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

def find_longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize variables to keep track of the longest word
    longest_word = ""
    
    # Iterate through the words to find the longest one
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

sentence = input("Kindly enter any sentence of your choice")
print(find_longest_word(sentence)) 






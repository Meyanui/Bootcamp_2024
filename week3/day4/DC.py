

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()  # To split the text into words
        frequency = words.count(word)  # To count the occurrences of the word

        if frequency == 0:
            return f"The word '{word}' is not found in the text."
        return frequency

    def most_common_word(self):
        words = self.text.split()  # Split the text into words
        word_count = {}  # Dictionary to store word frequencies

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        # Find the word with the highest frequency
        most_common = max(word_count, key=word_count.get)
        return most_common

    def unique_words(self):
        words = self.text.split()  # Split the text into words
        unique = set(words)  # Convert the list to a set to remove duplicates
        return list(unique)  # Convert the set back to a list

text_string = "A good book, a really good book, would sometimes cost as much as a house, a good house."

# this is to create an instance of the Text class
text_analysis = Text(text_string)

# In order to know the frequency of a specific word
print(text_analysis.word_frequency("good"))
print(text_analysis.word_frequency("bad")) 

print(text_analysis.most_common_word()) 

print(text_analysis.unique_words())  # Output: List of unique words in the text
################################################################################

#PART II

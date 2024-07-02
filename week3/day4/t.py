
class Text:
    def __init__(self, content):
        self.content = content
    
    def word_frequency(self, word):
        words = self.content.split()
        frequency = words.count(word)
        if frequency == 0:
            return f"The word '{word}' is not found in the text."
        else:
            return f"The word '{word}' appears {frequency} times in the text."
    
    def most_common_word(self):
        words = self.content.split()
        if not words:
            return "The text is empty."
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        most_common = max(word_counts, key=word_counts.get)
        return f"The most common word is '{most_common}' with {word_counts[most_common]} occurrences."
    
    def unique_words(self):
        words = self.content.split()
        unique_words = set(words)
        return list(unique_words)
    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return cls(content)

# Using the class to read from the provided 'the_stranger.txt' file
text_instance = Text.from_file('/the_stranger.txt')

# Printing the content of the text instance to verify
print(text_instance.content[:500])  # Print first 500 characters for verification


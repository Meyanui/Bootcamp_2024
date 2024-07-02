import random


def get_words_from_file(filename):
  '''
  This function reads file content and returns the word as a list
  '''
  with open(filename, 'r') as file:
    words = file.read().split()

    return words
  
def get_random_sentence(words, length):
  '''
  This function permits us to create a sentence
  '''
  random_words = random.sample(words, length)
  ["Django" "is" "A" "web" "development" "Application"]
  sentence = ' '.join(random_words).lower() 

  return sentence

#Creating the main function
def main():
  '''
  This is the principal function used to generate random sentences
  '''
  print("This program generates a random sentence of specified length")

  length = int(input("Enter the length of the sentence between 2 and 20): \n")
  
  try:
    if length < 2 or length > 20:
      print("Error. please enter a number between 2 and 20")

  except ValueError:
    print("Invalid input. kindly enter a valid value (eg 5, etc)")

#Read the words from the file

words = get_words_from_file("wordlist.txt")

#Generate the random sentence

try:
  sentence = get_random_sentence(words = words, length = length):
  print()

  
               

  
            
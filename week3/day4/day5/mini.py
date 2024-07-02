
# Valentine =  to Build the main file

# Gilbert = well commented codes

# Einstein = Build the second part of the File

# Josiane = present the project - documentation of the project

# Alain = Manager of the entire work 
# ##################################################################################################

# create a menu to ask the user to give us all the names of the words that are in the world. 
# if valid, let it print this is an english word,
# later it prints all the anagrams

#####################################################################################################
import os
os.system("color")

class Anagram_checker():
  def __init__(self) -> None:
    pass

  def word_checkers(self, word1, word2):
    self.word1 = word1
    self.word2 = word2

  #Converting the words into lists
    check_list1 = list(self.word1)
    check_list2 = list(self.word2)

    return(sorted(check_list1) == sorted(check_list2))
  

# take word1 and split into a list of characters
word_list1 = input("Kindly enter your first word here: ")
word_list2 = input("\nKindly enter your second word here: ")
print(f'Your two words are [\033[1m{word_list1}\033[0m] and [\033[1m{word_list2}\033[0m]\n')








    
    
  



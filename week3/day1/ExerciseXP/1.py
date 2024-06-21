# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# # Instantiate three Cat (Creating the 3 cats)
# cat1 = Cat("Whiskers", 2)
# cat2 = Cat("Mittens", 3)
# cat3 = Cat("Shadow", 4) 
# 
# # Print details of the cats to verify
# print(f"Cat 1: Name = {cat1.name}, Age = {cat1.age}")
# print(f"Cat 2: Name = {cat2.name}, Age = {cat2.age}")
# print(f"Cat 3: Name = {cat3.name}, Age = {cat3.age}")

# # OR ********************

cat1 = Cat(cat_name = "Minou", cat_age= 2)
cat2 = Cat(cat_name = "Shamba", cat_age= 8)
cat3 = Cat(cat_name = "Dimba", cat_age= 6)

cats = [cat1, cat2, cat3]

# create a function to find the oldest cat
def find_oldest_cat(cats):
    oldest_cat = max(cats, key = lambda cat: cat.age)
    return oldest_cat

oldest_cat = find_oldest_cat(cats)
print(f"\nThe oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old \n")
#****************************************************************************************************

# 🌟 Exercise 3 : Who’s The Song Producer?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example: stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

our_song = [
    "There’s a lady who's sure", 
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
    ]

#To create object of the song class
new_song = Song(our_song)

 #to call the class
new_song.sing_me_a_song()
